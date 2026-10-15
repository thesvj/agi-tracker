# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml", "matplotlib"]
# ///
"""Pull primary-source data and redraw the figures.

Run:  uv run src/update_data.py

Sources (primary only):
  METR Time Horizon 1.1  https://metr.org/assets/benchmark_results_1_1.yaml
  Epoch Capabilities Index https://epoch.ai/data/eci_scores.csv
  Epoch benchmark data     https://epoch.ai/data/benchmark_data.zip

Writes data/metr_time_horizons.csv, data/eci_scores.csv, data/eci_frontier.csv,
data/epoch_top_results.csv, figures/metr_time_horizon.png, figures/eci_frontier.png,
figures/test_status.png and data/SNAPSHOT.json. The status chart is drawn from
data/test_status.csv, which is kept by hand.
"""
import csv
import datetime as dt
import io
import json
import pathlib
import urllib.request
import zipfile

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA, FIG = ROOT / "data", ROOT / "figures"
METR_URL = "https://metr.org/assets/benchmark_results_1_1.yaml"
ECI_URL = "https://epoch.ai/data/eci_scores.csv"
BENCH_URL = "https://epoch.ai/data/benchmark_data.zip"
# Benchmarks the tracker cites from Epoch's data: file name, score column, label.
BENCHES = [
    ("frontiermath_tier_4_v2.csv", "Best score (across scorers)", "FrontierMath Tier 4 (v2)"),
    ("frontiermath_erdos.csv", "Best score (across scorers)", "FrontierMath: Erdős"),
    ("arc_agi_2_external.csv", "Score", "ARC-AGI-2"),
    ("hle_external.csv", "Accuracy", "Humanity's Last Exam"),
]
STATUS_COLORS = {"Not met": "#c53030", "Partly": "#d69e2e", "Met": "#2f855a"}


