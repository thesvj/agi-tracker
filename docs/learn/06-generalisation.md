# 06 · Generalisation and the ARC story

**Goal.** You can explain the difference between memorising and generalising, tell the history of the ARC benchmarks, and read ARC results critically.

**Why it matters for AGI.** T2 (learning new things) is where 2026 moved most, and where claims are easiest to over-read.

## Core ideas

- **In-distribution versus out-of-distribution:** doing well on things like the training data is not the same as handling the truly new.
- **Priors:** humans bring core knowledge (objects, counting, geometry, goals). ARC assumes only these.
- **Skill-acquisition efficiency:** how much experience is needed to learn a new skill. ARC-AGI-3 measures it as *number of actions* compared with humans.
- **The ARC timeline:**
  - ARC-AGI-1 (2019): static grid puzzles. o3 cracked it in Dec 2024 (75.7% / 87.5%).
  - ARC-AGI-2 (2025): harder static puzzles. Reported to be near saturation by late 2026.
  - ARC-AGI-3 (2026): interactive games with no instructions. Below 1% at launch (March). 62.7% Standard and 99.9% with the adapter harness (GPT-6 Astra, September).
- **The harness caveat:** "the model" means model plus harness. Report both.

## Read

1. ⭐ Chollet 2019 ([1911.01547](https://arxiv.org/abs/1911.01547)): §II–III.
2. ⭐ ARC-AGI-3 technical report ([2603.24621](https://arxiv.org/abs/2603.24621)).
3. ⭐ [ARC Prize on GPT-6 Astra](https://arcprize.org/blog/astra), including the caveats section.
4. Chollet et al. 2025, ARC-AGI-2 ([2505.11831](https://arxiv.org/abs/2505.11831)).
5. [ARC Prize: o3 breakthrough](https://arcprize.org/blog/oai-o3-pub-breakthrough) (Dec 2024).

## Do

Play 3 public ARC-AGI-3 games at [arcprize.org](https://arcprize.org/). Count your actions. Then write down what you had to *discover* (the goal, the rules) and how. That is what T2 asks of AI.

## Check yourself

1. Why did ARC switch from static puzzles to interactive games?
2. Why are the 62.7% and 99.9% ARC-AGI-3 numbers not comparable?
3. ARC Prize says saturating ARC-AGI-3 would not prove AGI. Give their reason in one sentence.
