import numpy as np
import gym
from collections import deque
from tensorboardX import SummaryWriter


class TensorboardSummaries(gym.Wrapper):
    """ Writes env summaries."""

    def __init__(self, env, prefix=None, running_mean_size=100, step_var=None):
        super(TensorboardSummaries, self).__init__(env)
        self.episode_counter = 0
        self.prefix = prefix or self.env.spec.id
        self.writer = SummaryWriter(f"logs/{self.prefix}")
        self.step_var = 0

        self.nenvs = getattr(self.env.unwrapped, "nenvs", 1)
        self.rewards = np.zeros(self.nenvs)
        self.had_ended_episodes = np.zeros(self.nenvs, dtype=np.bool)
        self.episode_lengths = np.zeros(self.nenvs)
        self.reward_queues = [deque([], maxlen=running_mean_size)
                              for _ in range(self.nenvs)]

    def should_write_summaries(self):
        """ Returns true if it's time to write summaries. """
        return np.all(self.had_ended_episodes)

    def add_summaries(self):
        """ Writes summaries. """
        self.writer.add_scalar(
            f"Episodes/total_reward",
            np.mean([q[-1] for q in self.reward_queues]),
            self.step_var
        )
        self.writer.add_scalar(
            f"Episodes/reward_mean_{self.reward_queues[0].maxlen}",
            np.mean([np.mean(q) for q in self.reward_queues]),
            self.step_var
        )
        self.writer.add_scalar(
            f"Episodes/episode_length",
            np.mean(self.episode_lengths),
            self.step_var
        )
        if self.had_ended_episodes.size > 1:
            self.writer.add_scalar(
                f"Episodes/min_reward",
                min(q[-1] for q in self.reward_queues),
                self.step_var
            )
            self.writer.add_scalar(
                f"Episodes/max_reward",
                max(q[-1] for q in self.reward_queues),
                self.step_var
            )
        self.episode_lengths.fill(0)
        self.had_ended_episodes.fill(False)

    def step(self, action):
        obs, rew, done, info = self.env.step(action)
        self.rewards += rew
        self.episode_lengths[~self.had_ended_episodes] += 1

        info_collection = [info] if isinstance(info, dict) else info
        done_collection = [done] if isinstance(done, bool) else done
        done_indices = [i for i, info in enumerate(info_collection)
                        if info.get("real_done", done_collection[i])]
        for i in done_indices:
            if not self.had_ended_episodes[i]:
                self.had_ended_episodes[i] = True
            self.reward_queues[i].append(self.rewards[i])
            self.rewards[i] = 0

        self.step_var += self.nenvs
        if self.should_write_summaries():
            self.add_summaries()
        return obs, rew, done, info

    def reset(self, **kwargs):
        self.rewards.fill(0)
        self.episode_lengths.fill(0)
        self.had_ended_episodes.fill(False)
        return self.env.reset(**kwargs)