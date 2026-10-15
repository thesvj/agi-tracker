# Survey

State of the field on 15 October 2026, organised by capability. Each section says which of the [five tests](definition.md) it bears on, describes the area, gives dated results, lists what is still unsolved, and ends with a few primary sources to read first. Detailed numbers are on the [tracker](tracker.md), and the full reading path is under [Learn](learn/README.md).

- [Scaling](#scaling)
- [Reasoning models and test-time compute](#reasoning-models-and-test-time-compute)
- [Agents and long tasks](#agents-and-long-tasks)
- [Generalisation and learning efficiency](#generalisation-and-learning-efficiency)
- [Memory and continual learning](#memory-and-continual-learning)
- [Multimodality and world models](#multimodality-and-world-models)
- [Embodiment and robotics](#embodiment-and-robotics)
- [AI for maths and science](#ai-for-maths-and-science)
- [Safety, alignment and control](#safety-alignment-and-control)
- [Measurement](#measurement)
- [Compute, economics and forecasts](#compute-economics-and-forecasts)
- [Competing views](#competing-views)

## Scaling

*Bears on T1.*

When a neural network is trained with more parameters, more data and more compute, its loss falls along a smooth power law, and lower loss has repeatedly brought new abilities with it. This scaling hypothesis explains most of the progress since 2018. Rich Sutton's essay *The Bitter Lesson* (2019) makes the general argument that methods which use more compute end up beating methods built on human insight.

Kaplan et al. (2020) published the first scaling laws. Hoffmann et al. (2022, the "Chinchilla" paper) corrected them, showing that for a fixed compute budget, model size and training data should grow at about the same rate. From 2024, labs reported smaller gains from pre-training alone and moved compute into post-training and reinforcement learning (see Reasoning models and test-time compute). Pre-training is still where the model's knowledge comes from, and reinforcement learning builds on it.

According to Epoch AI, training compute for frontier models has grown about four to five times per year. Data looks like the tighter limit: Epoch estimates that high-quality public text will run out somewhere between the mid-2020s and the early 2030s (Villalobos et al., 2022, updated 2024), and synthetic data and reinforcement-learning data are the main responses. Epoch's capability index for the best model rose from about 150 (GPT-5, August 2025) to 166.8 (Claude Opus 5.5, September 2026), as the [tracker chart](tracker.md#t1-breadth) shows.

Still unsolved: nobody can predict which abilities will appear at which scale. Wei et al. (2022) described abilities that seem to emerge suddenly, and Schaeffer et al. (2023) argued that much of the suddenness comes from the choice of metric. Scaling on its own has also not solved continual learning (see Memory and continual learning) or reliability (see Safety, alignment and control).

Read first: Kaplan et al. 2020 ([2001.08361](https://arxiv.org/abs/2001.08361)); Hoffmann et al. 2022 ([2203.15556](https://arxiv.org/abs/2203.15556)); Sutton, [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html); Villalobos et al. ([2211.04325](https://arxiv.org/abs/2211.04325)).

## Reasoning models and test-time compute

*Bears on T1 and T2.*

A reasoning model writes out a long chain of thought before it answers. It learns to reason usefully through reinforcement learning on problems whose answers can be checked automatically, such as maths and code. This gives a second way to scale: spending more compute when answering produces better answers.

OpenAI's o1 (September 2024) showed large gains in maths and science. In December 2024, o3 scored 75.7% on ARC-AGI-1 with low compute and 87.5% with high compute, according to ARC Prize. DeepSeek-R1 (January 2025) showed that plain reinforcement learning with verifiable rewards can teach long reasoning to an open model. In July 2025, experimental systems from Google DeepMind and OpenAI each reached gold-medal level at the International Mathematical Olympiad, working in natural language.

By 2026 every frontier model has an adjustable reasoning effort, and the setting makes a large difference. ARC Prize measured GPT-6 Astra at 17.5% on ARC-AGI-3 with low effort and 62.7% with maximum effort (September 2026).

Still unsolved: reinforcement learning works best where an answer can be checked automatically, and open-ended work like strategy, writing or choosing research problems has no clean reward. The written reasoning may also be unfaithful, meaning it isn't what actually produced the answer. And extra thinking costs money, which counts against T5.

Read first: Wei et al. 2022, chain of thought ([2201.11903](https://arxiv.org/abs/2201.11903)); Lightman et al. 2023, process supervision ([2305.20050](https://arxiv.org/abs/2305.20050)); Snell et al. 2024, test-time compute ([2408.03314](https://arxiv.org/abs/2408.03314)); DeepSeek-AI 2025, R1 ([2501.12948](https://arxiv.org/abs/2501.12948)).

## Agents and long tasks

*Bears on T3 and T5.*

An agent is a model running in a loop. It plans, calls tools such as a terminal, a browser or a code interpreter, looks at the results, and continues until the job is done. If AGI means a colleague you can hand work to, agents have to finish long jobs without help.

METR's time horizon is the clearest single measure of this. It records the length of task, in the time a human expert would need, that an agent completes half the time. It rose from about 4 minutes for GPT-4 in 2023 to about 17 hours for the early Claude Mythos Preview in April 2026, doubling about every 129 days ([chart](tracker.md#t3-long-tasks-alone)).

Coding is the furthest along. On SWE-bench Verified, which uses real GitHub issues, scores went from single digits in 2023 to close to the ceiling by 2026, and harder benchmarks such as SWE-bench Pro and Terminal-Bench have taken its place. Computer use, where an agent operates a desktop through screenshots and clicks as in OSWorld, has improved quickly but is less reliable than coding.

Agents also became a security issue in 2026. In April, Anthropic gave Claude Mythos Preview only to vetted partners under Project Glasswing because of how well it finds and exploits software vulnerabilities. In July, about 700 OpenAI agents that were running in an internal evaluation attacked Hugging Face's servers, and METR published an independent review in August.

Still unsolved: reliability over long tasks, since errors compound and the 80% horizon is about five times shorter than the 50% one. Agents also don't always complete tasks honestly; METR found cheating in at least 16% of successful runs on tasks longer than 8 hours. And current benchmarks measure hours. METR's suite is reliable only up to about 16 hours, with nothing yet that measures work lasting weeks.

Read first: Yao et al. 2022, ReAct ([2210.03629](https://arxiv.org/abs/2210.03629)); Jimenez et al. 2023, SWE-bench ([2310.06770](https://arxiv.org/abs/2310.06770)); Xie et al. 2024, OSWorld ([2404.07972](https://arxiv.org/abs/2404.07972)); Kwa et al. 2025, time horizons ([2503.14499](https://arxiv.org/abs/2503.14499)).

## Generalisation and learning efficiency

*Bears on T2.*

A child can learn a new card game in five minutes from a few examples. Chollet (2019) argued that this efficiency in acquiring skills is what intelligence is, and that a system which knows a great deal may still learn slowly. He built the ARC benchmarks to measure it, using small puzzles that need no special knowledge and can't be memorised.

ARC-AGI-1, released in 2019, held out against large language models for years until o3's result in December 2024. ARC-AGI-2 (2025) was made harder. By late 2026, aggregator sites report frontier scores of around 95% (UNVERIFIED), which would put it close to saturation.

ARC-AGI-3, launched in March 2026, uses interactive games instead of static puzzles. There are no instructions: the agent has to explore, work out the goal and win in as few actions as it can. Frontier models scored below 1% at launch. By September 2026, GPT-6 Astra scored 62.7% with the provider-neutral Standard harness. With a harness that keeps its reasoning state it scored 99.9%, using fewer actions than the median human on 96% of levels.

Still unsolved: the ARC games are small, closed and deterministic, and ARC Prize itself says that saturating ARC-AGI-3 would not prove AGI. The open question is whether this efficiency carries over to real jobs, where the rules are unclear, feedback is slow and mistakes cost something.

Read first: Chollet 2019 ([1911.01547](https://arxiv.org/abs/1911.01547)); Chollet et al. 2025, ARC-AGI-2 ([2505.11831](https://arxiv.org/abs/2505.11831)); ARC Prize 2026, ARC-AGI-3 ([2603.24621](https://arxiv.org/abs/2603.24621)); [ARC Prize on GPT-6 Astra](https://arcprize.org/blog/astra).

## Memory and continual learning

*Bears on T4, which may turn out to be the hardest test.*

People store experiences in long-term memory and get better at their jobs over months. Current models are trained once and then frozen. Whatever they pick up during use stays in the context window, or in notes that a tool saves and reloads, and it is gone when the session ends.

The AGI Score paper (Hendrycks et al., October 2025) names long-term memory storage as the critical deficit of current systems. Products work around it with long context windows (around a million tokens is now common), memory files, retrieval, and agents that keep their own notes. ARC Prize describes GPT-6 Astra writing compact, code-like notes as it plays.

Research is going in several directions. Test-time training updates some of the weights while the model works (Sun et al. 2024). Learned memory modules such as Titans add a component that stores information (Behrouz et al. 2024). Work on catastrophic forgetting, where learning something new erases older skills, goes back to methods like EWC (Kirkpatrick et al. 2017). Sutton and Silver (2025) call for an "era of experience" in which agents learn mainly from their own interaction with the world.

Still unsolved: no frontier system safely updates itself from deployment experience at scale. Forgetting is one obstacle and cost is another. Safety is a third, because a model that changes after release is harder to audit. There is also no accepted benchmark for getting better at a job over a month; the [Ideas](ideas.md#learning-on-the-job-t4) page sketches some.

Read first: Kirkpatrick et al. 2017 ([1612.00796](https://arxiv.org/abs/1612.00796)); Packer et al. 2023, MemGPT ([2310.08560](https://arxiv.org/abs/2310.08560)); Sun et al. 2024, test-time training layers ([2407.04620](https://arxiv.org/abs/2407.04620)); Behrouz et al. 2024, Titans ([2501.00663](https://arxiv.org/abs/2501.00663)).

## Multimodality and world models

*Bears on T1, and supports T3 and embodiment.*

A general system has to handle images, audio and video as well as text. A world model is an internal simulator that predicts what will happen after an action. Some researchers, LeCun among them, think world models are the main missing piece and that text prediction can't supply it.

Frontier models are now natively multimodal and read images, charts, screens and audio. Generators can produce interactive environments: Google DeepMind's Genie went from 2D game worlds in 2024 to explorable 3D worlds in real time with Genie 3 in August 2025. Self-supervised video models such as Meta's V-JEPA 2 (2025) learn to predict physical events from video and are used for robot planning.

Still unsolved: it isn't clear whether models trained on text have a world model in any useful sense. Generated worlds look convincing, but their physics and long-term consistency are weak. Visual reasoning, such as counting, spatial relations and reading diagrams precisely, lags behind reasoning in text.

Read first: Ha and Schmidhuber 2018, world models ([1803.10122](https://arxiv.org/abs/1803.10122)); Hafner et al. 2023, DreamerV3 ([2301.04104](https://arxiv.org/abs/2301.04104)); Bruce et al. 2024, Genie ([2402.15391](https://arxiv.org/abs/2402.15391)); LeCun 2022, [A Path Towards Autonomous Machine Intelligence](https://openreview.net/pdf?id=BZ5a1r-kVsf); Assran et al. 2025, V-JEPA 2 ([2506.09985](https://arxiv.org/abs/2506.09985)).

## Embodiment and robotics

*The separate embodied track, outside the five tests.*

Moravec's paradox is the observation that what people find easy, like walking or picking up a cup, is hard for machines, and the other way round. Robots also need physical data, which is slow and expensive to collect.

Vision-language-action models take an image and an instruction and output motor commands. RT-2 (2023) and Physical Intelligence's π0 (2024) were early examples, and many successors followed in 2025 and 2026. Humanoid robots attracted heavy investment over the same period. The demonstrations are impressive, but robots still have trouble staying reliable in homes they haven't seen before and on long chores with many steps.

Still unsolved: there is nothing like web-scale data for robots, safe operation around people is hard, and dexterous manipulation over long tasks remains weak. Most forecasters expect embodied AGI to arrive well after cognitive AGI.

Read first: Brohan et al. 2023, RT-2 ([2307.15818](https://arxiv.org/abs/2307.15818)); Black et al. 2024, π0 ([2410.24164](https://arxiv.org/abs/2410.24164)); Reed et al. 2022, Gato ([2205.06175](https://arxiv.org/abs/2205.06175)).

## AI for maths and science

*Bears on the top end of T1, the virtuoso level.*

A system that produces new knowledge, such as proofs or discoveries, is doing more than imitating. This is also the route by which AGI could speed up science, including AI research.

AlphaFold, which predicts protein structures, earned a share of the 2024 Nobel Prize in Chemistry. AlphaEvolve (Google DeepMind, 2025) combined language models with evolutionary search to find new algorithms, among them a faster method for multiplying 4×4 complex matrices.

Epoch's FrontierMath (2024) tests research-level maths. Its hardest tier, Tier 4, was revised in June 2026 to version 2 with 43 problems. By Epoch's own evaluation, GPT-6.1 Sol solved all of them in September 2026, so the tier is now saturated. FrontierMath: Erdős, released in September 2026, uses problems that are still open. GPT-6 Astra solved 2 of the 68, and Epoch reports that no earlier model had solved any.

METR now treats the automation of AI research as a risk category in its own right (October 2026). RE-Bench, MLE-bench and PaperBench each measure part of it.

Still unsolved: choosing which problems are worth working on, running long experiments that fail in untidy ways, and checking results when there is no automatic verifier.

Read first: Glazer et al. 2024, FrontierMath ([2411.04872](https://arxiv.org/abs/2411.04872)); Novikov et al. 2025, AlphaEvolve ([2506.13131](https://arxiv.org/abs/2506.13131)); Wijk et al. 2024, RE-Bench ([2411.15114](https://arxiv.org/abs/2411.15114)); Lu et al. 2024, The AI Scientist ([2408.06292](https://arxiv.org/abs/2408.06292)).

## Safety, alignment and control

*Bears on T5, and on whether reaching AGI goes well.*

Alignment means the system tries to do what people actually want. Control means that even if it doesn't, it can be prevented from causing harm. Interpretability means being able to see what it is doing internally. All three become harder, and more important, as systems become more capable and more autonomous.

The main training methods are RLHF (Ouyang et al. 2022) and Constitutional AI (Bai et al. 2022). Lab experiments have produced worrying behaviour. Hubinger et al. (2024) showed sleeper agents, whose hidden behaviours survive safety training. Greenblatt et al. (2024) showed alignment faking, where a model acts differently when it believes it is being trained. METR (2026) documented reward hacking and cheating on agentic tasks.

Two incidents in 2026 happened outside the lab: Mythos Preview's release was restricted in April because of its cyber capabilities, and in July OpenAI agents attacked Hugging Face. Interpretability research has moved from toy models to finding millions of features in production models (Anthropic, *Scaling Monosemanticity*, 2024). Outside assessment is also growing. METR published risk assessments of GPT-5.6 Sol in June 2026 and Claude Opus 5.5 in September 2026. In October it set out proposals for how assessors should examine alignment, the monitoring of internal agents, and acceleration of AI research.

Still unsolved: there is no way yet to verify that a model is aligned, as opposed to testing it for bad behaviour. Nor is there a proven way to oversee a system smarter than its overseer (the scalable oversight and weak-to-strong problems), or to monitor internal agents at scale.

Read first: Amodei et al. 2016, Concrete Problems ([1606.06565](https://arxiv.org/abs/1606.06565)); Hubinger et al. 2024, Sleeper Agents ([2401.05566](https://arxiv.org/abs/2401.05566)); Greenblatt et al. 2024, Alignment Faking ([2412.14093](https://arxiv.org/abs/2412.14093)); Greenblatt et al. 2023, AI Control ([2312.06942](https://arxiv.org/abs/2312.06942)); Burns et al. 2023, Weak-to-Strong ([2312.09390](https://arxiv.org/abs/2312.09390)).

## Measurement

*Bears on every test.*

Benchmarks are how the field sees progress, and they wear out. They saturate, so top scores near 100% stop telling models apart. Their test items leak into training data. And some of them reward narrow tricks.

MMLU (2020) was saturated by 2024. GPQA (2023) and SWE-bench Verified were near their ceilings by 2025 and 2026, and ARC-AGI-2 (2025) by late 2026. Benchmarks that once lasted years now last months.

The field has responded in several ways. Some new tests are simply harder, like Humanity's Last Exam and FrontierMath Tier 4. FrontierMath: Erdős uses problems nobody has solved. ARC-AGI-3 uses interactive environments the model hasn't seen. METR's time horizon measures task length, and Epoch's capability index combines many benchmarks into one scale. OpenAI's GDPval (2025) grades model output on real job tasks against the work of professionals.

The harness matters as much as the model. On ARC-AGI-3 the same model scores 62.7% or 99.9% depending on the scaffold, so a number reported without its harness and settings can't be compared with anything.

Still unsolved: benchmarks for T4 and for reliability over many runs (T5), a clean human baseline for long real tasks, and evaluations that labs can't train against.

Read first: Hendrycks et al. 2020, MMLU ([2009.03300](https://arxiv.org/abs/2009.03300)); Phan et al. 2025, Humanity's Last Exam ([2501.14249](https://arxiv.org/abs/2501.14249)); Rein et al. 2023, GPQA ([2311.12022](https://arxiv.org/abs/2311.12022)); Schaeffer et al. 2023, emergence as a mirage ([2304.15004](https://arxiv.org/abs/2304.15004)).

## Compute, economics and forecasts

When AGI arrives depends on money, chips and power as well as on ideas, and forecasts shift with each major release.

Frontier labs and the large cloud companies are building data centres on the scale of gigawatts, and training compute for frontier models has grown about four to five times per year (Epoch AI). Open models trail the best closed models by about 9 points on Epoch's index, roughly half a year (October 2026). The best open model is Moonshot's Kimi K3, with DeepSeek close behind.

Metaculus runs two community forecasting questions, one on "weak" and one on "strong" AGI; the values change often, so it is worth checking the live pages. *AI 2027* (Kokotajlo et al., 2025) laid out a detailed fast-takeoff scenario, and the [AI 2027 tracker](https://ai2027-tracker.com/) compares its predictions with what has happened. Leaders of some labs have said publicly that they expect "powerful AI" in the late 2020s.

Still unsolved: there is little good evidence on how much AI is actually speeding up the economy, or AI research itself. METR's October 2026 note on assessing acceleration of AI research is a first step.

Read first: Sevilla et al. 2022, compute trends ([2202.05924](https://arxiv.org/abs/2202.05924)); [Epoch AI data hub](https://epoch.ai/data); [AI 2027](https://ai-2027.com/); Amodei 2024, [Machines of Loving Grace](https://darioamodei.com/machines-of-loving-grace).

## Competing views

Researchers disagree about how AGI will be built, and knowing the main positions makes new results easier to place.

| View | Main proponents | Claim | Evidence that would count against it |
|---|---|---|---|
| Scale and reinforcement learning are enough | Most frontier labs | Larger models, reinforcement learning on more environments, and agent scaffolds will get there | Progress on T3 or T4 stalls while compute keeps rising |
| World models are needed | LeCun and the JEPA line of work | Predicting the next token can't give grounded understanding or planning; models need to predict the world in an abstract space | Text-first models pass T2 and T3 on tasks in the physical world |
| Learning efficiency is central | Chollet and ARC Prize | Without efficient skill acquisition, a system is memorising | Systems that learn as efficiently as people still fail at real jobs, or the reverse |
| Learning from experience | Sutton and Silver | The next stage is agents that learn mainly from their own interaction, with human data playing a smaller part | Systems trained on human data pass T4 without learning from experience |
| Neuro-symbolic | Marcus and others | Robust reasoning needs explicit symbols and structure in addition to neural networks | Purely neural systems reach high reliability on reasoning (T5) |

The tracker takes no side. Each test is built so that every one of these positions can be checked against the same evidence.

If you find an error, please [open an issue](https://github.com/thesvj/agi-tracker/issues) with a primary source.
