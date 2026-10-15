# 07 · Memory and continual learning

**Goal.** You can explain why current models do not learn from deployment, the main research approaches, and why this may be the last wall.

**Why it matters for AGI.** T4 (learning on the job) is the test with the least progress. The AGI Score paper names long-term memory storage as the critical deficit.

## Core ideas

- **Kinds of memory in AI systems:**
  - *Weights*: slow, permanent; changed only by training.
  - *Context window*: fast, temporary; wiped each session.
  - *External memory*: notes, files and retrieval that a tool saves and reloads.
- **Catastrophic forgetting:** training on new data overwrites old skills.
- **Fixes in research:**
  - *Regularise* important weights (EWC).
  - *Replay* old data while training on new data.
  - *Test-time training*: update a small part of the model while working.
  - *Learned memory modules* (Titans).
  - *Agents that manage their own memory* (MemGPT).
- **Why labs are careful:** a model that changes after release is harder to evaluate and to keep safe.
- **The "era of experience" view (Sutton & Silver, 2025):** future agents should learn mainly from their own streams of experience, not from fixed human data.

## Read

1. ⭐ Kirkpatrick et al. 2017, EWC ([1612.00796](https://arxiv.org/abs/1612.00796)).
2. ⭐ Packer et al. 2023, MemGPT ([2310.08560](https://arxiv.org/abs/2310.08560)).
3. ⭐ Hendrycks et al. 2025 ([2510.18212](https://arxiv.org/abs/2510.18212)): the memory domains.
4. Sun et al. 2024, test-time training layers ([2407.04620](https://arxiv.org/abs/2407.04620)).
5. Behrouz et al. 2024, Titans ([2501.00663](https://arxiv.org/abs/2501.00663)).
6. Silver & Sutton 2025, *Welcome to the Era of Experience* (essay; search the title).

## Do

Design (on paper) the "first month at work" benchmark from [Ideas](../ideas.md) 3.1. What is the job? How do you measure improvement? How do you check that old skills are kept? What is the human baseline?

## Check yourself

1. Why is a 1M-token context window not the same as learning?
2. What is catastrophic forgetting, and which method addresses it by protecting important weights?
3. Give one safety reason why self-updating models are hard to deploy.
