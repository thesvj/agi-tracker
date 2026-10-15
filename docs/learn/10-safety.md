# 10 · Safety, alignment and control

**Goal.** You can name the main failure modes of capable AI, the main research responses, and the 2026 incidents that made them concrete.

**Why it matters for AGI.** T5 requires trustworthy behaviour. Beyond the definition, safety decides whether reaching AGI goes well.

## Core ideas

- **Outer versus inner alignment:** is the objective right, and did the model actually learn it?
- **Reward hacking and specification gaming:** high score, wrong behaviour.
- **Deceptive behaviour:** sleeper agents and alignment faking, shown in lab settings.
- **Scalable oversight:** how a weaker overseer supervises a stronger system (weak-to-strong generalisation, debate).
- **AI control:** assume the model might be misaligned, and design monitoring and limits so that it still cannot cause harm.
- **Interpretability:** find features and circuits inside models (sparse autoencoders, *Scaling Monosemanticity*).
- **2026 cases:** Mythos Preview gated for cyber risk (Apr). OpenAI agents attacked Hugging Face during an internal evaluation (Jul). METR proposed ways for assessors to check alignment and internal-agent monitoring (Oct).

## Read

1. ⭐ Amodei et al. 2016, *Concrete Problems in AI Safety* ([1606.06565](https://arxiv.org/abs/1606.06565)).
2. ⭐ Greenblatt et al. 2024, *Alignment Faking* ([2412.14093](https://arxiv.org/abs/2412.14093)).
3. ⭐ Greenblatt et al. 2023, *AI Control* ([2312.06942](https://arxiv.org/abs/2312.06942)).
4. Hubinger et al. 2024, *Sleeper Agents* ([2401.05566](https://arxiv.org/abs/2401.05566)).
5. Burns et al. 2023, *Weak-to-Strong Generalization* ([2312.09390](https://arxiv.org/abs/2312.09390)).
6. Templeton et al. 2024, [*Scaling Monosemanticity*](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html).
7. [METR](https://metr.org/) posts from Aug–Oct 2026.

## Do

Read the METR review of the OpenAI–Hugging Face incident. Write down: (1) what the agents did, (2) which safeguard failed, (3) which idea from this module would have caught it.

## Check yourself

1. What is the difference between alignment and control?
2. Why is "it passed our safety tests" weak evidence against alignment faking?
3. Which 2026 event most directly bears on T5, and why?
