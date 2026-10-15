# AGI Tracker

**How close are we to artificial general intelligence?** A precise definition, five measurable tests, and dated evidence from primary sources.

**Read it here: https://thesvj.github.io/agi-tracker/**

> **AGI is an AI system that can learn and do nearly all the cognitive work that skilled humans do, including work it was never trained for. It does this on its own, as reliably as those humans, and at no greater cost.**

| Test | Status (Oct 2026) |
|---|---|
| T1 Breadth | 🟡 Partly |
| T2 Learning new things | 🟡 Partly, moving fast |
| T3 Long tasks alone | 🔴 Not met |
| T4 Learning on the job | 🔴 Not met |
| T5 Reliable and affordable | 🔴 Not met |

## Contents

| Page | |
|---|---|
| [What is AGI?](docs/definition.md) | Definition, five tests, nine definitions compared |
| [Tracker](docs/tracker.md) | Status of each test with sourced numbers |
| [Survey](docs/survey.md) | The field in 12 areas |
| [Timeline](docs/timeline.md) | Milestones, 1950 to today |
| [Learn](docs/learn/index.md) | 12-module study path |
| [Ideas](docs/ideas.md) | Open problems |

## Layout

```
docs/   the site's pages and figures
data/   raw data (METR time horizons, Epoch Capabilities Index, curated benchmark table)
src/    code: update_data.py rebuilds data + figures; check_refs.py verifies every arXiv ID
```

```bash
uv run src/update_data.py
uv run src/check_refs.py
```

Text CC BY 4.0, code MIT. See [LICENSE](LICENSE) and [CITATION.cff](CITATION.cff). Corrections with a primary source are welcome as [issues](https://github.com/thesvj/agi-tracker/issues).
