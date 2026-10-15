# World models, multimodality and robots

By the end of this module you should be able to explain what a world model is, how it differs from next-token prediction, and why robotics moves more slowly than software. Many researchers think planning in the real world needs grounded world models, and embodied AGI depends on them.

## Main ideas

A world model is a learned simulator that predicts the next state from the current state and an action. An agent with one can plan by imagining the results of different actions. In model-based reinforcement learning, as in Dreamer, the agent learns the world model first and then trains its policy inside it.

Generative interactive environments are video models that can be steered with actions, such as Genie (2024) and Genie 3 (2025). LeCun's JEPA approach predicts in an abstract representation space instead of in pixels, so the model can ignore detail that can't be predicted.

Vision-language-action models such as RT-2 and π0 use knowledge from web-trained vision-language models to produce robot actions. Moravec's paradox explains why progress there is slow: sensing and moving are hard for machines, while abstract reasoning is comparatively easy.

## Reading

Start with these:

1. Ha and Schmidhuber 2018, *World Models* ([1803.10122](https://arxiv.org/abs/1803.10122)).
2. LeCun 2022, [*A Path Towards Autonomous Machine Intelligence*](https://openreview.net/pdf?id=BZ5a1r-kVsf).

Further reading:

3. Hafner et al. 2023, DreamerV3 ([2301.04104](https://arxiv.org/abs/2301.04104)).
4. Bruce et al. 2024, Genie ([2402.15391](https://arxiv.org/abs/2402.15391)).
5. Assran et al. 2025, V-JEPA 2 ([2506.09985](https://arxiv.org/abs/2506.09985)).
6. Brohan et al. 2023, RT-2 ([2307.15818](https://arxiv.org/abs/2307.15818)), and Black et al. 2024, π0 ([2410.24164](https://arxiv.org/abs/2410.24164)).

## Exercise

Watch a demo video of a generated world and list three physics errors, such as objects passing through each other, things appearing from nowhere, or lighting that changes for no reason. For each one, note what a world model would need in order to avoid it.

## Questions

1. How does a world model let an agent plan?
2. What is LeCun's main objection to predicting pixels or tokens?
3. Why is robot data so much scarcer than text?
