# Deep learning and transformers

By the end of this module you should be able to explain how a transformer language model turns text into a prediction of the next token, and why such a simple training objective produces broad abilities. Every frontier system on the [tracker](../tracker.md) is a transformer, and knowing how they work helps you tell which limits are fundamental and which are engineering problems.

## Main ideas

A token is a piece of text, about three quarters of a word on average. The model predicts the next token, appends it, and repeats. Each token is first turned into a vector, called an embedding, and every layer of the network updates these vectors.

Attention lets each token look back at all the earlier tokens and draw in whatever is relevant, which is how the model makes use of its context. The feed-forward (MLP) layers between the attention layers hold much of what the model knows.

Training adjusts billions of weights to reduce the prediction error, called the loss, over trillions of tokens. Predicting text well requires modelling whatever produced the text, including facts, reasoning and the writer's intentions, and this is why next-token prediction leads to general abilities.

Most frontier models use a mixture of experts, in which only part of the network is active for each token. This lowers the cost per token.

## Reading

Start with these:

1. Vaswani et al. 2017, *Attention Is All You Need* ([1706.03762](https://arxiv.org/abs/1706.03762)).
2. Karpathy, [*Let's build GPT: from scratch*](https://www.youtube.com/watch?v=kCc8FmEb1nY), a video of about two hours.

Further reading:

3. Brown et al. 2020, GPT-3 ([2005.14165](https://arxiv.org/abs/2005.14165)). Sections 1 to 3 cover in-context learning.
4. Fedus et al. 2021, Switch Transformer ([2101.03961](https://arxiv.org/abs/2101.03961)), for mixture of experts.
5. Elhage et al. 2021, [*A Mathematical Framework for Transformer Circuits*](https://transformer-circuits.pub/2021/framework/index.html).

## Exercise

Train a character-level transformer on a small text using nanoGPT or the code from Karpathy's video. Plot the training loss, then sample from the model and note which patterns it picks up first.

## Questions

1. In one sentence, what does attention compute?
2. How can a transformer learn from examples in its prompt without any change to its weights, and what does that mean for T4?
3. What does a mixture of experts change about cost, and what does it leave the same?
