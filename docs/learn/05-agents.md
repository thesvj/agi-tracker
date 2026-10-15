# 05 · Agents and long tasks

**Goal.** You can explain how agents work, how METR's time horizon is measured, and why reliability falls as tasks get longer.

**Why it matters for AGI.** T3 (long tasks alone) is the clearest gap between "smart chatbot" and "colleague".

## Core ideas

- **The agent loop:** think → act (call a tool) → observe → repeat. The *scaffold* (or *harness*) is the code around the model that runs this loop.
- **Tools:** shell, browser, code execution, file editing, other agents.
- **Time horizon (METR):** take many tasks with known human completion times. Fit success probability against log task length. The 50% horizon is the length at which the agent succeeds half the time.
- **Compounding error:** if each step succeeds 99% of the time, a 500-step task succeeds about 0.7% of the time (0.99^500). Long tasks need recovery from errors, not just accuracy.
- **Cheating:** agents may edit tests, hard-code outputs or read hidden answers. METR found this in ≥ 16% of successful runs over 8 h (2026).

## Read

1. ⭐ Kwa et al. 2025, *Measuring AI Ability to Complete Long Software Tasks* ([2503.14499](https://arxiv.org/abs/2503.14499)).
2. ⭐ Yao et al. 2022, ReAct ([2210.03629](https://arxiv.org/abs/2210.03629)).
3. Jimenez et al. 2023, SWE-bench ([2310.06770](https://arxiv.org/abs/2310.06770)), and Yang et al. 2024, SWE-agent ([2405.15793](https://arxiv.org/abs/2405.15793)).
4. Xie et al. 2024, OSWorld ([2404.07972](https://arxiv.org/abs/2404.07972)).
5. [METR Frontier Risk Report, May 2026](https://metr.org/blog/2026-05-19-frontier-risk-report/).

## Do

Use [`data/metr_time_horizons.csv`](https://github.com/thesvj/agi-tracker/blob/main/data/metr_time_horizons.csv). Fit log2(p80_hours) against release date for the `is_sota` rows only. What doubling time do you get for the 80% horizon? Compare it with the 129-day doubling METR reports for the 50% horizon. (This is [Ideas](../ideas.md) 4.1.)

## Check yourself

1. Why is the 80% horizon about 5× shorter than the 50% horizon?
2. Why does METR say its numbers above 16 h are unreliable?
3. Name two ways an agent's long-horizon score could be *too high*.
