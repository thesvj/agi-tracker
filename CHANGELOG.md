# Changelog

What changed in the tracker and when, newest first. Each entry lists changed results with their source, and any change to the definition or a pass line. The weekly data refresh is not listed here unless it changes a status or a headline number.

To get a notice for every change, click Watch on the [GitHub page](https://github.com/thesvj/agi-tracker) and choose All activity.

## 2026-10-16

Results:

- FrontierMath Tier 4 (v2) is now saturated. GPT-6.1 Sol solved all of its problems in Epoch's evaluation (September 2026), and GPT-6 Astra scored 97.6%. This replaces the unverified 83% figure for GPT-5.6 Sol. Source: [Epoch benchmark data](https://epoch.ai/data/benchmark_data.zip).
- Humanity's Last Exam: GPT-6 Astra scores 54.8%. This replaces the unverified 46.4% figure. Source: Epoch benchmark data.
- ARC-AGI-2: GPT-6 Astra (max effort) scores 95.0%. The number is unchanged, but it now comes from Epoch's data instead of an aggregator site.
- No test changed status.

Repo:

- Added [papers.md](papers.md), a list of seminal papers, and [labs.md](labs.md), the labs and organisations working on general AI.
- Added [`data/test_status.csv`](data/test_status.csv) and a chart of how each test's status has changed.
- Added [`data/README.md`](data/README.md), which explains every data file and column.
- Added [references.bib](references.bib), every work cited in the repo in BibTeX.
- The tracker now has a fourth source label, compiled, for results republished in Epoch's benchmark data.
- Added a website at [thesvj.github.io/agi-tracker](https://thesvj.github.io/agi-tracker/), built from these same files.
- Data now refreshes every week through a GitHub Action.

## 2026-10-15

First release.

- The definition and the five tests, each with a fixed pass line, were set for the first time.
- Status: T1 and T2 partly met, T3, T4 and T5 not met.
- Claude Opus 5.5 (166.8), GPT-6 Astra (166.4) and GPT-6.1 Sol (166.3) were statistically tied at the top of the Epoch Capabilities Index. The best open-weights model was Kimi K3 (157.4).
- T2: GPT-6 Astra scored 62.7% on ARC-AGI-3 with the Standard harness and 99.9% with the Provider Adapter harness (ARC Prize, 3 September 2026). Frontier models were below 1% at the March launch.
- T3: the best public METR result was Claude Mythos Preview (early), with 17.4 hours at 50% success and 3.1 hours at 80%.
- T5: METR found cheating in at least 16% of successful runs on tasks over 8 hours.
