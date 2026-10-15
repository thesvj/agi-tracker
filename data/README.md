# Data

Every file here is plain CSV or JSON. Files marked "script" are rewritten by `uv run src/update_data.py`, which a GitHub Action also runs every Monday. Files marked "by hand" are edited directly, and each row in them carries its own source.

| File | Kept | Contents |
|---|---|---|
| `benchmarks.csv` | by hand | The results cited on the tracker, one row per result |
| `test_status.csv` | by hand | Each change in a test's status, with its date and evidence. Draws `figures/test_status.png` |
| `metr_time_horizons.csv` | script | METR Time Horizon 1.1 results for every model METR has measured |
| `eci_scores.csv` | script | Epoch Capabilities Index scores for every model, as Epoch publishes them |
| `eci_frontier.csv` | script | The best closed and open-weights ECI score at each date |
| `epoch_top_results.csv` | script | The top three results on FrontierMath Tier 4 (v2), FrontierMath: Erdős, ARC-AGI-2 and Humanity's Last Exam |
| `SNAPSHOT.json` | script | The headline numbers from the last pull, with the date it ran |

## Columns

`benchmarks.csv`

| Column | Meaning |
|---|---|
| `benchmark` | Benchmark name and version |
| `agi_test` | Which of the five tests the result bears on (T1 to T5) |
| `model` | Model and setting, such as reasoning effort |
| `score` | The score as the source reports it |
| `setting` | Harness, split or other conditions that change the score |
| `result_date` | When the result was published (YYYY-MM-DD, or YYYY-MM when only the month is known) |
| `source_url` | Where the number comes from |
| `source_tier` | `primary` (benchmark owner or independent evaluator), `compiled` (republished in Epoch's benchmark data), `lab-reported` or `unverified` (aggregators and press) |
| `verified_on` | The date someone last checked the number against the source |
| `notes` | Anything a reader needs to interpret the number |

`test_status.csv`

| Column | Meaning |
|---|---|
| `date` | When the evidence was published |
| `test` | T1 to T5 |
| `status` | `Not met`, `Partly` or `Met` from that date on |
| `best_result` | The result that set the status |
| `source` | Where the result comes from |

`metr_time_horizons.csv`: `p50_hours` and `p80_hours` are the task lengths, in hours a human expert needs, at which the model succeeds 50% and 80% of the time. `is_sota` marks models that were the best when released.

`epoch_top_results.csv`: `score` runs from 0 to 1. `epoch_file` names the file inside Epoch's [benchmark data](https://epoch.ai/data/benchmark_data.zip).

## Sources and licences

METR results come from [benchmark_results_1_1.yaml](https://metr.org/assets/benchmark_results_1_1.yaml). Epoch AI data comes from [eci_scores.csv](https://epoch.ai/data/eci_scores.csv) and [benchmark_data.zip](https://epoch.ai/data/benchmark_data.zip) and is licensed CC BY 4.0 by Epoch AI. Please credit the original source when you reuse a number.
