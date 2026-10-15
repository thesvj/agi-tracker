# Post-training: RLHF, Constitutional AI, DPO

By the end of this module you should be able to explain how a raw next-token predictor becomes a helpful assistant, and what can go wrong along the way. Post-training shapes honesty, helpfulness, refusals and, more and more, reasoning. It is also where alignment problems such as reward hacking first show up, which matters for T5.

## Main ideas

Supervised fine-tuning trains the model on example conversations written by people.

In RLHF, people compare pairs of answers. A reward model learns to predict their preferences, and reinforcement learning (PPO, for example) then pushes the model toward answers the reward model scores highly. Constitutional AI, also called RLAIF, has an AI critique answers against a set of written principles, which replaces much of the human labelling. DPO drops the separate reward model and trains directly on the preference pairs, which is simpler and more stable.

Reward hacking is when the model finds ways to score highly without doing what was intended, for example by flattering the user or gaming tests. Sycophancy, telling users what they want to hear, is a common side effect of training on human preferences.

## Reading

Start with these:

1. Ouyang et al. 2022, InstructGPT ([2203.02155](https://arxiv.org/abs/2203.02155)).
2. Bai et al. 2022, Constitutional AI ([2212.08073](https://arxiv.org/abs/2212.08073)).

Further reading:

3. Rafailov et al. 2023, DPO ([2305.18290](https://arxiv.org/abs/2305.18290)).
4. Casper et al. 2023, *Open Problems and Fundamental Limitations of RLHF* ([2307.15217](https://arxiv.org/abs/2307.15217)).

## Exercise

Give a model one of its own wrong answers to grade, and insist that the answer is right. Note whether it gives in. Then repeat with a system prompt that asks it to be honest, and compare.

## Questions

1. Why train a reward model instead of having people score every output?
2. Which T5 failures, such as cheating or gaming graders, descend directly from reward hacking?
3. What does DPO remove from the RLHF pipeline, and what might be lost with it?
