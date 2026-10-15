# Agents and long tasks

By the end of this module you should be able to explain how agents work, how METR measures the time horizon, and why reliability falls as tasks get longer. T3 is the clearest gap between a capable chatbot and a colleague you can hand work to.

## Main ideas

An agent repeats a cycle: it thinks, calls a tool, looks at the result, and goes again. The code around the model that runs this loop is called the scaffold or harness. Typical tools are a shell, a browser, code execution, file editing and other agents.

To measure the time horizon, METR takes many tasks whose completion time for a human expert is known and fits the agent's success probability against the logarithm of task length. The 50% horizon is the task length at which the agent succeeds half the time.

Errors compound over long tasks. If each step succeeds 99% of the time, a 500-step task succeeds only about 0.7% of the time (0.99^500), so long tasks need an agent that can notice and recover from its mistakes.

Agents also cheat. They have been seen editing tests, hard-coding outputs and reading hidden answers, and METR found cheating in at least 16% of successful runs on tasks over 8 hours (2026).

## Reading

Start with these:

1. Kwa et al. 2025, *Measuring AI Ability to Complete Long Software Tasks* ([2503.14499](https://arxiv.org/abs/2503.14499)).
2. Yao et al. 2022, ReAct ([2210.03629](https://arxiv.org/abs/2210.03629)).

Further reading:

3. Jimenez et al. 2023, SWE-bench ([2310.06770](https://arxiv.org/abs/2310.06770)), and Yang et al. 2024, SWE-agent ([2405.15793](https://arxiv.org/abs/2405.15793)).
4. Xie et al. 2024, OSWorld ([2404.07972](https://arxiv.org/abs/2404.07972)).
5. [METR Frontier Risk Report, May 2026](https://metr.org/blog/2026-05-19-frontier-risk-report/).

## Exercise

Using [`data/metr_time_horizons.csv`](../data/metr_time_horizons.csv), fit log2 of `p80_hours` against release date for the rows where `is_sota` is true. What doubling time does the 80% horizon have, and how does it compare with the 129 days METR reports for the 50% horizon? This is one of the open problems on the [Ideas](../ideas.md) page.

## Questions

1. Why is the 80% horizon about five times shorter than the 50% horizon?
2. Why does METR consider its numbers above 16 hours unreliable?
3. Name two ways an agent's long-horizon score could come out too high.
