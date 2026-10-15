# What is AGI, and how would we know?

By the end of this module you should be able to state a precise definition of AGI, compare it with four others, and say what evidence would show that AGI had been reached. Without a fixed definition, claims about AGI can't be tested, so the rest of the path builds on this module.

## Main ideas

Generality and performance are separate. A chess engine is superhuman in one narrow area, while a chatbot covers a wide range but is shallow in places. AGI needs both breadth and expert-level performance (Morris et al. 2023).

Knowing is also separate from learning. A system could know everything on the internet and still be slow to learn a new skill. Chollet (2019) defines intelligence as the efficiency with which a system acquires skills.

AGI is judged by what a system does, whatever it is built from, which is why the field needs benchmarks with human baselines.

Hendrycks et al. (2025) borrow the Cattell-Horn-Carroll model of human intelligence. It has 10 domains: knowledge, reading and writing, maths, reasoning, working memory, long-term memory storage, memory retrieval, visual processing, auditory processing and speed. The result is a single score from 0 to 100%.

The tracker's five tests are breadth, learning new things, long tasks alone, learning on the job, and reliability with affordability.

## Reading

Start with these:

1. [What is AGI?](../definition.md), the whole page.
2. Morris et al. 2023, *Levels of AGI* ([2311.02462](https://arxiv.org/abs/2311.02462)). Read sections 1 to 4 and the table of levels.
3. Chollet 2019, *On the Measure of Intelligence* ([1911.01547](https://arxiv.org/abs/1911.01547)). Read Part I and the section on ARC.

Further reading:

4. Hendrycks et al. 2025, *A Definition of AGI* ([2510.18212](https://arxiv.org/abs/2510.18212)), and its [website](https://agidefinition.safe.ai/).
5. Legg and Hutter 2007 ([0712.3329](https://arxiv.org/abs/0712.3329)). Skim the definition and the survey of intelligence tests.

## Exercise

Choose a frontier model you have access to. Place it on the Morris et al. grid of levels for three tasks: writing code, planning a trip under some constraints, and a puzzle you make up yourself. Write one sentence of evidence for each placement.

## Questions

1. Why does Chollet consider a high score on a test of knowledge to be weak evidence of intelligence?
2. Describe a system that would pass T1 (breadth) but fail T4 (learning on the job).
3. What makes the OpenAI Charter definition hard to use as a test?
4. Why does the tracker use the 80% time horizon for T3 instead of the 50% one?
