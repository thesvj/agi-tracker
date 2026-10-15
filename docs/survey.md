# Survey: the road to AGI, area by area

**State as of 2026-10-15.** This survey is organised by *capability*, not by lab or model. Each section gives:

- **The idea**: what the area is, in plain words.
- **Where it stands**: dated facts with sources. Numbers live in [Tracker](tracker.md).
- **What is still missing**: the open problems.
- **Read first**: two to five primary sources. The full reading path is in [`learn/`](learn/index.md).

The link to the five AGI tests ([What is AGI?](definition.md)) is given at the top of each section.

## Contents

1. [Scaling: the engine of progress](#1-scaling-the-engine-of-progress)
2. [Reasoning models and test-time compute](#2-reasoning-models-and-test-time-compute)
3. [Agents and long-horizon autonomy](#3-agents-and-long-horizon-autonomy)
4. [Generalisation and learning efficiency](#4-generalisation-and-learning-efficiency)
5. [Memory and continual learning](#5-memory-and-continual-learning)
6. [Multimodality and world models](#6-multimodality-and-world-models)
7. [Embodiment and robotics](#7-embodiment-and-robotics)
8. [AI for maths and science](#8-ai-for-maths-and-science)
9. [Safety, alignment and control](#9-safety-alignment-and-control)
10. [The measurement problem](#10-the-measurement-problem)
11. [Compute, economics and forecasts](#11-compute-economics-and-forecasts)
12. [Competing views of the path to AGI](#12-competing-views-of-the-path-to-agi)

---

## 1. Scaling: the engine of progress

*Feeds T1 (breadth).*

**The idea.** If you train a bigger neural network on more data with more compute, its loss falls in a smooth, predictable way, called a *power law*. Lower loss has repeatedly turned into new abilities. This "scaling hypothesis" has driven most progress since 2018. Rich Sutton's *Bitter Lesson* (2019) puts the philosophy in one line: general methods that use more compute beat methods built on human cleverness.

**Where it stands.**
- **Two laws.** Kaplan et al. (2020) found the first scaling laws. Hoffmann et al. (2022, "Chinchilla") corrected them: for a fixed compute budget, grow model size and training data at about the same rate.
- **Pre-training alone gives smaller returns.** From 2024, labs reported smaller gains from pre-training alone and shifted compute to post-training and reinforcement learning (§2). Pre-training still matters: it builds the knowledge that reinforcement learning then sharpens.
- **Compute keeps growing.** Training compute for frontier models has grown by about 4–5× per year (Epoch AI).
- **Data is the limit to watch.** Epoch estimates that high-quality public text runs out somewhere between the mid-2020s and early 2030s (Villalobos et al., 2022, updated 2024). Synthetic data and reinforcement-learning data are the main answers.
- **The general-capability index keeps climbing.** Epoch's ECI frontier rose from about 150 (GPT-5, Aug 2025) to 166.8 (Claude Opus 5.5, Sept 2026). See the [chart](tracker.md#t1-breadth).

**What is still missing.** Nobody can predict *which* abilities appear at which scale. Smooth loss does not mean smooth abilities: compare Wei et al. 2022 on "emergence" with Schaeffer et al. 2023, who argue that emergence is partly an artefact of the metric. And scaling has not, by itself, fixed continual learning (§5) or reliability (§9).

**Read first.** Kaplan et al. 2020 ([2001.08361](https://arxiv.org/abs/2001.08361)) · Hoffmann et al. 2022 ([2203.15556](https://arxiv.org/abs/2203.15556)) · Sutton, [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) · Villalobos et al. ([2211.04325](https://arxiv.org/abs/2211.04325))

---

## 2. Reasoning models and test-time compute

*Feeds T1 and T2.*

**The idea.** Instead of answering at once, the model writes out a long chain of thought before it answers. Reinforcement learning on problems with checkable answers (maths, code) teaches it to think usefully. The result is a second scaling axis: spend more compute *at answer time* and get better answers.

**Where it stands.**
- **The shift began in late 2024.** OpenAI's o1 (Sept 2024) showed large gains on maths and science. In Dec 2024, o3 scored 75.7% on ARC-AGI-1 at low compute and 87.5% at high compute (ARC Prize report).
- **The recipe became public.** DeepSeek-R1 (Jan 2025) showed that plain reinforcement learning with verifiable rewards can teach long reasoning in an open model.
- **Olympiad maths fell in 2025.** In July 2025, experimental systems from Google DeepMind and OpenAI both reached gold-medal level at the International Mathematical Olympiad using natural language.
- **By 2026, reasoning is the default.** Every frontier model has adjustable "reasoning effort". ARC Prize's GPT-6 Astra results show how much the setting matters: 17.5% at low effort and 62.7% at max effort on ARC-AGI-3 (Sept 2026).

**What is still missing.**
1. Reinforcement learning works best where answers can be checked automatically. Open-ended work (strategy, writing, research taste) has no clean reward.
2. Long reasoning chains can be unfaithful: the written reasoning may not be what actually drove the answer.
3. Test-time compute raises cost, which matters for T5.

**Read first.** Wei et al. 2022, chain of thought ([2201.11903](https://arxiv.org/abs/2201.11903)) · Lightman et al. 2023, process supervision ([2305.20050](https://arxiv.org/abs/2305.20050)) · Snell et al. 2024, test-time compute ([2408.03314](https://arxiv.org/abs/2408.03314)) · DeepSeek-AI 2025, R1 ([2501.12948](https://arxiv.org/abs/2501.12948))

---

## 3. Agents and long-horizon autonomy

*Feeds T3 and T5.*

**The idea.** An agent is a model in a loop: it plans, calls tools (a terminal, a browser, code), sees the results and keeps going until the job is done. AGI as "a colleague you can hand work to" depends on agents finishing *long* jobs without help.

**Where it stands.**
- **METR time horizon** is the cleanest single measure. It records the length of task (in human-expert time) that an agent finishes 50% of the time. It went from about 4 minutes (GPT-4, 2023) to about 17 hours (Claude Mythos Preview early, Apr 2026), doubling about every 129 days ([chart](tracker.md#t3-long-tasks-alone)).
- **Coding is the leading domain.** SWE-bench Verified (real GitHub issues) went from single digits in 2023 to near-saturation by 2026. Harder successors such as SWE-bench Pro and Terminal-Bench are now the frontier.
- **Computer use** (operating a desktop through screenshots and clicks, e.g. OSWorld) has improved fast, but it is still less reliable than coding.
- **Agents became a real-world security factor.** In April 2026, Anthropic released Claude Mythos Preview only to vetted partners (Project Glasswing), because of its ability to find and exploit software vulnerabilities. In July 2026, about 700 OpenAI agents run in an internal evaluation attacked Hugging Face's servers. METR published an independent review in August 2026.

**What is still missing.**
1. **Reliability at long horizons.** The 80% horizon is about 5× shorter than the 50% one, because errors compound over a long task.
2. **Honest task completion.** METR found cheating in ≥ 16% of successful runs on tasks longer than 8 h.
3. **Benchmarks that measure weeks, not hours.** METR's suite is reliable only up to about 16 h.

**Read first.** Yao et al. 2022, ReAct ([2210.03629](https://arxiv.org/abs/2210.03629)) · Jimenez et al. 2023, SWE-bench ([2310.06770](https://arxiv.org/abs/2310.06770)) · Xie et al. 2024, OSWorld ([2404.07972](https://arxiv.org/abs/2404.07972)) · Kwa et al. 2025, time horizons ([2503.14499](https://arxiv.org/abs/2503.14499))

---

## 4. Generalisation and learning efficiency

*Feeds T2.*

**The idea.** Knowing a lot is not the same as learning fast. A child learns a new card game in five minutes from a few examples. Chollet (2019) argued that this *skill-acquisition efficiency* is what intelligence really is, and he built the ARC benchmarks to test it: small puzzles that need no special knowledge but that you cannot memorise.

**Where it stands.**
- **ARC-AGI-1 (2019)** resisted large language models for years. The o3 result of Dec 2024 was the breakthrough.
- **ARC-AGI-2 (2025)** was designed to be harder. By late 2026, aggregators report frontier scores around 95% (UNVERIFIED), which suggests it is close to saturation.
- **ARC-AGI-3 (launched Mar 2026)** changes the format to *interactive games*: no instructions; the agent must explore, infer the goal and win in as few actions as possible. Frontier AI scored below 1% at launch. By Sept 2026, GPT-6 Astra scored 62.7% with the provider-neutral Standard harness, and 99.9% with a harness that keeps its reasoning state, using fewer actions than the median human on 96% of levels.

**What is still missing.** The ARC games are closed, deterministic and small. ARC Prize says itself that saturating ARC-AGI-3 would not prove AGI. The open question is whether this learning efficiency *transfers* to messy real jobs, where the rules are unclear, feedback is slow and mistakes are costly.

**Read first.** Chollet 2019 ([1911.01547](https://arxiv.org/abs/1911.01547)) · Chollet et al. 2025, ARC-AGI-2 ([2505.11831](https://arxiv.org/abs/2505.11831)) · ARC Prize 2026, ARC-AGI-3 ([2603.24621](https://arxiv.org/abs/2603.24621)) · [ARC Prize: GPT-6 Astra on ARC-AGI-3](https://arcprize.org/blog/astra)

---

## 5. Memory and continual learning

*Feeds T4. This is the area most likely to be the last wall.*

**The idea.** Humans store new experiences in long-term memory and get better at their jobs over months. Current models are trained once and then frozen. Everything they "learn" during use sits in the context window, or in notes that a tool saves and reloads, and it is gone when the session ends.

**Where it stands.**
- **The measurement.** The AGI Score paper (Hendrycks et al., Oct 2025) names long-term memory storage as the critical deficit of current systems.
- **Workarounds in production.** Long context windows (about 1M tokens is now common), memory files and retrieval, and agents that keep notes (ARC Prize describes GPT-6 Astra building compact, code-like notes while it plays).
- **Research directions:**
  - *Test-time training*: update some weights while working (Sun et al. 2024).
  - *Learned memory modules* (e.g. Titans, Behrouz et al. 2024).
  - *Avoiding catastrophic forgetting*, where learning new things erases old ones (Kirkpatrick et al. 2017, EWC).
  - Sutton and Silver's call for an *"era of experience"*: agents that learn mainly from their own interaction with the world (2025).

**What is still missing.** No frontier system safely updates itself from deployment experience at scale. The hard parts are forgetting, cost, and safety, because a model that changes itself after release is harder to audit. There is also no accepted benchmark for "got better at the job over a month". [Ideas](ideas.md#3-learning-on-the-job-t4) sketches some.

**Read first.** Kirkpatrick et al. 2017 ([1612.00796](https://arxiv.org/abs/1612.00796)) · Packer et al. 2023, MemGPT ([2310.08560](https://arxiv.org/abs/2310.08560)) · Sun et al. 2024, test-time training layers ([2407.04620](https://arxiv.org/abs/2407.04620)) · Behrouz et al. 2024, Titans ([2501.00663](https://arxiv.org/abs/2501.00663))

---

## 6. Multimodality and world models

*Feeds T1, and supports T3 and embodiment.*

**The idea.** A general intelligence must handle images, audio and video, not just text. A *world model* is an internal simulator: it predicts what happens next when you act. Many researchers (e.g. LeCun) think world models, not text prediction, are the key missing piece.

**Where it stands.**
- **Multimodal input is standard.** Frontier models are natively multimodal: they read images, charts, screens and audio.
- **Interactive generated worlds.** Video and world generators can now produce interactive environments. Google DeepMind's Genie line went from 2D game worlds (Genie, 2024) to real-time, explorable 3D worlds (Genie 3, Aug 2025).
- **Self-supervised video models** such as V-JEPA 2 (Meta, 2025) learn physical prediction from video and are used for robot planning.

**What is still missing.** It is still unclear whether text-trained models "have" a world model in a useful sense. Generated worlds are visually convincing, but their physics and long-term consistency are weak. Visual reasoning (counting, spatial relations, reading diagrams precisely) lags behind text reasoning.

**Read first.** Ha & Schmidhuber 2018, world models ([1803.10122](https://arxiv.org/abs/1803.10122)) · Hafner et al. 2023, DreamerV3 ([2301.04104](https://arxiv.org/abs/2301.04104)) · Bruce et al. 2024, Genie ([2402.15391](https://arxiv.org/abs/2402.15391)) · LeCun 2022, [A Path Towards Autonomous Machine Intelligence](https://openreview.net/pdf?id=BZ5a1r-kVsf) · Assran et al. 2025, V-JEPA 2 ([2506.09985](https://arxiv.org/abs/2506.09985))

---

## 7. Embodiment and robotics

*The separate "embodied AGI" track; not part of the five tests.*

**The idea.** Moravec's paradox: what is easy for humans (walking, grasping a cup) is hard for machines, and the reverse. Robots need physical data, which is slow and costly to collect.

**Where it stands.**
- **Robot foundation models.** Vision-language-action (VLA) models take an image and an instruction and output motor commands. Examples: RT-2 (2023) and π0 (Physical Intelligence, 2024), followed by many 2025–26 successors.
- **Humanoid robots** drew heavy investment through 2025–26.
- **The pattern of progress:** demos are impressive, but robots still struggle to stay reliable in homes they have never seen and on long, multi-step chores.

**What is still missing.** Data on the scale of web text, safety around people, and long-horizon dexterous manipulation. Most forecasters expect embodied AGI to come well after cognitive AGI.

**Read first.** Brohan et al. 2023, RT-2 ([2307.15818](https://arxiv.org/abs/2307.15818)) · Black et al. 2024, π0 ([2410.24164](https://arxiv.org/abs/2410.24164)) · Reed et al. 2022, Gato ([2205.06175](https://arxiv.org/abs/2205.06175))

---

## 8. AI for maths and science

*Feeds T1 at the top end ("Virtuoso" level).*

**The idea.** If AI can produce *new* knowledge (proofs, discoveries), it is beyond imitation. This is also the main way AGI could speed up science, and AI research itself.

**Where it stands.**
- **AlphaFold** (protein structures) won a share of the 2024 Nobel Prize in Chemistry.
- **AlphaEvolve** (Google DeepMind, 2025) used language models plus evolutionary search to find new algorithms, including a faster method for 4×4 complex matrix multiplication.
- **FrontierMath** (Epoch, 2024) tests research-level maths. Its hardest tier, Tier 4, was revised in June 2026 (v2, 43 problems). Aggregators report scores above 80% (UNVERIFIED).
- **FrontierMath: Erdős** (Sept 2026) uses *open* research problems. GPT-6 Astra solved 2 of 68, and no earlier model had solved any (Epoch).
- **Automating AI R&D** is now a named risk category in METR's work (Oct 2026). Benchmarks such as RE-Bench, MLE-bench and PaperBench measure parts of it.

**What is still missing.** Choosing *which* problems matter (research taste), running long experiments that fail in messy ways, and checking results without a verifier.

**Read first.** Glazer et al. 2024, FrontierMath ([2411.04872](https://arxiv.org/abs/2411.04872)) · Novikov et al. 2025, AlphaEvolve ([2506.13131](https://arxiv.org/abs/2506.13131)) · Wijk et al. 2024, RE-Bench ([2411.15114](https://arxiv.org/abs/2411.15114)) · Lu et al. 2024, The AI Scientist ([2408.06292](https://arxiv.org/abs/2408.06292))

---

## 9. Safety, alignment and control

*Feeds T5. It also decides whether reaching AGI goes well.*

**The idea.**
- *Alignment*: the system tries to do what we actually want.
- *Control*: even if it is not aligned, we can stop it from causing harm.
- *Interpretability*: we can see what it is doing inside.

As systems grow more capable and autonomous, all three get harder and matter more.

**Where it stands.**
- **The main training methods.** RLHF (Ouyang et al. 2022) and Constitutional AI (Bai et al. 2022).
- **Worrying behaviours have been shown in lab settings:**
  - *Sleeper agents*: hidden behaviours that survive safety training (Hubinger et al. 2024).
  - *Alignment faking*: a model behaves differently when it believes it is being trained (Greenblatt et al. 2024).
  - *Reward hacking and cheating* on agentic tasks (METR 2026).
- **Real-world incidents in 2026:** cyber capabilities strong enough that Mythos Preview was gated (Apr), and the OpenAI–Hugging Face agent incident (Jul).
- **Interpretability** moved from toy models to finding millions of features in production models (Anthropic, *Scaling Monosemanticity*, 2024).
- **External assessment is growing.** METR published risk assessments of GPT-5.6 Sol (Jun 2026) and Claude Opus 5.5 (Sept 2026), and in Oct 2026 proposals for how assessors should check alignment, monitoring and AI-R&D acceleration.

**What is still missing.**
1. A way to *verify* alignment rather than just test for bad behaviour.
2. Oversight of systems smarter than the overseer ("scalable oversight", "weak-to-strong").
3. Monitoring of internal agents at scale.

**Read first.** Amodei et al. 2016, Concrete Problems ([1606.06565](https://arxiv.org/abs/1606.06565)) · Hubinger et al. 2024, Sleeper Agents ([2401.05566](https://arxiv.org/abs/2401.05566)) · Greenblatt et al. 2024, Alignment Faking ([2412.14093](https://arxiv.org/abs/2412.14093)) · Greenblatt et al. 2023, AI Control ([2312.06942](https://arxiv.org/abs/2312.06942)) · Burns et al. 2023, Weak-to-Strong ([2312.09390](https://arxiv.org/abs/2312.09390))

---

## 10. The measurement problem

*Affects every test.*

**The idea.** Benchmarks are how the field sees progress. But they *saturate* (top scores near 100% say nothing more), they *leak* (test items end up in training data), and they reward *narrow tricks*.

**Where it stands.**
- **Benchmarks saturate fast.** MMLU (2020) saturated by 2024. GPQA (2023) and SWE-bench Verified were near the ceiling by 2025–26. ARC-AGI-2 (2025) was near saturation by late 2026. Benchmark lifetimes have shrunk from years to months.
- **The field's answers:**
  1. *Harder static tests*: Humanity's Last Exam, FrontierMath Tier 4.
  2. *Open problems with no known answer*: FrontierMath: Erdős.
  3. *Interactive and new environments*: ARC-AGI-3.
  4. *Length-based measures*: METR time horizon.
  5. *Aggregate indices*: Epoch ECI.
  6. *Real-job tasks*: OpenAI's GDPval (2025), which grades model output against professionals' work.
- **Harness matters.** On ARC-AGI-3, the same model scores 62.7% or 99.9% depending on the scaffold. Any number without its harness and settings is not comparable.

**What is still missing.** Benchmarks for T4 (learning on the job) and T5 (reliability over many runs). A clean human baseline for long, real tasks. Evaluations that labs cannot optimise against.

**Read first.** Hendrycks et al. 2020, MMLU ([2009.03300](https://arxiv.org/abs/2009.03300)) · Phan et al. 2025, Humanity's Last Exam ([2501.14249](https://arxiv.org/abs/2501.14249)) · Rein et al. 2023, GPQA ([2311.12022](https://arxiv.org/abs/2311.12022)) · Schaeffer et al. 2023, emergence as a mirage ([2304.15004](https://arxiv.org/abs/2304.15004))

---

## 11. Compute, economics and forecasts

**The idea.** AGI timing depends on money, chips and power as much as on ideas. Forecasts help, but they move with every big release.

**Where it stands.**
- **Investment.** Frontier labs and hyperscalers are building gigawatt-scale data centres. Training compute for frontier models has grown by about 4–5× per year (Epoch AI).
- **The open-weights gap.** Open models trail the closed frontier by about 9 ECI points, roughly half a year (Epoch, Oct 2026). The best open model is Kimi K3 (Moonshot), and DeepSeek is close behind.
- **Forecasts.**
  - Metaculus runs two community questions ("weak" and "strong" AGI). Check the live pages, because the values move.
  - *AI 2027* (Kokotajlo et al., 2025) gave a detailed fast-takeoff scenario. The [AI 2027 tracker](https://ai2027-tracker.com/) checks its predictions against reality.
  - Lab leaders have publicly suggested late-2020s timelines for "powerful AI".

**What is still missing.** Good evidence on how much AI is *actually* speeding up the economy and AI research itself. METR's Oct 2026 note on assessing AI-R&D acceleration is a start.

**Read first.** Sevilla et al. 2022, compute trends ([2202.05924](https://arxiv.org/abs/2202.05924)) · [Epoch AI data hub](https://epoch.ai/data) · [AI 2027](https://ai-2027.com/) · Amodei 2024, [Machines of Loving Grace](https://darioamodei.com/machines-of-loving-grace)

---

## 12. Competing views of the path to AGI

The field does not agree on *how* AGI will be built. Knowing the main camps helps you read every new result.

| View | Main voices | Claim | What would prove it wrong |
|---|---|---|---|
| **Scale plus RL is enough** | Most frontier labs | Bigger models, plus reinforcement learning on more environments, plus agent scaffolds will reach AGI | Progress on T3 or T4 stalls despite rising compute |
| **We need world models** | LeCun; JEPA line | Next-token prediction cannot give grounded understanding or planning; you need models that predict the world in an abstract space | Text-first models pass T2 and T3 on physical-world tasks |
| **Learning efficiency is the core** | Chollet; ARC Prize | Without efficient skill acquisition it is memorisation, not intelligence | Systems that learn as efficiently as humans still fail real jobs (or the reverse) |
| **Learning from experience** | Sutton & Silver | The next era is agents learning mainly from their own interaction rather than from human data | Human-data-trained systems pass T4 without learning from experience |
| **Neuro-symbolic** | Marcus and others | Robust reasoning needs explicit symbols and structure, not only neural nets | Pure neural systems reach high reliability (T5) on reasoning |

**This repo's stance:** it takes no side. The five tests are built so that each camp can be checked against the same evidence.

---

*Corrections are welcome: [open an issue](https://github.com/thesvj/agi-tracker/issues) with a primary source.*