def fetch(url, raw=False):
    req = urllib.request.Request(url, headers={"User-Agent": "agi-tracker/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        body = r.read()
    return body if raw else body.decode()


def metr():
    d = yaml.safe_load(fetch(METR_URL))
    rows = []
    for key, v in d["results"].items():
        m = v["metrics"]
        rows.append({
            "model": key,
            "release_date": str(v["release_date"]),
            "p50_hours": round(m["p50_horizon_length"]["estimate"] / 60, 3),
            "p50_ci_low_hours": round(m["p50_horizon_length"]["ci_low"] / 60, 3),
            "p50_ci_high_hours": round(m["p50_horizon_length"]["ci_high"] / 60, 3),
            "p80_hours": round(m["p80_horizon_length"]["estimate"] / 60, 3),
            "is_sota": m.get("is_sota", False),
        })
    rows.sort(key=lambda r: r["release_date"])
    write_csv(DATA / "metr_time_horizons.csv", rows)
    doubling = d.get("doubling_time_in_days", {})

    sota = [r for r in rows if r["is_sota"] and r["p50_hours"] > 0]
    x = [dt.date.fromisoformat(r["release_date"]) for r in sota]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.errorbar(x, [r["p50_hours"] for r in sota],
                yerr=[[r["p50_hours"] - r["p50_ci_low_hours"] for r in sota],
                      [r["p50_ci_high_hours"] - r["p50_hours"] for r in sota]],
                fmt="o", color="#2b6cb0", ecolor="#a0aec0", capsize=2, label="50% success")
    ax.plot(x, [r["p80_hours"] for r in sota], "s", color="#c05621", label="80% success")
    ax.axhline(16, ls="--", color="#718096", lw=1)
    ax.text(x[0], 18, "above 16 h: METR says unreliable", fontsize=8, color="#4a5568")
    ax.set_yscale("log")
    ax.set_ylabel("Task length a human expert needs (hours, log scale)")
    ax.set_title("METR time horizon: how long a task AI agents can finish (frontier models)")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.legend(loc="lower right")
    ax.grid(alpha=0.3)
    fig.text(0.01, 0.01, f"Source: METR Time Horizon 1.1 ({METR_URL})", fontsize=7, color="#4a5568")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(FIG / "metr_time_horizon.png", dpi=150)
    plt.close(fig)
    return rows, doubling


def eci():
    text = fetch(ECI_URL)
    (DATA / "eci_scores.csv").write_text(text)
    rows = [r for r in csv.DictReader(io.StringIO(text)) if r["eci"] and r["date"]]
    rows.sort(key=lambda r: r["date"])
    frontier, best = [], {"closed": -1.0, "open": -1.0}
    for r in rows:
        group = "open" if r["Accessibility group"] == "Open weights" else "closed"
        if float(r["eci"]) > best[group]:
            best[group] = float(r["eci"])
            frontier.append({"group": group, "model": r["Display name"], "date": r["date"],
                             "org": r["Organization"], "eci": r["eci"],
                             "ci_low": r["eci_ci_low"], "ci_high": r["eci_ci_high"]})
    write_csv(DATA / "eci_frontier.csv", frontier)

    fig, ax = plt.subplots(figsize=(8, 4.5))
    for group, color, label in [("closed", "#2b6cb0", "Best closed model so far"),
                                ("open", "#2f855a", "Best open-weights model so far")]:
        pts = [f for f in frontier if f["group"] == group]
        ax.step([dt.date.fromisoformat(p["date"]) for p in pts], [float(p["eci"]) for p in pts],
                where="post", color=color, label=label, marker="o", ms=3)
    ax.set_ylabel("Epoch Capabilities Index (GPT-5 = 150)")
    ax.set_title("General capability frontier, Epoch Capabilities Index")
    ax.legend(loc="upper left")
    ax.grid(alpha=0.3)
    fig.text(0.01, 0.01, f"Source: Epoch AI ({ECI_URL})", fontsize=7, color="#4a5568")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(FIG / "eci_frontier.png", dpi=150)
    plt.close(fig)
    top = sorted(rows, key=lambda r: -float(r["eci"]))
    top_open = [r for r in top if r["Accessibility group"] == "Open weights"]
    return top[:10], top_open[:3]


def epoch_benchmarks():
    """Top three results on each benchmark in BENCHES, from Epoch's benchmark data."""
    zf = zipfile.ZipFile(io.BytesIO(fetch(BENCH_URL, raw=True)))
    out = []
    for name, col, label in BENCHES:
        rows = [r for r in csv.DictReader(io.TextIOWrapper(zf.open(name), "utf-8")) if r.get(col)]
        rows.sort(key=lambda r: -float(r[col]))
        for r in rows[:3]:
            out.append({"benchmark": label, "model": r.get("Name") or r["Model version"],
                        "score": round(float(r[col]), 4), "release_date": r["Release date"],
                        "organization": r["Organization"], "epoch_file": name})
    write_csv(DATA / "epoch_top_results.csv", out)
    return out


def status_chart():
    """Draw figures/test_status.png from the hand-kept data/test_status.csv."""
    rows = list(csv.DictReader(open(DATA / "test_status.csv")))
    tests = ["T1", "T2", "T3", "T4", "T5"]
    names = {"T1": "T1 Breadth", "T2": "T2 Learning new things", "T3": "T3 Long tasks alone",
             "T4": "T4 Learning on the job", "T5": "T5 Reliable and affordable"}
    today = dt.date.today()
    fig, ax = plt.subplots(figsize=(8, 3.2))
    for i, t in enumerate(tests):
        events = sorted((dt.date.fromisoformat(r["date"]), r["status"]) for r in rows if r["test"] == t)
        for (start, status), nxt in zip(events, events[1:] + [(today, None)]):
            ax.barh(i, (nxt[0] - start).days, left=start, height=0.5, color=STATUS_COLORS[status])
    ax.set_yticks(range(len(tests)), [names[t] for t in tests])
    ax.invert_yaxis()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    first = min(dt.date.fromisoformat(r["date"]) for r in rows)
    ax.set_xlim(first - dt.timedelta(days=30), today + dt.timedelta(days=15))
    ax.legend(handles=[mpatches.Patch(color=c, label=s) for s, c in STATUS_COLORS.items()],
              loc="upper left", bbox_to_anchor=(1.01, 1), fontsize=8, frameon=False)
    ax.set_title("Status of the five tests over time")
    ax.grid(axis="x", alpha=0.3)
    fig.text(0.01, 0.01, "Source: data/test_status.csv, each change dated and sourced", fontsize=7, color="#4a5568")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(FIG / "test_status.png", dpi=150)
    plt.close(fig)


def write_csv(path, rows):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def main():
    DATA.mkdir(exist_ok=True)
    FIG.mkdir(exist_ok=True)
    metr_rows, doubling = metr()
    top, top_open = eci()
    bench = epoch_benchmarks()
    status_chart()
    snap = {
        "pulled_on": dt.date.today().isoformat(),
        "metr_best_p50": max(metr_rows, key=lambda r: r["p50_hours"]),
        "metr_doubling_days": doubling,
        "eci_top10": [{k: r[k] for k in ("Display name", "eci", "eci_ci_low", "eci_ci_high", "date", "Organization")} for r in top],
        "eci_top_open": [{k: r[k] for k in ("Display name", "eci", "date", "Organization")} for r in top_open],
        "epoch_best": {b["benchmark"]: b for b in reversed(bench)},
    }
    (DATA / "SNAPSHOT.json").write_text(json.dumps(snap, indent=2) + "\n")
    print(json.dumps(snap, indent=2))


if __name__ == "__main__":
    main()
