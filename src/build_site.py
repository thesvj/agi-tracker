# /// script
# requires-python = ">=3.10"
# dependencies = ["markdown"]
# ///
"""Build the website in site/ from the markdown files in this repo.

Run:  uv run src/build_site.py
Then open site/index.html. The GitHub Action runs the same script and
publishes site/ to GitHub Pages. The markdown files stay the source; nothing
here is edited by hand except page.html and style.css.
"""
import html
import pathlib
import re
import shutil
import subprocess

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "site"
TEMPLATE = (ROOT / "src/site/page.html").read_text()
REPO = "https://github.com/thesvj/agi-tracker"
NAV = [("README.md", "Home"), ("tracker.md", "Tracker"), ("definition.md", "Definition"),
       ("survey.md", "Survey"), ("timeline.md", "Timeline"), ("papers.md", "Papers"),
       ("labs.md", "Labs"), ("learn/README.md", "Learn"), ("ideas.md", "Ideas"),
       ("CHANGELOG.md", "Changelog")]


def slug(text, sep="-"):
    """GitHub's heading anchors, so links written for GitHub work on the site too."""
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    return re.sub(r"[^\w\- ]", "", text).replace(" ", sep)


def page_path(md):
    """learn/README.md -> learn/index.html, tracker.md -> tracker.html."""
    rel = md.relative_to(ROOT)
    return rel.with_name("index.html") if rel.name == "README.md" else rel.with_suffix(".html")


def fix_link(target, src):
    """Point a link from a markdown file at the right place on the site."""
    if re.match(r"^[a-z]+:|^#", target):
        return target
    path, _, frag = target.partition("#")
    dest = (src.parent / path).resolve()
    frag = f"#{frag}" if frag else ""
    here = page_path(src).parent
    if dest.suffix == ".md" and dest.exists():
        return rel_url(page_path(dest), here) + frag
    if dest.is_dir() and (dest / "README.md").exists():
        return rel_url(page_path(dest / "README.md"), here) + frag
    if dest.is_relative_to(ROOT / "figures"):
        return rel_url(dest.relative_to(ROOT), here)
    kind = "tree" if dest.is_dir() else "blob"
    return f"{REPO}/{kind}/main/{dest.relative_to(ROOT).as_posix()}"


def rel_url(target, here):
    up = "../" * len(here.parts)
    return up + target.as_posix()


def last_changed(md):
    out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", str(md)],
                         cwd=ROOT, capture_output=True, text=True).stdout.strip()
    return out or "recently"


def render(md):
    text = md.read_text()
    conv = markdown.Markdown(extensions=["tables", "fenced_code", "toc"],
                             extension_configs={"toc": {"slugify": lambda v, s: slug(v, s)}})
    body = conv.convert(text)
    body = re.sub(r'(href|src)="([^"]+)"',
                  lambda m: f'{m[1]}="{html.escape(fix_link(html.unescape(m[2]), md))}"', body)
    body = body.replace("<table>", '<div class="table"><table>').replace("</table>", "</table></div>")
    title = re.search(r"^# (.+)$", text, re.M)[1]
    first_para = next((p for p in text.split("\n\n")[1:] if p and p[0].isalpha()), "")
    description = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", first_para).replace("\n", " ")[:300]
    here = page_path(md).parent
    root = "../" * len(here.parts)
    nav = " ".join(
        f'<a href="{rel_url(page_path(ROOT / f), here)}"'
        f'{" aria-current=page" if ROOT / f == md else ""}>{name}</a>' for f, name in NAV)
    page_title = "AGI Tracker" if md == ROOT / "README.md" else f"{title} · AGI Tracker"
    return TEMPLATE.format(title=html.escape(page_title), description=html.escape(description),
                           root=root, nav=nav, body=body, updated=last_changed(md), repo=REPO)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    sources = [ROOT / f for f, _ in NAV] + sorted((ROOT / "learn").glob("[0-9]*.md"))
    sources += [ROOT / "data/README.md"]
    for md in sources:
        dest = OUT / page_path(md)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render(md))
    shutil.copytree(ROOT / "figures", OUT / "figures")
    shutil.copy(ROOT / "src/site/style.css", OUT / "style.css")
    (OUT / ".nojekyll").write_text("")
    print(f"site/: {len(sources)} pages")


if __name__ == "__main__":
    main()
