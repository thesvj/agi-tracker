# Seminal papers

The papers that anyone starting work on general AI should read. Each one either started a line of work that the field still follows or changed how people think about the problem. They are grouped by topic and sorted by year within each group. Newer results are in the [survey](survey.md), and the [study path](learn/README.md) adds exercises around many of these papers.

If you only have time for ten, start with Turing 1950, Sutton 2019, Chollet 2019, Vaswani et al. 2017, Kaplan et al. 2020, Hoffmann et al. 2022, Ouyang et al. 2022, Wei et al. 2022 (chain of thought), DeepSeek-AI 2025 and Kwa et al. 2025.

## What intelligence is and how to measure it

| Year | Paper | Why read it |
|---|---|---|
| 1950 | Turing, [Computing Machinery and Intelligence](https://doi.org/10.1093/mind/LIX.236.433) | Asks whether machines can think and proposes the imitation game as a test. |
| 1955 | McCarthy et al., [A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence](http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf) | The proposal that named the field and set out its first goals. |
| 2007 | Legg and Hutter, Universal Intelligence ([0712.3329](https://arxiv.org/abs/0712.3329)) | A formal definition of intelligence as the ability to achieve goals across many environments. |
| 2016 | Lake et al., Building Machines That Learn and Think Like People ([1604.00289](https://arxiv.org/abs/1604.00289)) | Argues that human-like learning needs causal models, intuitive physics and fast learning from few examples. |
| 2019 | Chollet, On the Measure of Intelligence ([1911.01547](https://arxiv.org/abs/1911.01547)) | Defines intelligence as how efficiently a system learns new skills, and introduces ARC. |
| 2019 | Sutton, [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) | A one-page argument that general methods using more compute beat methods built on human knowledge. |
| 2020 | Hendrycks et al., MMLU ([2009.03300](https://arxiv.org/abs/2009.03300)) | The knowledge benchmark that tracked language models for four years. |
| 2023 | Bubeck et al., Sparks of Artificial General Intelligence ([2303.12712](https://arxiv.org/abs/2303.12712)) | An early, much-debated case that GPT-4 showed signs of general intelligence. |
| 2023 | Morris et al., Levels of AGI ([2311.02462](https://arxiv.org/abs/2311.02462)) | Grades AGI by performance and generality, in the style of levels for self-driving cars. |

## Deep learning foundations

| Year | Paper | Why read it |
|---|---|---|
| 1986 | Rumelhart, Hinton and Williams, [Learning representations by back-propagating errors](https://doi.org/10.1038/323533a0) | Backpropagation, the training method behind every model in this repo. |
| 2012 | Krizhevsky, Sutskever and Hinton, [ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) | AlexNet, the result that started the deep learning era. |
| 2013 | Mikolov et al., word2vec ([1301.3781](https://arxiv.org/abs/1301.3781)) | Showed that words can be represented as vectors that capture meaning. |
| 2015 | He et al., ResNet ([1512.03385](https://arxiv.org/abs/1512.03385)) | Residual connections, which made very deep networks trainable and are used in every transformer. |

## Language models and scaling

| Year | Paper | Why read it |
|---|---|---|
| 2014 | Bahdanau, Cho and Bengio, attention for translation ([1409.0473](https://arxiv.org/abs/1409.0473)) | Introduced attention, the idea the transformer is built on. |
| 2017 | Vaswani et al., Attention Is All You Need ([1706.03762](https://arxiv.org/abs/1706.03762)) | The transformer architecture. |
| 2018 | Devlin et al., BERT ([1810.04805](https://arxiv.org/abs/1810.04805)) | Showed that one pre-trained model can be fine-tuned for many tasks. |
| 2020 | Brown et al., GPT-3 ([2005.14165](https://arxiv.org/abs/2005.14165)) | Showed that a large enough model can learn tasks from a few examples in its prompt. |
| 2020 | Kaplan et al., Scaling Laws for Neural Language Models ([2001.08361](https://arxiv.org/abs/2001.08361)) | Loss falls as a smooth power law in parameters, data and compute. |
| 2022 | Hoffmann et al., Chinchilla ([2203.15556](https://arxiv.org/abs/2203.15556)) | Corrected the scaling laws: model size and data should grow together. |
| 2022 | Wei et al., Emergent Abilities of Large Language Models ([2206.07682](https://arxiv.org/abs/2206.07682)) | Abilities that seem to appear suddenly with scale. Read with Schaeffer et al. 2023 ([2304.15004](https://arxiv.org/abs/2304.15004)) for the counter-argument. |

## Post-training and alignment methods

| Year | Paper | Why read it |
|---|---|---|
| 2017 | Christiano et al., Deep Reinforcement Learning from Human Preferences ([1706.03741](https://arxiv.org/abs/1706.03741)) | The original method of training from human comparisons, later called RLHF. |
| 2022 | Ouyang et al., InstructGPT ([2203.02155](https://arxiv.org/abs/2203.02155)) | How RLHF turned GPT-3 into an assistant that follows instructions. |
| 2022 | Bai et al., Constitutional AI ([2212.08073](https://arxiv.org/abs/2212.08073)) | Replaced most human labels with AI feedback guided by written principles. |
| 2023 | Rafailov et al., DPO ([2305.18290](https://arxiv.org/abs/2305.18290)) | Trains on preference pairs directly, without a separate reward model. |

## Reasoning

| Year | Paper | Why read it |
|---|---|---|
| 2022 | Wei et al., Chain-of-Thought Prompting ([2201.11903](https://arxiv.org/abs/2201.11903)) | Asking a model to write out its steps improves multi-step answers. |
| 2022 | Zelikman et al., STaR ([2203.14465](https://arxiv.org/abs/2203.14465)) | A model improves its reasoning by training on its own correct solutions. |
| 2023 | Lightman et al., Let's Verify Step by Step ([2305.20050](https://arxiv.org/abs/2305.20050)) | Rewarding each correct step works better than rewarding only the final answer. |
| 2024 | Snell et al., Scaling LLM Test-Time Compute ([2408.03314](https://arxiv.org/abs/2408.03314)) | When spending more compute at answer time beats training a bigger model. |
| 2025 | DeepSeek-AI, DeepSeek-R1 ([2501.12948](https://arxiv.org/abs/2501.12948)) | The clearest public account of training a reasoning model with reinforcement learning. |

## Reinforcement learning, planning and world models

| Year | Paper | Why read it |
|---|---|---|
| 2013 | Mnih et al., Playing Atari with Deep Reinforcement Learning ([1312.5602](https://arxiv.org/abs/1312.5602)) | One network learned many games from pixels and score alone. |
| 2016 | Silver et al., [Mastering the game of Go with deep neural networks and tree search](https://doi.org/10.1038/nature16961) | AlphaGo, which combined learning with search to beat a world champion. |
| 2017 | Silver et al., AlphaZero ([1712.01815](https://arxiv.org/abs/1712.01815)) | Learned chess, shogi and Go from self-play with no human games. |
| 2018 | Ha and Schmidhuber, World Models ([1803.10122](https://arxiv.org/abs/1803.10122)) | An agent that learns a model of its environment and trains inside it. |
| 2019 | Schrittwieser et al., MuZero ([1911.08265](https://arxiv.org/abs/1911.08265)) | Planning with a learned model, without being told the rules. |
| 2022 | LeCun, [A Path Towards Autonomous Machine Intelligence](https://openreview.net/forum?id=BZ5a1r-kVsf) | The main proposal for AGI built on world models rather than language models. |
| 2023 | Hafner et al., DreamerV3 ([2301.04104](https://arxiv.org/abs/2301.04104)) | One world-model agent with fixed settings that works across many domains. |

## Learning, memory and generalisation

| Year | Paper | Why read it |
|---|---|---|
| 2017 | Finn, Abbeel and Levine, MAML ([1703.03400](https://arxiv.org/abs/1703.03400)) | Meta-learning: training a model so that it can learn new tasks quickly. |
| 2017 | Kirkpatrick et al., Overcoming catastrophic forgetting ([1612.00796](https://arxiv.org/abs/1612.00796)) | Why networks forget old skills when they learn new ones, and one fix. Central to T4. |
| 2020 | Lewis et al., Retrieval-Augmented Generation ([2005.11401](https://arxiv.org/abs/2005.11401)) | Giving a model access to documents at answer time instead of storing everything in weights. |

## Agents

| Year | Paper | Why read it |
|---|---|---|
| 2022 | Yao et al., ReAct ([2210.03629](https://arxiv.org/abs/2210.03629)) | The think, act, observe loop most agents still use. |
| 2023 | Schick et al., Toolformer ([2302.04761](https://arxiv.org/abs/2302.04761)) | A model that teaches itself when to call tools. |
| 2023 | Jimenez et al., SWE-bench ([2310.06770](https://arxiv.org/abs/2310.06770)) | Real GitHub issues as a test of software agents. |
| 2025 | Kwa et al., Measuring AI Ability to Complete Long Software Tasks ([2503.14499](https://arxiv.org/abs/2503.14499)) | METR's time horizon, the measure behind T3. |

## AI for science

| Year | Paper | Why read it |
|---|---|---|
| 2021 | Jumper et al., [Highly accurate protein structure prediction with AlphaFold](https://doi.org/10.1038/s41586-021-03819-2) | The first AI result to solve a long-standing scientific problem. |
| 2023 | Romera-Paredes et al., [Mathematical discoveries from program search with large language models](https://doi.org/10.1038/s41586-023-06924-6) | FunSearch, where a language model found new results in mathematics. |

## Safety and interpretability

| Year | Paper | Why read it |
|---|---|---|
| 2016 | Amodei et al., Concrete Problems in AI Safety ([1606.06565](https://arxiv.org/abs/1606.06565)) | Set out reward hacking, safe exploration and other problems in practical terms. |
| 2019 | Hubinger et al., Risks from Learned Optimization ([1906.01820](https://arxiv.org/abs/1906.01820)) | A trained model may pursue goals different from the one it was trained on. |
| 2022 | Elhage et al., Toy Models of Superposition ([2209.10652](https://arxiv.org/abs/2209.10652)) | Why single neurons are hard to interpret, and the start of much interpretability work. |
| 2023 | Burns et al., Weak-to-Strong Generalization ([2312.09390](https://arxiv.org/abs/2312.09390)) | Can a weaker supervisor control a stronger model? A first experiment. |
