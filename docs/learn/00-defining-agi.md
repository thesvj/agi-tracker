# 00 · What is AGI, and how would we know?

**Goal.** You can state a precise definition of AGI, compare it with four others, and say which evidence would show that AGI has been reached.

**Why it matters for AGI.** Without a fixed definition, every claim about AGI is untestable. This module is the lens for everything else.

## Core ideas

- **Generality versus performance.** A chess engine is superhuman but narrow. A chatbot is broad but shallow in places. AGI needs both: broad *and* expert (Morris et al. 2023).
- **Knowing versus learning.** A system can know everything on the internet and still learn a new skill badly. Chollet (2019) defines intelligence as *skill-acquisition efficiency*.
- **Behavioural tests.** We judge AGI by what the system does, not by what it is made of. This is why we need benchmarks with human baselines.
- **A cognitive profile.** Hendrycks et al. (2025) use the human Cattell–Horn–Carroll model of intelligence: 10 domains (knowledge, reading and writing, maths, reasoning, working memory, long-term memory storage, memory retrieval, visual, auditory, speed). The result is one score from 0 to 100%.
- **The five tests in this tracker:** breadth, learning new things, long tasks alone, learning on the job, and reliable and affordable.

## Read

1. ⭐ [What is AGI?](../definition.md), the whole page.
2. ⭐ Morris et al. 2023, *Levels of AGI* ([2311.02462](https://arxiv.org/abs/2311.02462)): read §1–4 and the levels table.
3. ⭐ Chollet 2019, *On the Measure of Intelligence* ([1911.01547](https://arxiv.org/abs/1911.01547)): Part I and the ARC section.
4. Hendrycks et al. 2025, *A Definition of AGI* ([2510.18212](https://arxiv.org/abs/2510.18212)), with the [website](https://agidefinition.safe.ai/).
5. Legg & Hutter 2007 ([0712.3329](https://arxiv.org/abs/0712.3329)): skim the definition and the "intelligence tests" survey.

## Do

Pick any frontier model you can access. Place it on Morris et al.'s level grid for three tasks: coding, planning a trip with constraints, and a new puzzle you invent. Write one sentence of evidence per task.

## Check yourself

1. Why does Chollet say that a high score on a test of *knowledge* is weak evidence of intelligence?
2. Give an example of a system that would pass T1 (breadth) and fail T4 (learning on the job).
3. What is the weakness of the OpenAI Charter definition as a *test*?
4. Why does this tracker use the 80% time horizon, not the 50% one, for T3?
