# 04 · Reasoning models and test-time compute

**Goal.** You can explain how "thinking" models are trained, why they help, and where they stop helping.

**Why it matters for AGI.** Reasoning models produced the 2024–26 jumps on maths, science and ARC (T1, T2).

## Core ideas

- **Chain of thought:** writing intermediate steps improves answers on multi-step problems.
- **Process versus outcome reward:** reward each correct step, or only the final answer.
- **Reinforcement learning with verifiable rewards (RLVR):** on maths and code, a program can check the answer, so reinforcement learning can run at huge scale without human labels. This is the core of o1-style and R1-style training.
- **Test-time compute scaling:** more thinking tokens, sampling many answers and voting, or search over answers. Each buys accuracy with compute.
- **Reasoning effort as a dial:** on ARC-AGI-3, GPT-6 Astra scored 17.5% at low effort and 62.7% at max effort (Sept 2026).
- **Limits:** the reward must be checkable; the written reasoning may be unfaithful; the cost rises.

## Read

1. ⭐ Wei et al. 2022, chain of thought ([2201.11903](https://arxiv.org/abs/2201.11903)).
2. ⭐ DeepSeek-AI 2025, R1 ([2501.12948](https://arxiv.org/abs/2501.12948)): the clearest public recipe.
3. Lightman et al. 2023, *Let's Verify Step by Step* ([2305.20050](https://arxiv.org/abs/2305.20050)).
4. Snell et al. 2024, test-time compute ([2408.03314](https://arxiv.org/abs/2408.03314)).
5. Zelikman et al. 2022, STaR ([2203.14465](https://arxiv.org/abs/2203.14465)): early self-taught reasoning.
6. [ARC Prize: GPT-6 Astra on ARC-AGI-3](https://arcprize.org/blog/astra): effort against score against cost.

## Do

Plot ARC-AGI-3 score against cost for the six GPT-6 Astra effort levels in the ARC Prize post (Standard harness). Is more effort always better? Is it always more expensive?

## Check yourself

1. Why does RLVR work for maths but struggle for essay writing?
2. What is the difference between a model being *right* and its chain of thought being *faithful*?
3. Which of the five AGI tests does test-time compute help most, and which does it hurt?
