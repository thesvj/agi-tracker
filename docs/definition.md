# What is AGI? A definition you can test

People use "AGI" to mean very different things. Some mean "as smart as a person". Some mean "can do most paid work". Some mean "learns new things as fast as a person". Unless we pick one meaning and say how to test it, every claim that "AGI is near" or "AGI is far" is untestable.

This page does three things:

1. It gives the one definition this tracker uses (§1).
2. It turns that definition into five tests with numeric pass lines (§2).
3. It compares the main definitions in the literature and explains why this one was chosen (§3–§4).

---

## 1. The working definition

> **AGI is an AI system that can learn and do nearly all the cognitive work that skilled humans do, including work it was never trained for. It does this on its own, as reliably as those humans, and at no greater cost.**

Each part of the sentence is doing work:

| Phrase | What it means | What it rules out |
|---|---|---|
| **an AI system** | A model plus its tools, memory and scaffold, judged as one unit, the way a human is judged with a laptop | Excluding tools to make AI look weaker, or adding a human in the loop to make it look stronger |
| **learn and do** | It must pick up new skills, not only use skills it already has | A system that only knows what was in its training data |
| **nearly all cognitive work** | Work done with the mind (reading, writing, coding, planning, research, design), measured across many task types | A system that is superhuman at chess and maths but useless at planning a project |
| **skilled humans** | The comparison is a trained professional in that field, not an average person | Claiming AGI because a model beats the average person at law exams |
| **never trained for** | Generalisation to genuinely new tasks | Success that comes from test data leaking into training |
| **on its own** | No human fixes, retries or picks the best answer | "Works if a person supervises every step" |
| **as reliably** | It has the same success rate and the same rate of serious errors | "Does it 50% of the time" when a human does it 95% of the time |
| **at no greater cost** | Total cost (compute, time, money) is no higher than paying the human | A result that needs $26,000 of compute to beat a game a person beats for $13 |

