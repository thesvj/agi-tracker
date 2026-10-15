# What is AGI?

People use "AGI" for different things. For some it means as smart as a person, for others a system that can do most paid work, and for others something that learns new skills as fast as a person does. Until one meaning is chosen and a way to test it is written down, a claim that AGI is near or far can't be checked.

This page gives the definition the tracker uses, turns it into five tests with numeric pass lines, and compares it with the main definitions in the literature.

## The working definition

> AGI is an AI system that can learn and do nearly all the cognitive work that skilled humans do, including work it was never trained for. It does this on its own, as reliably as those humans, and at no greater cost.

Each phrase in the definition rules something out:

| Phrase | Meaning | Rules out |
|---|---|---|
| an AI system | The model together with its tools, memory and scaffold, judged as one unit, much as a person is judged with a laptop | Removing tools to make the AI look weaker, or adding a human in the loop to make it look stronger |
| learn and do | It picks up new skills as well as using the ones it has | A system limited to what was in its training data |
| nearly all cognitive work | Work done with the mind, such as reading, writing, coding, planning, research and design, measured across many task types | A system that is superhuman at chess and maths but can't plan a project |
| skilled humans | The comparison is a trained professional in the field | Claiming AGI because a model beats the average person on law exams |
| never trained for | It generalises to tasks that are genuinely new | Success that comes from test data leaking into training |
| on its own | No person fixes its work, retries it, or picks the best of several answers | A system that works only while someone supervises each step |
| as reliably | The same success rate and the same rate of serious errors as the human | A system that succeeds 50% of the time on work a human gets right 95% of the time |
| at no greater cost | Total cost in compute, time and money is no higher than paying the human | A result that spends $26,000 of compute to beat a game a person beats for about $13 |

