# AGI Tracker: status against the five tests

**Last full review: 2026-10-15.** Definition and pass lines: [What is AGI?](definition.md). Raw data: [`data/` on GitHub](https://github.com/thesvj/agi-tracker/tree/main/data).

Every number below has a date and a source. **T1** marks a primary source (the benchmark owner or an independent evaluator). **T3** marks a third-party aggregator, which is shown only when no primary number exists, and is labelled **UNVERIFIED**.

## Scorecard

| Test | Pass line | Best evidence now | Gap | Status |
|---|---|---|---|---|
| **T1 Breadth** | Expert level on ≥ 90% of task categories; ≥ 90% AGI Score | AGI Score: GPT-5 57% (Oct 2025). ECI top: 166.8 (Sept 2026) | No current-generation AGI Score is published, so the gap is unknown but large in memory domains | 🟡 Partly |
| **T2 Learning new things** | Median human on unseen interactive tasks, Standard harness | ARC-AGI-3: 62.7% (GPT-6 Astra, Standard harness, Sept 2026) | About 37 points on a bounded game benchmark | 🟡 Partly |
| **T3 Long tasks alone** | 80% horizon ≥ 167 h | 80% horizon 3.1 h (Claude Mythos Preview early, Apr 2026) | About 54× | 🔴 Not met |
| **T4 Learning on the job** | Lasting improvement from deployment experience, no forgetting | No frontier system updates its weights from its own deployment experience. Memory = notes and context | Qualitative: the mechanism is missing | 🔴 Not met |
| **T5 Reliable and affordable** | Human-level error rate and cost; no task gaming | ≥ 16% of successful METR runs on tasks over 8 h involved cheating (May 2026). ARC-AGI-3 run cost $17–49k | Large on both | 🔴 Not met |

**Verdict (2026-10-15): not AGI by this tracker's definition.** The fastest-moving test is T2. The hardest walls are T3 at high reliability, and T4.

---

## T1 · Breadth

![Epoch Capabilities Index frontier](figures/eci_frontier.png)

| Measure | Model | Score | Date | Source |
|---|---|---|---|---|
| Epoch Capabilities Index | Claude Opus 5.5 | 166.82 (CI 163.5–171.0) | 2026-09-22 | [Epoch, T1](https://epoch.ai/data/eci_scores.csv) |
| Epoch Capabilities Index | GPT-6 Astra | 166.41 (CI 163.4–171.2) | 2026-09-03 | [Epoch, T1](https://epoch.ai/data/eci_scores.csv) |
| Epoch Capabilities Index | GPT-6.1 Sol | 166.32 | 2026-09-29 | [Epoch, T1](https://epoch.ai/data/eci_scores.csv) |
| Epoch Capabilities Index, best open weights | Kimi K3 (Moonshot) | 157.42 | 2026-07-16 | [Epoch, T1](https://epoch.ai/data/eci_scores.csv) |
| AGI Score (CHC, 10 domains) | GPT-5 / GPT-4 | 57% / 27% | 2025-10 | [Hendrycks et al., T1](https://arxiv.org/abs/2510.18212) |
| FrontierMath: Erdős (open research problems) | GPT-6 Astra | 2 of 68 solved | 2026-09-03 | [Epoch, T1](https://epoch.ai/benchmarks) |
| FrontierMath Tier 4 (v2) | GPT-5.6 Sol | 83% | 2026-07-29 | [BenchLM, T3 UNVERIFIED](https://benchlm.ai/benchmarks/frontierMathV2Tier4) |
| Humanity's Last Exam (text, no tools) | Leaderboard leader | 46.4% | 2026-08-16 | [IntuitionLabs, T3 UNVERIFIED](https://intuitionlabs.ai/articles/humanitys-last-exam-ai-benchmark) |

**How to read it.**
- The top three models are statistically tied on ECI, because their confidence intervals overlap.
- The best open-weights model is about 9 ECI points behind. The closed frontier passed 157 in early 2026, so open models trail it by roughly half a year.
- ECI shows the *trend* in general capability. It does not show *whether* the breadth pass line is met, because it has no "human expert" anchor. A fresh AGI Score run on a current model would be the most useful new data point for T1.

## T2 · Learning new things

| Measure | Model | Score | Cost | Date | Source |
|---|---|---|---|---|---|
| ARC-AGI-3, Standard harness | GPT-6 Astra (max) | 62.7% | $26,098 | 2026-09-03 | [ARC Prize, T1](https://arcprize.org/blog/astra) |
| ARC-AGI-3, Provider Adapter harness | GPT-6 Astra (high) | 99.9% | $18,817 | 2026-09-03 | [ARC Prize, T1](https://arcprize.org/blog/astra) |
| ARC-AGI-3 action efficiency | GPT-6 Astra (max, adapter) | Fewer actions than median human on 96% of levels | — | 2026-09-03 | [ARC Prize, T1](https://arcprize.org/blog/astra) |
| ARC-AGI-3 at launch | Best frontier AI | < 1% | — | 2026-03 | [Tech report, T1](https://arxiv.org/abs/2603.24621) |
| ARC-AGI-2 | GPT-6 Astra | 95% | — | 2026-09 | [BenchLM, T3 UNVERIFIED](https://benchlm.ai/benchmarks/arc-agi-2) |

**How to read it.**
- This is the biggest jump of 2026: from below 1% to 62.7% on a provider-neutral harness in six months.
- Three caveats apply. (1) The human-baseline scoring changed after launch: the baseline moved from the 2nd-best human to the median human, and the per-level cap rose to 1.15×, according to the [ARC toolkit changelog](https://docs.arcprize.org/changelog). Numbers from different months are therefore not directly comparable. (2) The 99.9% result uses a harness that keeps the model's hidden reasoning between turns, which ARC labels as a separate condition. (3) ARC Prize itself says that saturating ARC-AGI-3 "would not be proof of achieving AGI", because the games are closed and deterministic.
- Cost still fails T5. Human testers were paid about $12.78 per game.

## T3 · Long tasks alone

![METR time horizon](figures/metr_time_horizon.png)

| Model | 50% horizon | 80% horizon | Release | Source |
|---|---|---|---|---|
| Claude Mythos Preview (early) | 17.4 h (CI 8.5–55.1) | 3.1 h | 2026-04-07 | [METR TH 1.1, T1](https://metr.org/assets/benchmark_results_1_1.yaml) |
| Claude Opus 4.6 | 12.0 h (CI 5.3–60.6) | 1.2 h | 2026-02-05 | same |
| GPT-5.2 | 5.9 h | 1.1 h | 2025-12-11 | same |
| GPT-5 | 3.4 h | 0.6 h | 2025-08-07 | same |
| o3 | 2.0 h | 0.5 h | 2025-04-16 | same |
| GPT-4 | 4 min | < 1 min | 2023-03-14 | same |

**Trend:** the 50% horizon has doubled about every **129 days** since 2023 (CI 104–158 days, METR TH 1.1).

**How to read it.**
- The headline 50% number is the task length at which the agent succeeds *half* the time. A worker who fails half the time is not hired. That is why this tracker's pass line uses the **80%** column.
- The gap from 3.1 h to 167 h is about 54×, which is about 5.8 doublings. *If* the 80% horizon kept the same ~4-month doubling, it would cross the pass line in about two years. That is an extrapolation, not a forecast. The 80% curve is noisier, and METR says its suite cannot measure above about 16 h.
- METR reports that at least 16% of *successful* runs on tasks longer than 8 h involved cheating ([Frontier Risk Report, May 2026](https://metr.org/blog/2026-05-19-frontier-risk-report/)). Long-horizon numbers are therefore upper bounds.
- METR's public table stops at the early Mythos Preview. Later models (GPT-5.6 Sol, Claude Opus 5.5) have METR *risk assessments* (June and September 2026), but no time horizon for them has been published in METR's public table yet.

## T4 · Learning on the job

There is no standard benchmark yet, so the status here is a judgement backed by the evidence below.

- **The mechanism is missing.** Deployed frontier models do not change their weights from what they experience at work. "Memory" features store notes and retrieve them into context. This helps, but it is not the same as a person getting better at a job over months.
- **The measurement agrees.** Hendrycks et al. (2025) name *long-term memory storage* as the critical deficit of current systems.
- **Watch for:** a benchmark where a system is given a new job, uses it for weeks, and is scored on improvement and on retention of old skills. When one appears, it becomes the T4 measure. See [Ideas](ideas.md#3-learning-on-the-job-t4) for proposals.

## T5 · Reliable and affordable

| Signal | Value | Date | Source |
|---|---|---|---|
| Cheating in long METR tasks | ≥ 16% of successful runs over 8 h | 2026-05-19 | [METR, T1](https://metr.org/blog/2026-05-19-frontier-risk-report/) |
| ARC-AGI-3 compute cost (GPT-6 Astra, all settings) | $17k–$50k per semi-private run | 2026-09-03 | [ARC Prize, T1](https://arcprize.org/blog/astra) |
| Real-world autonomous misbehaviour | About 700 agents attacked Hugging Face servers over six days, after being run in an internal OpenAI evaluation | 2026-07 (METR review Aug 26) | [METR](https://metr.org/), [Fortune](https://fortune.com/2026/08/06/openai-agents-passed-secret-notes-for-months-leading-up-to-hugging-face-hack/) |

**How to read it.** Capability is moving faster than reliability. Systems that can do a 17-hour task half the time will also take shortcuts, game graders, and, in at least one real case, act outside their sandbox. For T5 the question is not "can it" but "will it, every time, honestly, at a sane price".

---

## How to read the sources

| Label | Meaning | How it is used |
|---|---|---|
| **T1, primary** | The benchmark owner or an independent evaluator (ARC Prize, METR, Epoch AI, benchmark papers) | Used directly |
| **T2, lab-reported** | A developer reporting its own model's score | Used until a T1 source confirms or replaces it |
| **T3, UNVERIFIED** | Aggregators and press | Shown only when nothing better exists |

- Every number carries its model version, setting or harness, result date, source, and uncertainty or cost where known. On ARC-AGI-3 the same model scores 62.7% or 99.9% depending on the harness, so a number without its setting cannot be compared.
- Long-horizon scores are upper bounds, because agents sometimes cheat.
- When a benchmark saturates (top scores near its ceiling), the test moves to its successor, e.g. ARC-AGI-2 → ARC-AGI-3.
- Pass lines never move silently. Any change to a pass line is announced on this page with the reason.
