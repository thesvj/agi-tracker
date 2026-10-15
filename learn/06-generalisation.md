# Generalisation and the ARC benchmarks

By the end of this module you should be able to explain the difference between memorising and generalising, tell the history of the ARC benchmarks, and read ARC results with the right caveats. T2 moved more than any other test in 2026, and it is also where results are easiest to over-read.

## Main ideas

Doing well on material similar to the training data is in-distribution performance. Handling something genuinely new is out-of-distribution, and it is much harder.

People bring core knowledge to any new problem: objects, counting, basic geometry and the idea that agents have goals. ARC assumes only these priors. It measures skill-acquisition efficiency, meaning how much experience a system needs to learn something new, and ARC-AGI-3 counts this as the number of actions taken compared with humans.

ARC-AGI-1 (2019) used static grid puzzles, and o3 broke through in December 2024 with 75.7% at low compute and 87.5% at high compute. ARC-AGI-2 (2025) used harder static puzzles and was reported to be near saturation by late 2026. ARC-AGI-3 (2026) uses interactive games with no instructions. Frontier models scored below 1% when it launched in March, and in September GPT-6 Astra scored 62.7% with the Standard harness and 99.9% with the adapter harness.

Any ARC result belongs to the model and its harness together, so both need to be reported.

## Reading

Start with these:

1. Chollet 2019 ([1911.01547](https://arxiv.org/abs/1911.01547)), parts II and III.
2. The ARC-AGI-3 technical report ([2603.24621](https://arxiv.org/abs/2603.24621)).
3. [ARC Prize on GPT-6 Astra](https://arcprize.org/blog/astra), including its caveats.

Further reading:

4. Chollet et al. 2025, ARC-AGI-2 ([2505.11831](https://arxiv.org/abs/2505.11831)).
5. [ARC Prize on the o3 result](https://arcprize.org/blog/oai-o3-pub-breakthrough), December 2024.

## Exercise

Play three public ARC-AGI-3 games at [arcprize.org](https://arcprize.org/) and count your actions. Afterwards, write down what you had to work out for yourself, such as the goal and the rules, and how you worked it out. T2 asks AI systems to do the same.

## Questions

1. Why did ARC move from static puzzles to interactive games?
2. Why can't the 62.7% and 99.9% ARC-AGI-3 results be compared?
3. ARC Prize says saturating ARC-AGI-3 wouldn't prove AGI. What is their reason, in one sentence?
