# Scaling laws

By the end of this module you should be able to read a scaling-law plot, explain compute-optimal training, and make the case for and against the idea that scaling alone will reach AGI. Scaling is the main reason capabilities improve predictably, and most AGI forecasts are extrapolations of it.

## Main ideas

Loss falls as a power law in compute: roughly loss ≈ A · C^(−α), where C is compute. On a plot with both axes logarithmic, this is a straight line.

Three quantities are involved: the number of parameters N, the amount of training data D in tokens, and compute C, which for a dense model is about 6·N·D. The Chinchilla result says that for a fixed compute budget, N and D should grow together, at about 20 tokens per parameter. Many earlier models were too large for the data they were trained on.

Loss falls smoothly, but particular abilities can seem to appear suddenly, which is often called emergence. Part of that suddenness depends on the metric used to measure the ability.

High-quality human text is limited, and the main responses are synthetic data, multimodal data and data generated through reinforcement learning. Since 2024, compute spent at inference time (module 04) and on reinforcement learning has become a second route to improvement.

## Reading

Start with these:

1. Kaplan et al. 2020 ([2001.08361](https://arxiv.org/abs/2001.08361)), figures 1 to 4.
2. Hoffmann et al. 2022, Chinchilla ([2203.15556](https://arxiv.org/abs/2203.15556)).
3. Sutton 2019, [*The Bitter Lesson*](http://www.incompleteideas.net/IncIdeas/BitterLesson.html), one page long.

Further reading:

4. Wei et al. 2022, *Emergent Abilities* ([2206.07682](https://arxiv.org/abs/2206.07682)), followed by Schaeffer et al. 2023 ([2304.15004](https://arxiv.org/abs/2304.15004)) for the counter-argument.
5. Villalobos et al. 2022, *Will we run out of data?* ([2211.04325](https://arxiv.org/abs/2211.04325)).

## Exercise

Open [`data/eci_frontier.csv`](../data/eci_frontier.csv) and fit a straight line to the closed-model scores against date. How many points per year does the line give? Do the 2026 models sit above or below it?

## Questions

1. With 10 times more compute, how much larger should the model be under Chinchilla, and how much more data does it need?
2. Give one reason why smoothly falling loss might not mean smooth progress on T3.
3. What is the strongest argument that scaling by itself won't pass T4?
