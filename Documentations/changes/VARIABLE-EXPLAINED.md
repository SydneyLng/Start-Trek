# Variables Explained

This document provides practical explanations of key variables used in this project.

## Table of Contents

- [learning_rate](#learning_rate)
- [gamma](#gamma)
- [batch_size](#batch_size)
- [buffer_size](#buffer_size)
- [target_update_freq](#target_update_freq)
- [epsilon_start](#epsilon_start)
- [epsilon_end](#epsilon_end)
- [epsilon_decay](#epsilon_decay)
- [reward_clipping](#reward_clipping)
- [obs_normalization](#obs_normalization)
- [seed](#seed)

## learning_rate
Controls how large each gradient update step is.
Too high can destabilize training; too low can slow learning.

## gamma
Discount factor for future rewards.
Higher values prioritize long-term rewards; lower values emphasize immediate rewards.

## batch_size
Number of samples drawn from replay buffer per optimization step.
Larger batches often stabilize gradients but increase compute cost.

## buffer_size
Maximum number of transitions stored in replay memory.
Larger buffers improve diversity but may keep stale experience longer.

## target_update_freq
How often target network parameters are updated.
Frequent updates can reduce lag but may reduce stability benefits.

## epsilon_start
Initial exploration rate for epsilon-greedy policy.

## epsilon_end
Minimum exploration rate after decay.

## epsilon_decay
Speed of exploration decay across steps/episodes.
Fast decay can lead to early exploitation; slow decay can delay convergence.

## reward_clipping
Whether rewards are clipped to a bounded range.
Can stabilize training but may remove reward magnitude information.

## obs_normalization
Whether observations are normalized before entering the model.
Can improve optimization by keeping feature scales consistent.

## seed
Random seed controlling reproducibility for environment and training components.