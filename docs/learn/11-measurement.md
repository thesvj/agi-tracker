# 11 · Measuring and forecasting progress

**Goal.** You can read any benchmark claim critically, and you can make and update your own AGI forecast from the tracker's data.

**Why it matters for AGI.** Every claim about AGI rests on a measurement. Bad measurement makes the field look faster or slower than it is.

## Core ideas

- **Saturation:** when the top scores are near the ceiling, a benchmark stops telling models apart. Benchmark lifetimes have shrunk from years to months.
- **Contamination:** test data leaks into training. Guards: private sets, fresh problems, interactive tests.
- **Harness and settings:** the same model can score 62.7% or 99.9% (ARC-AGI-3). Always ask "under what setting?".
- **Aggregate indices:** Epoch ECI combines 40+ benchmarks with statistical difficulty weights, anchored at Claude 3.5 Sonnet = 130 and GPT-5 = 150.
- **Trend extrapolation:** straight lines on log plots are useful but break. Always say "if the trend continued".
- **Forecasting hygiene:** write your forecast down with a date and a probability, then score yourself later.

## Read

1. ⭐ [The tracker](../tracker.md), including "How to read the sources".
2. ⭐ [Epoch ECI page](https://epoch.ai/eci) (method and FAQ).
3. Phan et al. 2025, *Humanity's Last Exam* ([2501.14249](https://arxiv.org/abs/2501.14249)).
4. Sevilla et al. 2022, compute trends ([2202.05924](https://arxiv.org/abs/2202.05924)).
5. [AI 2027](https://ai-2027.com/) scenario and the [AI 2027 tracker](https://ai2027-tracker.com/).

## Do

Write down your own forecast: for each of T1–T5, the year by which you think it passes (50% confidence), plus one sentence of reasoning. Revisit it every quarter.

## Check yourself

1. Name three things you must know before comparing two benchmark numbers.
2. Why can ECI show progress after single benchmarks saturate?
3. What is wrong with extrapolating the 50% METR horizon to "AGI in year X"?
