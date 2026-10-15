# Ideas and open problems

A working list of open problems, grouped by the AGI test they would move. Each idea says **why it is open**, **what would count as progress**, and **the nearest existing work**, so it can be picked up as a project.

Status tags: 💡 idea · 🔎 being read · 🧪 being tried · ✅ done or answered elsewhere.

---

## 1. Breadth (T1)

**1.1 💡 A current-generation AGI Score.** The CHC AGI Score exists only for GPT-4 and GPT-5 (Oct 2025). Re-running it on 2026 models would show which of the 10 domains moved and which did not.
*Progress:* domain-by-domain scores for 3 or more 2026 frontier models. *Nearest:* Hendrycks et al. 2025 ([2510.18212](https://arxiv.org/abs/2510.18212)).

**1.2 💡 A human anchor for ECI.** ECI tracks the trend but has no "skilled human" point. Mapping a human-professional baseline onto the ECI scale would turn it into a T1 test.
*Progress:* one or more benchmarks inside ECI with clean professional baselines, used to place "expert human" on the scale. *Nearest:* the Epoch ECI method; GDPval.

## 2. Learning new things (T2)

**2.1 💡 Does ARC-AGI-3 efficiency transfer?** GPT-6 Astra learns ARC games with fewer actions than the median human. Does that hold for unfamiliar *software* (a new API, a new codebase) or a new *game with noise*?
*Progress:* a correlation study across models between ARC-AGI-3 action efficiency and learning speed on real new tools. *Nearest:* ARC-AGI-3 ([2603.24621](https://arxiv.org/abs/2603.24621)).

**2.2 💡 Separate the harness from the model.** The same model scores 62.7% or 99.9% depending on the harness. Which harness parts (persistent reasoning state, compaction, tool-writing) explain the gap?
*Progress:* an ablation that removes one harness part at a time.

## 3. Learning on the job (T4)

**3.1 💡 A "first month at work" benchmark.** Give an agent a new simulated job (a codebase plus a ticket stream, or a lab notebook), run it for many sessions, and score (a) its improvement on later tickets and (b) whether its old skills are kept. Compare memory-only agents with agents allowed to update their weights.
*Progress:* a public benchmark with a human baseline curve. *Nearest:* MemGPT ([2310.08560](https://arxiv.org/abs/2310.08560)), Titans ([2501.00663](https://arxiv.org/abs/2501.00663)), continual-learning literature ([1612.00796](https://arxiv.org/abs/1612.00796)).

**3.2 💡 Notes versus weights.** How far can "write good notes and reread them" go compared with real weight updates? Where does each break: notes that are too long, or forgetting?
*Progress:* a scaling curve of performance against the size of the experience store, for both approaches.

**3.3 💡 Safe self-updating.** If a deployed model updates itself, how do we audit it? An eval that tests whether safety behaviours survive continual fine-tuning on deployment data.
*Nearest:* Sleeper Agents ([2401.05566](https://arxiv.org/abs/2401.05566)).

## 4. Long tasks alone (T3)

**4.1 💡 The 80% horizon trend.** Everyone quotes the 50% horizon. Fit the trend for the 80% horizon separately, with uncertainty, from METR's public YAML. Is its doubling time the same?
*Progress:* a short note with a plot. The data is already in [`data/metr_time_horizons.csv`](https://github.com/thesvj/agi-tracker/blob/main/data/metr_time_horizons.csv), so this could be done this week.

**4.2 💡 Where do long runs fail?** Classify failures in long agent runs: lost goal, compounding error, tool failure, cheating. Which ones shrink with scale and which do not?
*Nearest:* METR reports; SWE-agent trajectories.

## 5. Reliable and affordable (T5)

**5.1 💡 Cost-adjusted leaderboards.** Re-plot ARC-AGI-3 and METR results as *score per dollar* against the human cost line. When does AI become cheaper than the human per solved task?
*Progress:* a cost-adjusted chart, updated monthly.

**5.2 💡 A cheating-rate tracker.** Collect every published rate of reward hacking or cheating (METR, lab system cards) into one dated table.

## 6. Measurement

**6.1 💡 Benchmark half-life.** Measure how long benchmarks last from release to saturation (MMLU, GPQA, SWE-bench Verified, HLE, ARC-AGI-1/2). Is the lifetime shrinking on a fixed curve?
*Progress:* a table and a plot. This is cheap and useful.

**6.2 💡 Contamination-proof by construction.** Benchmarks built from problems with *no known answer* (like FrontierMath: Erdős) cannot leak. How far can that idea go beyond maths, e.g. open bugs or unsolved engineering tasks?

## 7. Questions to keep asking

- If T2 is solved on games but T4 is not, is the result "AGI that cannot hold a job"?
- Does real-world AI-R&D speed-up (METR's Oct 2026 focus) show up before or after T3 passes?
- What would make *this* definition wrong? Record each argument in [definition.md §4](definition.md#how-this-definition-could-be-wrong).

---

*Add ideas freely. Keep the format: why open → what counts as progress → nearest work.*
