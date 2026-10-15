# 08 · World models, multimodality and robots

**Goal.** You can explain what a world model is, how it differs from next-token prediction, and why robotics moves more slowly.

**Why it matters for AGI.** Many researchers think grounded world models are needed for real planning, and embodied AGI depends on them.

## Core ideas

- **World model:** a learned simulator that predicts the next state from the current state and an action. With one, an agent can plan by "imagining".
- **Model-based reinforcement learning:** learn the world model, then train the policy inside it (Dreamer).
- **Generative interactive environments:** video models you can steer with actions (Genie, 2024; Genie 3, 2025).
- **JEPA (LeCun):** predict in an *abstract* space, not pixels, so the model ignores unpredictable detail.
- **Vision-language-action models (VLAs):** use web-trained vision-language knowledge to output robot actions (RT-2, π0).
- **Moravec's paradox:** sensing and moving is hard for machines; abstract thinking is comparatively easy.

## Read

1. ⭐ Ha & Schmidhuber 2018, *World Models* ([1803.10122](https://arxiv.org/abs/1803.10122)).
2. ⭐ LeCun 2022, [*A Path Towards Autonomous Machine Intelligence*](https://openreview.net/pdf?id=BZ5a1r-kVsf).
3. Hafner et al. 2023, DreamerV3 ([2301.04104](https://arxiv.org/abs/2301.04104)).
4. Bruce et al. 2024, Genie ([2402.15391](https://arxiv.org/abs/2402.15391)).
5. Assran et al. 2025, V-JEPA 2 ([2506.09985](https://arxiv.org/abs/2506.09985)).
6. Brohan et al. 2023, RT-2 ([2307.15818](https://arxiv.org/abs/2307.15818)), and Black et al. 2024, π0 ([2410.24164](https://arxiv.org/abs/2410.24164)).

## Do

Find one generated-world demo video. List three physics errors (objects passing through each other, things appearing, inconsistent lighting). What would a world model need in order to avoid each one?

## Check yourself

1. How does a world model let an agent plan?
2. What is LeCun's main objection to predicting pixels or tokens?
3. Why is robot data so much scarcer than text data?
