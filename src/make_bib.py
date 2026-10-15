# /// script
# requires-python = ">=3.10"
# ///
"""Write references.bib: every arXiv paper cited in the repo, plus the
seminal papers in papers.md that are not on arXiv.

Run:  uv run src/make_bib.py
"""
import pathlib
import re
import sys
import time
import unicodedata
import urllib.request
import xml.etree.ElementTree as ET

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from check_refs import ATOM, ROOT, cited_ids  # noqa: E402

# Papers in papers.md that have no arXiv version.
OTHER = [
    ("article", "turing1950computing", {"author": "Turing, A. M.", "title": "Computing Machinery and Intelligence",
     "journal": "Mind", "volume": "LIX", "number": "236", "pages": "433--460", "year": "1950",
     "doi": "10.1093/mind/LIX.236.433"}),
    ("misc", "mccarthy1955proposal", {"author": "McCarthy, John and Minsky, Marvin L. and Rochester, Nathaniel and Shannon, Claude E.",
     "title": "A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence", "year": "1955",
     "url": "http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf"}),
    ("article", "rumelhart1986learning", {"author": "Rumelhart, David E. and Hinton, Geoffrey E. and Williams, Ronald J.",
     "title": "Learning representations by back-propagating errors", "journal": "Nature", "volume": "323",
     "pages": "533--536", "year": "1986", "doi": "10.1038/323533a0"}),
    ("inproceedings", "krizhevsky2012imagenet", {"author": "Krizhevsky, Alex and Sutskever, Ilya and Hinton, Geoffrey E.",
     "title": "ImageNet Classification with Deep Convolutional Neural Networks",
     "booktitle": "Advances in Neural Information Processing Systems", "volume": "25", "year": "2012",
     "url": "https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html"}),
    ("article", "silver2016mastering", {"author": "Silver, David and others",
     "title": "Mastering the game of Go with deep neural networks and tree search", "journal": "Nature",
     "volume": "529", "pages": "484--489", "year": "2016", "doi": "10.1038/nature16961"}),
    ("misc", "sutton2019bitter", {"author": "Sutton, Richard S.", "title": "The Bitter Lesson", "year": "2019",
     "url": "http://www.incompleteideas.net/IncIdeas/BitterLesson.html"}),
    ("article", "jumper2021highly", {"author": "Jumper, John and others",
     "title": "Highly accurate protein structure prediction with AlphaFold", "journal": "Nature",
     "volume": "596", "pages": "583--589", "year": "2021", "doi": "10.1038/s41586-021-03819-2"}),
    ("misc", "lecun2022path", {"author": "LeCun, Yann", "title": "A Path Towards Autonomous Machine Intelligence",
     "year": "2022", "url": "https://openreview.net/forum?id=BZ5a1r-kVsf"}),
    ("article", "romeraparedes2024mathematical", {"author": "Romera-Paredes, Bernardino and others",
     "title": "Mathematical discoveries from program search with large language models", "journal": "Nature",
     "volume": "625", "pages": "468--475", "year": "2024", "doi": "10.1038/s41586-023-06924-6"}),
]


def ascii_word(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z]", "", s.lower())


def arxiv_entries(ids):
    entries = []
    for i in range(0, len(ids), 100):
        url = "https://export.arxiv.org/api/query?max_results=100&id_list=" + ",".join(ids[i:i + 100])
        req = urllib.request.Request(url, headers={"User-Agent": "agi-tracker/1.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            root = ET.fromstring(r.read())
        for e in root.findall(f"{ATOM}entry"):
            ident = e.find(f"{ATOM}id").text.rsplit("/", 1)[-1].split("v")[0]
            title = " ".join(e.find(f"{ATOM}title").text.split())
            if title == "Error":
                continue
            authors = [" ".join(a.find(f"{ATOM}name").text.split()) for a in e.findall(f"{ATOM}author")]
            year = e.find(f"{ATOM}published").text[:4]
            first_word = next((w for w in map(ascii_word, title.split()) if len(w) > 3), "paper")
            key = f"{ascii_word(authors[0].split()[-1])}{year}{first_word}"
            entries.append(("misc", key, {
                "author": " and ".join(authors[:10]) + (" and others" if len(authors) > 10 else ""),
                "title": title, "year": year, "eprint": ident, "archivePrefix": "arXiv",
                "url": f"https://arxiv.org/abs/{ident}"}))
        time.sleep(3)
    return entries


def main():
    entries = arxiv_entries(sorted(cited_ids())) + OTHER
    seen, lines = set(), []
    for kind, key, fields in sorted(entries, key=lambda x: x[1]):
        while key in seen:
            key += "b"
        seen.add(key)
        body = ",\n".join(f"  {k} = {{{v}}}" for k, v in fields.items())
        lines.append(f"@{kind}{{{key},\n{body}\n}}\n")
    (ROOT / "references.bib").write_text("\n".join(lines))
    print(f"references.bib: {len(lines)} entries")


if __name__ == "__main__":
    main()
