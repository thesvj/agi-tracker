# Ideas

Open problems, grouped by the test they would move. Each entry says why the problem is open, what result would count as progress, and which existing work comes closest, so it can be taken up as a project.

## Breadth (T1)

### An AGI Score for current models

The CHC AGI Score has been published only for GPT-4 and GPT-5 (October 2025). Running it on 2026 models would show which of its 10 domains have improved and which haven't.

Progress would be domain-by-domain scores for three or more frontier models from 2026. The closest work is Hendrycks et al. 2025 ([2510.18212](https://arxiv.org/abs/2510.18212)).

### A human reference point on the capability index

Epoch's capability index shows the trend but has no point for a skilled human. If a professional baseline could be placed on its scale, the index could be used directly for T1.

Progress would be one or more benchmarks inside the index with clean professional baselines, used to locate the expert human on the scale. The closest work is Epoch's method for the index, and GDPval.

## Learning new things (T2)

### Does efficiency on ARC-AGI-3 carry over?

GPT-6 Astra learns ARC games in fewer actions than the median human. It's unknown whether that holds for unfamiliar software, such as a new API or codebase, or for a new game with noise in it.

Progress would be a study across models that correlates action efficiency on ARC-AGI-3 with how fast they learn real tools they haven't seen. The closest work is ARC-AGI-3 itself ([2603.24621](https://arxiv.org/abs/2603.24621)).

### Separating the harness from the model

The same model scores 62.7% or 99.9% depending on the harness. Which parts of the harness explain the gap: the persistent reasoning state, compaction, or the model writing its own tools?

Progress would be an ablation that removes one part of the harness at a time.

## Learning on the job (T4)

### A "first month at work" benchmark

Give an agent a new simulated job, such as a codebase with a stream of tickets or a lab notebook, and run it over many sessions. Score how much it improves on later tickets and whether it keeps its old skills. Compare agents that only keep notes with agents that are allowed to update their weights.

Progress would be a public benchmark with a human learning curve to compare against. The closest work is MemGPT ([2310.08560](https://arxiv.org/abs/2310.08560)), Titans ([2501.00663](https://arxiv.org/abs/2501.00663)), and the continual-learning literature ([1612.00796](https://arxiv.org/abs/1612.00796)).

### Notes or weights

How far can an agent get by writing good notes and rereading them, compared with actually updating its weights? Notes eventually grow too long, and weight updates cause forgetting, and it's not known which limit comes first.

Progress would be a curve of performance against the amount of stored experience, for both approaches.

### Auditing a model that updates itself

If a deployed model changes its own weights, it has to be checked again. One test would be whether safety behaviours survive continual fine-tuning on deployment data. The closest work is Sleeper Agents ([2401.05566](https://arxiv.org/abs/2401.05566)).

## Long tasks alone (T3)

### The trend in the 80% horizon

Most reports quote the 50% horizon. Fitting a separate trend for the 80% horizon, with its uncertainty, from METR's public data would show whether it doubles at the same rate.

Progress would be a short note with a plot. The data is already in [`data/metr_time_horizons.csv`](data/metr_time_horizons.csv).

### Why long runs fail

Long agent runs fail in different ways: the agent loses track of the goal, small errors compound, a tool breaks, or the agent cheats. Classifying failures would show which kinds shrink as models scale and which stay. The closest material is METR's reports and published SWE-agent trajectories.

## Reliable and affordable (T5)

### Cost-adjusted results

Plot ARC-AGI-3 and METR results as score per dollar, with the human cost as a reference line, to see when AI becomes cheaper than a person per solved task. Progress would be a chart updated monthly.

### Cheating rates in one place

Collect every published rate of reward hacking or cheating, from METR reports and lab system cards, into one dated table.

## Measurement

### How long benchmarks last

Measure the time each benchmark took to go from release to saturation, for MMLU, GPQA, SWE-bench Verified, Humanity's Last Exam, and ARC-AGI-1 and 2, and see whether the lifetimes are shrinking along a regular curve. A table and a plot would answer it cheaply.

### Benchmarks that can't leak

Benchmarks built from problems that nobody has solved, like FrontierMath: Erdős, can't leak into training data. It's an open question how far the approach extends beyond maths, for example to open bugs or unsolved engineering tasks.

## Questions worth returning to

- If T2 is solved for games but T4 isn't, would the result be an AGI that can't hold a job?
- Will measurable speed-ups in AI research, which METR began focusing on in October 2026, show up before T3 is passed or after?
- What would show that this definition is wrong? The [definition page](definition.md#how-the-definition-could-be-wrong) lists the arguments so far.
