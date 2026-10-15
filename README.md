# AGI Tracker

A collection of surveys and notes that tracks how far AI systems are from artificial general intelligence. Everything is measured against one fixed definition and five tests, and every result is dated and taken from a primary source where one exists. You can read it here on GitHub or as a website at [thesvj.github.io/agi-tracker](https://thesvj.github.io/agi-tracker/).

> AGI is an AI system that can learn and do nearly all the cognitive work that skilled humans do, including work it was never trained for. It does this on its own, as reliably as those humans, and at no greater cost.

| Test | Status in October 2026 |
|---|---|
| T1 Breadth | Partly |
| T2 Learning new things | Partly, and improving quickly |
| T3 Long tasks alone | Not met (3.1 hours against a 167-hour target) |
| T4 Learning on the job | Not met |
| T5 Reliable and affordable | Not met |

## Contents

| File | Contents |
|---|---|
| [definition.md](definition.md) | The definition, the pass line for each test, and nine definitions compared |
| [tracker.md](tracker.md) | The current status of each test, with sources and dates |
| [survey.md](survey.md) | The state of research in twelve areas, from scaling and reasoning to memory, robotics and safety |
| [timeline.md](timeline.md) | Milestones from 1950 to now |
| [learn/](learn/README.md) | A twelve-module study path with readings, exercises and questions |
| [ideas.md](ideas.md) | Open problems, each with a note on what would count as progress |
| [papers.md](papers.md) | Seminal papers for anyone starting work in the field |
| [labs.md](labs.md) | Labs and organisations working on general AI, and where to follow them |
| [CHANGELOG.md](CHANGELOG.md) | What changed and when, newest first |
| [data/](data/README.md) | The numbers behind the tracker, with every column explained |

## Two charts

METR's time horizon: the length of task, in the time a human expert would need, that AI agents finish half the time. It has doubled about every 129 days since 2023.

![METR time horizon](figures/metr_time_horizon.png)

The best closed and open models on Epoch AI's capability index. Open models trail by about 9 points, roughly half a year.

![Epoch Capabilities Index](figures/eci_frontier.png)

## Data and code

`data/` holds METR's time-horizon results, Epoch's capability index and benchmark results, a curated table of results with sources, and the history of each test's status. [data/README.md](data/README.md) explains every file.

The scripts in `src/` do four jobs. `update_data.py` downloads the latest METR and Epoch data and redraws the charts. `check_refs.py` checks every cited arXiv ID against arXiv. `make_bib.py` writes [references.bib](references.bib), which holds every work cited in the repo. `build_site.py` turns these markdown files into the website.

```bash
uv run src/update_data.py
uv run src/check_refs.py
uv run src/make_bib.py
uv run src/build_site.py
```

A GitHub Action runs the data update every Monday, commits any new numbers, and rebuilds the website. It also rebuilds the website on every push.

The text is licensed CC BY 4.0 and the code MIT; see [LICENSE](LICENSE) and [CITATION.cff](CITATION.cff). If you find an error, please open an [issue](https://github.com/thesvj/agi-tracker/issues) with a primary source.
