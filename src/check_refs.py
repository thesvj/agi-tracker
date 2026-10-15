# /// script
# requires-python = ">=3.10"
# ///
"""Check every arXiv ID cited in the repo against the arXiv API.

Run:  uv run src/check_refs.py
Prints "ID  <real title>" for every ID, so a wrong ID shows a wrong title.
Exits 1 if any ID does not exist.
"""
import pathlib
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})|\barXiv:(\d{4}\.\d{4,5})|\((\d{4}\.\d{4,5})\)")
ATOM = "{http://www.w3.org/2005/Atom}"


def cited_ids():
    ids = {}
    for path in sorted((ROOT / "docs").rglob("*.md")):
        for m in ID_RE.finditer(path.read_text()):
            ident = next(g for g in m.groups() if g)
            ids.setdefault(ident, set()).add(str(path.relative_to(ROOT)))
    return ids


def titles(id_list):
    url = "https://export.arxiv.org/api/query?max_results=100&id_list=" + ",".join(id_list)
    req = urllib.request.Request(url, headers={"User-Agent": "agi-tracker/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        root = ET.fromstring(r.read())
    out = {}
    for e in root.findall(f"{ATOM}entry"):
        ident = e.find(f"{ATOM}id").text.rsplit("/", 1)[-1].split("v")[0]
        title = " ".join(e.find(f"{ATOM}title").text.split())
        if title != "Error":
            out[ident] = title
    return out


def main():
    ids = cited_ids()
    keys = sorted(ids)
    found = {}
    for i in range(0, len(keys), 50):
        found.update(titles(keys[i:i + 50]))
        time.sleep(3)
    bad = 0
    for k in keys:
        t = found.get(k)
        if t is None:
            bad += 1
            print(f"MISSING  {k}  (in {', '.join(sorted(ids[k]))})")
        else:
            print(f"{k}  {t}")
    print(f"\n{len(keys)} IDs, {bad} missing")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