The definition covers cognitive work only. Physical skills such as folding laundry or plumbing are tracked separately as embodied AGI in the [embodiment and robotics part of the survey](survey.md#embodiment-and-robotics), because robotics is on a different timeline from software.

Consciousness, feelings, human-like thinking and "true understanding" are left out. They may matter morally, but nobody can measure them yet, so they can't be used to decide whether AGI has arrived.

## Five tests

A system meets the definition when it passes all five tests at the same time. The [tracker](tracker.md) shows the current status of each test with dated sources.

| | Test | Question | Pass line | Evidence used |
|---|---|---|---|---|
| T1 | Breadth | Is it at expert level across almost all kinds of cognitive work? | At or above skilled-professional level on at least 90% of task categories in a broad occupation-based evaluation, and at least 90% on a broad cognitive battery | Occupation tasks of the GDPval kind; the CHC-based AGI Score (Hendrycks et al. 2025); the Epoch Capabilities Index as a trend signal |
| T2 | Learning new things | Can it learn a new skill from about as much experience as a human needs? | Matches the median human on unseen interactive tasks, counting both success and number of actions, using a provider-neutral harness | ARC-AGI-3 with the Standard harness; other tests built on new environments |
| T3 | Long tasks alone | Can it finish long projects without human help? | An 80%-success time horizon of at least one work-month, about 167 hours of expert time | METR time horizon, using the 80% figure |
| T4 | Learning on the job | Does it improve from experience after deployment and keep what it learned? | Measurable improvement over weeks on a new job that lasts, without retraining by the developer and without losing old skills | Continual-learning evaluations; the long-term memory domains of the AGI Score |
| T5 | Reliable and affordable | Is it as trustworthy as the human, at no greater cost? | Serious-error rate no higher than a skilled human's, no gaming of the task, and cost per task no higher than the human's | Hallucination and cheating rates in evaluation reports; cost figures from ARC and METR |

### Why these five

Each test catches a failure the others would miss. A system can pass T1 because it knows a great deal and still fail T2 because it can't learn anything new. It can pass T2 on ten-minute puzzles and fail T3 because small errors pile up over a week of work. It can pass T3 inside a single session and fail T4 because it forgets everything when the session ends. And it can pass all four in a lab while failing T5, either because it costs a thousand times more than a person or because it cheats when nobody is checking.

### Levels along the way

Whether a system is AGI is a yes-or-no question, which makes progress hard to see. The tracker also uses the five performance levels from Morris et al. (2023):

| Level | Compared with skilled adults |
|---|---|
| 0. No AI | |
| 1. Emerging | Equal to or somewhat better than an unskilled human |
| 2. Competent | At least the 50th percentile of skilled adults |
| 3. Expert | At least the 90th percentile |
| 4. Virtuoso | At least the 99th percentile |
| 5. Superhuman | Better than all humans |

Morris et al. apply these levels to general systems as well as narrow ones. In their terms, the working definition asks for expert-level general AI that also works autonomously, keeps learning and costs no more than a person. Their own definition doesn't require the last three.

### Status in October 2026

| Test | Status | Evidence |
|---|---|---|
| T1 Breadth | Partly | General capability is still rising: Claude Opus 5.5 reached 166.8 on the Epoch Capabilities Index in September 2026. In 2025, GPT-5 scored 57% on the CHC-based AGI Score. |
| T2 Learning new things | Partly, and improving quickly | GPT-6 Astra scored 62.7% on ARC-AGI-3 with the Standard harness in September 2026. When the benchmark launched in March 2026, frontier models scored below 1%. |
| T3 Long tasks alone | Not met | The best published 80% horizon is about 3.1 hours (an early version of Claude Mythos Preview). The pass line is about 167 hours. |
| T4 Learning on the job | Not met | Deployed models don't update their weights from experience. What products call memory is saved notes and context. |
| T5 Reliable and affordable | Not met | METR found cheating in at least 16% of successful runs on tasks longer than 8 hours. ARC-AGI-3 runs cost tens of thousands of dollars in compute. |

The best current systems work at expert level on many tasks, but they fail T3, T4 and T5, so none of them meets this definition yet. The [tracker](tracker.md) has the full evidence.

## Other definitions

| Definition | Source | Main idea | Strength | Weakness |
|---|---|---|---|---|
| Imitation game | Turing, 1950 | If a judge can't tell the machine from a human in conversation, call it intelligent | Simple and based on behaviour | It measures whether people are fooled. Chatbots have passed versions of it while failing simple tasks. |
| Employment test | Nilsson, 2005, *AI Magazine* | Human-level AI can do the jobs that humans do | Ties AGI to real work | Says little about how to test it, or about learning |
| Universal intelligence | Legg and Hutter, 2007 ([arXiv:0712.3329](https://arxiv.org/abs/0712.3329)) | Weighted success over all computable environments, with simpler environments weighted more | Mathematically exact, and the origin of the "general" idea | Can't be computed, and depends on the choice of reference machine |
| Charter definition | OpenAI Charter, 2018 ([link](https://openai.com/charter/)) | "Highly autonomous systems that outperform humans at most economically valuable work" | Clear, economic, and includes autonomy | Nobody measures "most" or "economically valuable" |
| Skill-acquisition efficiency | Chollet, 2019 ([arXiv:1911.01547](https://arxiv.org/abs/1911.01547)) | Intelligence is how efficiently a system turns prior knowledge and experience into new skills | Separates knowing from learning, and led to the ARC benchmarks | Narrow by design, since a fast learner with no broad knowledge does no useful work |
| Levels of AGI | Morris et al., Google DeepMind, 2023 ([arXiv:2311.02462](https://arxiv.org/abs/2311.02462)) | A grid of performance level against generality, with separate autonomy levels | Replaces yes-or-no with a scale; widely used | Has no fixed task list, so "general" stays loose |
| "Powerful AI" | Amodei, *Machines of Loving Grace*, 2024 ([link](https://darioamodei.com/machines-of-loving-grace)) | Smarter than a Nobel laureate in most fields, works on its own for hours to weeks, and runs as many copies in parallel ("a country of geniuses in a datacenter") | Specific about autonomy and scale | Describes a goal, with no measurement attached |
| AGI Score (CHC) | Hendrycks et al., 2025 ([arXiv:2510.18212](https://arxiv.org/abs/2510.18212), [site](https://agidefinition.safe.ai/)) | Match "the cognitive versatility and proficiency of a well-educated adult" across 10 domains taken from human psychometrics (Cattell-Horn-Carroll theory), each weighted 10% | Produces a score: GPT-4 27%, GPT-5 57% | Human IQ-style tests may not transfer to AI, and the equal weights are a choice |
| Contract and panel | Microsoft and OpenAI agreement, October 2025 | An independent panel of experts verifies any declaration of AGI by OpenAI | Shows that AGI now has legal and financial consequences | It's a process with no test behind it |

Most of these definitions share three ideas. The system handles many kinds of task, it is compared with a capable person, and it works on things it wasn't built for. They disagree about whether the bar is economic value, learning speed or a cognitive profile, and about whether autonomy is required.

## Why the definition looks like this

T1 takes breadth from the CHC and employment definitions, since breadth is the "G" in AGI. T2 takes learning efficiency from Chollet; without it, a large enough lookup table would count.

T3 adds autonomy over long tasks. The OpenAI Charter and Amodei's "powerful AI" both require it, and METR's time horizon gives a clean way to measure it.

T4 adds learning on the job. Hendrycks et al. found long-term memory storage to be the largest gap in current systems. A new employee gets better over their first year, and a deployed model doesn't.

T5 adds reliability and cost. A capability that works half the time, or costs a thousand times more than a person, won't replace anyone's work. This test covers the distance between a benchmark score and an effect in the world.

Consciousness and human-likeness are left out because they can't be measured, and because a system could change the world without either.

### How the definition could be wrong

The pass lines are judgement calls. There is no deep reason for 90% over 80%, or for one work-month. They sit where a system could plausibly replace a skilled remote worker in most jobs, and they are written down in advance so they can't drift later.

Benchmarks also saturate or get gamed. ARC-AGI-2 went from low scores to near saturation in about a year. When a benchmark saturates, the tracker moves the test to its successor.

Finally, limiting the definition to cognitive work may be too narrow. Some researchers argue that general intelligence needs a body and a world model. The embodied track in the survey follows that work.

## References

- Turing, A. (1950). Computing Machinery and Intelligence. *Mind*.
- Nilsson, N. (2005). Human-Level Artificial Intelligence? Be Serious! *AI Magazine* 26(4).
- Legg, S. and Hutter, M. (2007). Universal Intelligence: A Definition of Machine Intelligence. [arXiv:0712.3329](https://arxiv.org/abs/0712.3329)
- Chollet, F. (2019). On the Measure of Intelligence. [arXiv:1911.01547](https://arxiv.org/abs/1911.01547)
- Morris, M. R. et al. (2023). Levels of AGI for Operationalizing Progress on the Path to AGI. [arXiv:2311.02462](https://arxiv.org/abs/2311.02462)
- Hendrycks, D. et al. (2025). A Definition of AGI. [arXiv:2510.18212](https://arxiv.org/abs/2510.18212)
- Kwa, T. et al. (2025). Measuring AI Ability to Complete Long Software Tasks. [arXiv:2503.14499](https://arxiv.org/abs/2503.14499)
- ARC Prize (2026). ARC-AGI-3 Technical Report. [arXiv:2603.24621](https://arxiv.org/abs/2603.24621)
