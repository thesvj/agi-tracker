# Memory and continual learning

By the end of this module you should be able to explain why current models don't learn from deployment, describe the main research approaches, and say why this may be the last obstacle. T4 is the test with the least progress, and the AGI Score paper names long-term memory storage as the critical deficit of current systems.

## Main ideas

An AI system has three kinds of memory. Its weights change slowly and permanently, and only through training. Its context window is fast but temporary, and is wiped at the end of each session. External memory consists of notes, files and retrieval that a tool saves and loads back in.

Catastrophic forgetting happens when training on new data overwrites old skills. Research has tried several fixes. EWC protects the weights that matter most for old tasks. Replay mixes old data in with the new. Test-time training updates a small part of the model while it works. Titans adds a learned memory module. MemGPT has the agent manage its own memory.

Labs are cautious because a model that changes after release is harder to evaluate and to keep safe. Sutton and Silver (2025) argue that future agents should learn mainly from their own streams of experience instead of from a fixed set of human data.

## Reading

Start with these:

1. Kirkpatrick et al. 2017, EWC ([1612.00796](https://arxiv.org/abs/1612.00796)).
2. Packer et al. 2023, MemGPT ([2310.08560](https://arxiv.org/abs/2310.08560)).
3. Hendrycks et al. 2025 ([2510.18212](https://arxiv.org/abs/2510.18212)), the memory domains.

Further reading:

4. Sun et al. 2024, test-time training layers ([2407.04620](https://arxiv.org/abs/2407.04620)).
5. Behrouz et al. 2024, Titans ([2501.00663](https://arxiv.org/abs/2501.00663)).
6. Silver and Sutton 2025, *Welcome to the Era of Experience*, an essay you can find by searching its title.

## Exercise

On paper, design the "first month at work" benchmark described on the [Ideas](../ideas.md) page. Decide what the job is, how you will measure improvement, how you will check that old skills are kept, and what the human baseline will be.

## Questions

1. Why isn't a context window of a million tokens the same as learning?
2. What is catastrophic forgetting, and which method deals with it by protecting important weights?
3. Give one safety reason why models that update themselves are hard to deploy.
