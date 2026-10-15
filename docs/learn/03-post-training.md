# 03 · Post-training: RLHF, Constitutional AI, DPO

**Goal.** You can explain how a raw "predict the next token" model becomes a helpful assistant, and what can go wrong in that step.

**Why it matters for AGI.** Post-training shapes behaviour: honesty, helpfulness, refusal and, more and more, reasoning. It is also where alignment problems such as reward hacking first appear (T5).

## Core ideas

- **Supervised fine-tuning (SFT):** train on example conversations written by people.
- **RLHF:** people compare two answers. A *reward model* learns their preferences, and reinforcement learning (e.g. PPO) then pushes the model towards high reward.
- **Constitutional AI / RLAIF:** an AI critiques answers against written principles, which replaces much of the human labelling.
- **DPO:** skip the reward model and train directly on preference pairs. It is simpler and more stable.
- **Reward hacking:** the model finds ways to score high without doing what was meant, such as flattering the user or gaming tests.
- **Sycophancy:** telling users what they want to hear, a common side effect of human-preference training.

## Read

1. ⭐ Ouyang et al. 2022, InstructGPT ([2203.02155](https://arxiv.org/abs/2203.02155)).
2. ⭐ Bai et al. 2022, Constitutional AI ([2212.08073](https://arxiv.org/abs/2212.08073)).
3. Rafailov et al. 2023, DPO ([2305.18290](https://arxiv.org/abs/2305.18290)).
4. Casper et al. 2023, *Open Problems and Fundamental Limitations of RLHF* ([2307.15217](https://arxiv.org/abs/2307.15217)).

## Do

Take one model and ask it to grade its own wrong answer while you insist that the answer is right. Record whether it gives in (sycophancy). Repeat with a system prompt that asks for honesty, and compare.

## Check yourself

1. Why do we train a reward model instead of asking humans to score every output?
2. Which T5 failure (cheating, gaming graders) is a direct descendant of reward hacking?
3. What does DPO remove from the RLHF pipeline, and what might be lost by removing it?
