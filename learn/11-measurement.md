# Measuring and forecasting progress

By the end of this module you should be able to read a benchmark claim critically and to make, and later update, your own AGI forecast from the tracker's data. Every claim about AGI rests on a measurement, and poor measurement makes the field look faster or slower than it is.

## Main ideas

A benchmark is saturated when the top scores sit near its ceiling and it can no longer tell models apart. Benchmarks that used to last years now saturate within months.

Contamination is when test data leaks into training. Private test sets, newly written problems and interactive tests all help guard against it.

Settings matter. On ARC-AGI-3 the same model scores 62.7% with one harness and 99.9% with another, so the first question about any number is what setting produced it.

Epoch's capability index combines more than 40 benchmarks, weighting them by statistically estimated difficulty, on a scale where Claude 3.5 Sonnet is 130 and GPT-5 is 150. Because it draws on many benchmarks, it keeps showing progress after individual benchmarks saturate.

Straight lines on log plots are useful for extrapolation but eventually break, so any projection should be stated as what would happen if the trend continued. When you forecast, write it down with a date and a probability, so that you can score yourself later.

## Reading

Start with these:

1. [The tracker](../tracker.md), including the part on reading the sources.
2. Epoch's [capability index page](https://epoch.ai/eci), especially the method and the FAQ.

Further reading:

3. Phan et al. 2025, *Humanity's Last Exam* ([2501.14249](https://arxiv.org/abs/2501.14249)).
4. Sevilla et al. 2022, compute trends ([2202.05924](https://arxiv.org/abs/2202.05924)).
5. The [AI 2027](https://ai-2027.com/) scenario and the [AI 2027 tracker](https://ai2027-tracker.com/).

## Exercise

Write down your own forecast. For each of T1 to T5, give the year by which you think it will be passed, at 50% confidence, with one sentence of reasoning. Come back to it every three months.

## Questions

1. Name three things you need to know before comparing two benchmark numbers.
2. Why can the capability index show progress after individual benchmarks have saturated?
3. What is wrong with extrapolating METR's 50% horizon to "AGI in year X"?
