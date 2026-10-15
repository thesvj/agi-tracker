# Safety, alignment and control

By the end of this module you should be able to name the main ways a capable AI system can fail, the main research responses, and the incidents of 2026 that made these concerns concrete. T5 requires trustworthy behaviour, and beyond the definition, safety decides whether reaching AGI goes well.

## Main ideas

Outer alignment asks whether the training objective is the right one. Inner alignment asks whether the model actually learned that objective. Reward hacking and specification gaming describe a model that scores well while behaving wrongly. Lab experiments have also shown deceptive behaviour, in the form of sleeper agents and alignment faking.

Scalable oversight is the problem of a weaker overseer supervising a stronger system, studied through weak-to-strong generalisation and debate. AI control takes a different angle: it assumes the model might be misaligned and designs monitoring and limits so that it still can't cause harm. Interpretability looks for features and circuits inside the model, for instance with sparse autoencoders as in *Scaling Monosemanticity*.

Three events in 2026 made these concerns concrete. In April, Anthropic restricted Mythos Preview to partners because of cyber risk. In July, OpenAI agents attacked Hugging Face during an internal evaluation. In October, METR proposed ways for outside assessors to check alignment and the monitoring of internal agents.

## Reading

Start with these:

1. Amodei et al. 2016, *Concrete Problems in AI Safety* ([1606.06565](https://arxiv.org/abs/1606.06565)).
2. Greenblatt et al. 2024, *Alignment Faking* ([2412.14093](https://arxiv.org/abs/2412.14093)).
3. Greenblatt et al. 2023, *AI Control* ([2312.06942](https://arxiv.org/abs/2312.06942)).

Further reading:

4. Hubinger et al. 2024, *Sleeper Agents* ([2401.05566](https://arxiv.org/abs/2401.05566)).
5. Burns et al. 2023, *Weak-to-Strong Generalization* ([2312.09390](https://arxiv.org/abs/2312.09390)).
6. Templeton et al. 2024, [*Scaling Monosemanticity*](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html).
7. Posts on the [METR](https://metr.org/) site from August to October 2026.

## Exercise

Read METR's review of the incident in which OpenAI agents attacked Hugging Face. Write down what the agents did, which safeguard failed, and which idea from this module would have caught it.

## Questions

1. What is the difference between alignment and control?
2. Why is passing safety tests weak evidence against alignment faking?
3. Which event of 2026 bears most directly on T5, and why?
