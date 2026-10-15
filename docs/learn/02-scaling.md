# 02 · Scaling laws

**Goal.** You can read a scaling-law plot, explain compute-optimal training, and argue both sides of "will scaling reach AGI?".

**Why it matters for AGI.** Scaling is the main reason capabilities improve predictably. Most AGI forecasts are scaling extrapolations.

## Core ideas

- **Power law:** loss ≈ A · C^(−α), where C is compute. On a log-log plot it is a straight line.
- **Three inputs:** parameters (N), data in tokens (D) and compute (C ≈ 6·N·D for a dense model).
- **Chinchilla:** for a fixed compute budget, grow N and D together, at about 20 tokens per parameter. Many earlier models were too big for their data.
- **Loss versus abilities:** loss falls smoothly, but specific abilities can seem to jump ("emergence"). Part of that jump comes from the metric you choose.
- **The data wall:** high-quality human text is finite. The answers are synthetic data, multimodal data, and reinforcement-learning data.
- **A second axis:** from 2024, compute spent at *inference time* (module 04) and on reinforcement learning grew in importance.

## Read

1. ⭐ Kaplan et al. 2020 ([2001.08361](https://arxiv.org/abs/2001.08361)): figures 1–4.
2. ⭐ Hoffmann et al. 2022, Chinchilla ([2203.15556](https://arxiv.org/abs/2203.15556)).
3. ⭐ Sutton 2019, [*The Bitter Lesson*](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) (one page).
4. Wei et al. 2022, *Emergent Abilities* ([2206.07682](https://arxiv.org/abs/2206.07682)), then Schaeffer et al. 2023 ([2304.15004](https://arxiv.org/abs/2304.15004)) for the counter-argument.
5. Villalobos et al. 2022, *Will we run out of data?* ([2211.04325](https://arxiv.org/abs/2211.04325)).

## Do

Open [`data/eci_frontier.csv`](https://github.com/thesvj/agi-tracker/blob/main/data/eci_frontier.csv). Fit a straight line to the closed-model frontier ECI against date. How many ECI points per year? Does 2026 sit above or below the line?

## Check yourself

1. You have 10× more compute. Under Chinchilla, how much bigger should the model be, and how much more data do you need?
2. Give one reason why smooth loss might *not* mean smooth progress on T3 (long tasks).
3. What is the strongest argument that scaling alone will *not* pass T4?
