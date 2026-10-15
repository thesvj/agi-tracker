# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml", "matplotlib"]
# ///
"""Pull primary-source data and redraw the figures.

Run:  uv run src/update_data.py

Sources (primary only):
  METR Time Horizon 1.1  https://metr.org/assets/benchmark_results_1_1.yaml
  Epoch Capabilities Index https://epoch.ai/data/eci_scores.csv

Writes data/metr_time_horizons.csv, data/eci_scores.csv, data/eci_frontier.csv,
docs/figures/metr_time_horizon.png, docs/figures/eci_frontier.png, and data/SNAPSHOT.json.
"""
import csv
import datetime as dt
import io
import json
import pathlib
import urllib.request

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA, FIG = ROOT / "data", ROOT / "docs" / "figures"
METR_URL = "https://metr.org/assets/benchmark_results_1_1.yaml"
ECI_URL = "https://epoch.ai/data/eci_scores.csv"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "agi-tracker/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode()


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
    snap = {
        "pulled_on": dt.date.today().isoformat(),
        "metr_best_p50": max(metr_rows, key=lambda r: r["p50_hours"]),
        "metr_doubling_days": doubling,
        "eci_top10": [{k: r[k] for k in ("Display name", "eci", "eci_ci_low", "eci_ci_high", "date", "Organization")} for r in top],
        "eci_top_open": [{k: r[k] for k in ("Display name", "eci", "date", "Organization")} for r in top_open],
    }
    (DATA / "SNAPSHOT.json").write_text(json.dumps(snap, indent=2) + "\n")
    print(json.dumps(snap, indent=2))


if __name__ == "__main__":
    main()
