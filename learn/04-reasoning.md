# Reasoning models and test-time compute

By the end of this module you should be able to explain how reasoning models are trained, why they help, and where they stop helping. They account for most of the gains in maths, science and ARC from 2024 to 2026, which bear on T1 and T2.

## Main ideas

Writing out intermediate steps, a chain of thought, improves answers on problems that take several steps. Training can reward each correct step (process reward) or only the final answer (outcome reward).

On maths and code, a program can check whether an answer is right. That allows reinforcement learning at very large scale without human labels, and this reinforcement learning with verifiable rewards is the core of how o1 and R1 were trained.

Spending more compute at answer time also helps: more thinking tokens, sampling many answers and voting, or searching over candidate answers. Each trades compute for accuracy. ARC Prize measured GPT-6 Astra on ARC-AGI-3 at 17.5% with low reasoning effort and 62.7% with maximum effort (September 2026).

There are limits. The reward has to be checkable, the written reasoning may not reflect what actually produced the answer, and the cost rises with every extra token.

## Reading

Start with these:

1. Wei et al. 2022, chain of thought ([2201.11903](https://arxiv.org/abs/2201.11903)).
2. DeepSeek-AI 2025, R1 ([2501.12948](https://arxiv.org/abs/2501.12948)), the clearest public description of the method.

Further reading:

3. Lightman et al. 2023, *Let's Verify Step by Step* ([2305.20050](https://arxiv.org/abs/2305.20050)).
4. Snell et al. 2024, test-time compute ([2408.03314](https://arxiv.org/abs/2408.03314)).
5. Zelikman et al. 2022, STaR ([2203.14465](https://arxiv.org/abs/2203.14465)), an early method for self-taught reasoning.
6. [ARC Prize on GPT-6 Astra](https://arcprize.org/blog/astra), which reports score and cost at each effort level.

## Exercise

Using the ARC Prize post, plot ARC-AGI-3 score against cost for GPT-6 Astra's six effort levels with the Standard harness. Is more effort always better, and is it always more expensive?

## Questions

1. Why does reinforcement learning with verifiable rewards work for maths but struggle with essay writing?
2. What is the difference between a model being right and its chain of thought being faithful?
3. Which of the five tests does extra test-time compute help most, and which does it hurt?