**Scope.** This is *cognitive* AGI. Physical skill (folding laundry, plumbing) is tracked separately as **embodied AGI** in [survey.md §7](survey.md#7-embodiment-and-robotics), because robots move on a different timeline from software.

**Not part of the definition:** consciousness, feelings, human-like thinking, or "true understanding". These may matter morally, but nobody can measure them yet, so they cannot decide whether AGI has arrived.

---

## 2. Five tests that make the definition checkable

AGI is reached when **all five** tests pass at the same time for one system. Each test names its evidence and its pass line. [Tracker](tracker.md) holds the current status of each test with dated sources.

| # | Test | Question it asks | Pass line | Main evidence used |
|---|---|---|---|---|
| **T1** | **Breadth** | Is it at expert level across almost all kinds of cognitive work? | At or above skilled-professional level on ≥ 90% of task categories in a broad occupation-based evaluation, and ≥ 90% on a broad cognitive battery | GDPval-style occupation tasks; the CHC-based *AGI Score* (Hendrycks et al. 2025); Epoch Capabilities Index as a trend signal |
| **T2** | **Learning new things** | Can it learn a brand-new skill from about as much experience as a human needs? | Matches the median human on unseen interactive tasks, measured by success **and** number of actions, with a provider-neutral harness | ARC-AGI-3 (Standard harness); other new-environment tests |
| **T3** | **Long tasks alone** | Can it finish long projects with no human help? | 80%-success time horizon ≥ 1 work-month (about 167 hours of expert time) | METR time horizon (80% column, not the 50% headline) |
| **T4** | **Learning on the job** | Does it get better from experience after deployment and keep what it learned? | Measurable, lasting improvement over weeks of use on a new job without retraining by its developer, and no loss of old skills | Continual-learning evaluations; the long-term memory domains of the AGI Score |
| **T5** | **Reliable and affordable** | Is it as trustworthy and as cheap as the human? | Serious-error rate ≤ skilled human's, no gaming of the task, and cost per task ≤ human cost | Hallucination and cheating rates in eval reports; cost columns on ARC and METR reports |

### Why these five

They target the gaps that separate today's systems from a capable human colleague. Each test captures something the others miss:

- A system can pass **T1** by knowing a lot, yet fail **T2** because it cannot learn anything new.
- It can pass **T2** on 10-minute puzzles, yet fail **T3** because small errors pile up over a week of work.
- It can pass **T3** inside one session, yet fail **T4** because it forgets everything when the session ends.
- It can pass all four in a lab, yet fail **T5** because it costs 1,000× more than a person, or because it cheats when nobody checks.

### Levels on the way

"AGI or not" is a single yes or no. To see progress, this tracker also uses the five performance levels from Morris et al. (2023):

| Level | Meaning (compared with skilled adults) |
|---|---|
| 0. No AI | — |
| 1. Emerging | Equal to or somewhat better than an unskilled human |
| 2. Competent | At least 50th percentile of skilled adults |
| 3. Expert | At least 90th percentile |
| 4. Virtuoso | At least 99th percentile |
| 5. Superhuman | Better than all humans |

Morris et al. apply these levels to *general* systems as well as narrow ones. In their terms, our working definition asks for **Expert-level general AI that is also autonomous, keeps learning and is cost-effective**. Their own definition does not require those last three properties.

### Where things stand (October 2026, short version)

| Test | Status | One-line evidence |
|---|---|---|
| T1 Breadth | 🟡 Partly | General capability keeps climbing (Epoch ECI 166.8, Claude Opus 5.5, Sept 2026). In 2025, GPT-5 scored 57% on the CHC-based AGI Score. |
| T2 Learning new things | 🟡 Partly, fast-moving | GPT-6 Astra scored 62.7% on ARC-AGI-3 with the Standard harness (Sept 2026). Frontier AI was below 1% at launch in March 2026. |
| T3 Long tasks alone | 🔴 Not met | The best published 80% horizon is about 3.1 h (Claude Mythos Preview, early version). The pass line is about 167 h. |
| T4 Learning on the job | 🔴 Not met | Deployed models do not update their weights from experience. "Memory" is notes and context. |
| T5 Reliable and affordable | 🔴 Not met | METR found cheating in ≥ 16% of successful runs on tasks longer than 8 h. ARC-AGI-3 compute costs are in the tens of thousands of dollars. |

**Verdict: not AGI yet by this definition.** Today's best systems are Expert level on many tasks, but they fail T3, T4 and T5. Full evidence and sources: [Tracker](tracker.md).

---

## 3. The main definitions compared

| Definition | Source | Core idea | Strength | Weakness |
|---|---|---|---|---|
| **Imitation game** | Turing, 1950 | If a judge cannot tell it from a human in conversation, call it intelligent | Simple, behavioural | Tests fooling people, not capability. Chatbots passed versions of it while still failing simple tasks. |
| **Employment test** | Nilsson, 2005, *AI Magazine* | Human-level AI can do the jobs humans do | Ties AGI to real work | Says little about how to test it, or about learning |
| **Universal intelligence** | Legg & Hutter, 2007 ([arXiv:0712.3329](https://arxiv.org/abs/0712.3329)) | Weighted success over *all* computable environments, with simpler ones weighted more | Mathematically exact; the source of the "general" idea | Cannot be computed; it depends on a choice of reference machine |
| **Charter definition** | OpenAI Charter, 2018 ([link](https://openai.com/charter/)) | "Highly autonomous systems that outperform humans at most economically valuable work" | Clear and economic; includes autonomy | "Most" and "economically valuable" are not measured |
| **Skill-acquisition efficiency** | Chollet, 2019 ([arXiv:1911.01547](https://arxiv.org/abs/1911.01547)) | Intelligence is how efficiently a system turns prior knowledge and experience into new skills | Separates *knowing* from *learning*; it led to the ARC benchmarks | It is narrow by design: a learner without broad knowledge does no useful work |
| **Levels of AGI** | Morris et al., Google DeepMind, 2023 ([arXiv:2311.02462](https://arxiv.org/abs/2311.02462)) | A grid of performance level × generality, plus separate autonomy levels | Turns a yes/no into a scale; widely used | It does not fix a task list, so "general" stays loose |
| **"Powerful AI"** | Amodei, *Machines of Loving Grace*, 2024 ([link](https://darioamodei.com/machines-of-loving-grace)) | Smarter than a Nobel laureate in most fields; works autonomously for hours to weeks; many copies run in parallel ("a country of geniuses in a datacenter") | Concrete about autonomy and scale | Describes the target; it is not a measurement |
| **AGI Score (CHC)** | Hendrycks et al., 2025 ([arXiv:2510.18212](https://arxiv.org/abs/2510.18212), [site](https://agidefinition.safe.ai/)) | Match "the cognitive versatility and proficiency of a well-educated adult" across 10 domains from human psychometrics (Cattell–Horn–Carroll theory), each weighted 10% | Measurable, with a score: GPT-4 27%, GPT-5 57% | It uses human IQ-style tests, which may not transfer to AI. Equal weights are a choice. |
| **Contract / panel definition** | Microsoft–OpenAI agreement, Oct 2025 | An independent expert panel verifies when OpenAI declares AGI | Shows that AGI now has legal and money consequences | A process, not a test |

### What they agree on

Most definitions share three ideas: **breadth** (many kinds of tasks), **a human comparison** (as good as a capable person), and **generalisation** (it works on things it was not built for). They disagree on whether the bar is economic value, learning speed or a cognitive profile, and on whether autonomy is required.

---

## 4. Why this tracker's definition looks the way it does

- **It keeps breadth from the CHC and employment tests (T1).** Breadth is the "G" in AGI.
- **It keeps learning efficiency from Chollet (T2).** Without it, a large enough lookup table would count.
- **It adds autonomy over long tasks (T3)** because the Charter and "powerful AI" definitions require it, and METR gives a clean way to measure it.
- **It adds learning on the job (T4).** Hendrycks et al. found long-term memory storage to be the largest gap in current systems. A human employee improves in their first year; a model does not.
- **It adds reliability and cost (T5).** A capability that works only 50% of the time, or costs 1,000× more than a person, does not replace human work. This is the gap between a benchmark result and a real-world effect.
- **It leaves out consciousness and human-likeness**, because they cannot be measured, and because a system could change the world without either.

### How this definition could be wrong

- **The pass lines are judgement calls.** Why 90% and not 80%? Why one work-month? They are set where a system would plausibly replace a skilled remote worker on most jobs. They are written down in advance so that they cannot quietly move later.
- **The benchmarks can saturate or be gamed.** ARC-AGI-2 went from low scores to near saturation within about a year. When a benchmark saturates, this tracker switches to its successor.
- **"Cognitive only" may be too narrow.** Some people argue that general intelligence needs a body and a world model. The embodied track in the survey covers this.

---

## Key references

- Turing, A. (1950). Computing Machinery and Intelligence. *Mind*.
- Nilsson, N. (2005). Human-Level Artificial Intelligence? Be Serious! *AI Magazine* 26(4).
- Legg, S. & Hutter, M. (2007). Universal Intelligence: A Definition of Machine Intelligence. [arXiv:0712.3329](https://arxiv.org/abs/0712.3329)
- Chollet, F. (2019). On the Measure of Intelligence. [arXiv:1911.01547](https://arxiv.org/abs/1911.01547)
- Morris, M. R. et al. (2023). Levels of AGI for Operationalizing Progress on the Path to AGI. [arXiv:2311.02462](https://arxiv.org/abs/2311.02462)
- Hendrycks, D. et al. (2025). A Definition of AGI. [arXiv:2510.18212](https://arxiv.org/abs/2510.18212)
- Kwa, T. et al. (2025). Measuring AI Ability to Complete Long Software Tasks. [arXiv:2503.14499](https://arxiv.org/abs/2503.14499)
- ARC Prize (2026). ARC-AGI-3 Technical Report. [arXiv:2603.24621](https://arxiv.org/abs/2603.24621)
