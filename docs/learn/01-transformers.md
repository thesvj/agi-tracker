# 01 · Deep learning and transformers

**Goal.** You can explain how a transformer language model turns text into a next-token prediction, and why that simple objective produces broad abilities.

**Why it matters for AGI.** Every frontier system in [Tracker](../tracker.md) is built on transformers. Knowing their mechanics lets you judge which limits are fundamental and which are engineering.

## Core ideas

- **A token** is a chunk of text, about ¾ of a word. The model predicts the next token, again and again.
- **Embeddings** turn tokens into vectors. Each layer updates these vectors.
- **Attention** lets every token look at every earlier token and pull in what is relevant. It is how the model uses context.
- **The MLP layers** (feed-forward blocks) store much of the model's knowledge.
- **Training** adjusts billions of weights to reduce prediction error (the *loss*) on trillions of tokens.
- **Why prediction gives ability:** to predict text well, you must model what produced it, including facts, reasoning and intentions.
- **Mixture of experts (MoE):** only some of the weights are active for each token, which cuts cost per token. Most frontier models use it.

## Read

1. ⭐ Vaswani et al. 2017, *Attention Is All You Need* ([1706.03762](https://arxiv.org/abs/1706.03762)).
2. ⭐ Karpathy, [*Let's build GPT: from scratch*](https://www.youtube.com/watch?v=kCc8FmEb1nY) (video, about 2 h).
3. Brown et al. 2020, GPT-3 ([2005.14165](https://arxiv.org/abs/2005.14165)): §1–3, in-context learning.
4. Fedus et al. 2021, Switch Transformer ([2101.03961](https://arxiv.org/abs/2101.03961)): the MoE idea.
5. Elhage et al. 2021, [*A Mathematical Framework for Transformer Circuits*](https://transformer-circuits.pub/2021/framework/index.html).

## Do

Train a character-level transformer on a small text (nanoGPT or the Karpathy video code). Plot training loss. Then sample from it and note which patterns it learns first.

## Check yourself

1. What does attention compute, in one sentence?
2. Why can a transformer do *in-context learning* without any weight update? How does this relate to T4?
3. What does mixture of experts change about cost, and what does it leave unchanged?
