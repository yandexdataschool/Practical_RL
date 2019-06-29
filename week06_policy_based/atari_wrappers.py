""" Environment wrappers. """
from collections import deque

import cv2
import gym
import gym.spaces as spaces
from gym.envs import atari
import numpy as np
import tensorflow as tf

from env_batch import ParallelEnvBatch
cv2.ocl.setUseOpenCL(False)


class EpisodicLife(gym.Wrapper):
    """ Sets done flag to true when agent dies. """

    def __init__(self, env):
        super(EpisodicLife, self).__init__(env)
        self.lives = 0
        self.real_done = True

    def step(self, action):
        obs, rew, done, info = self.env.step(action)
        self.real_done = done
        info["real_done"] = done
        lives = self.env.unwrapped.ale.lives()
        if 0 < lives < self.lives:
            done = True
        self.lives = lives
        return obs, rew, done, info

    def reset(self, **kwargs):
        if self.real_done:
            obs = self.env.reset(**kwargs)
        else:
            obs, _, _, _ = self.env.step(0)
        self.lives = self.env.unwrapped.ale.lives()
        return obs


class FireReset(gym.Wrapper):
    """ Makes fire action when reseting environment.

    Some environments are fixed until the agent makes the fire action,
    this wrapper makes this action so that the epsiode starts automatically.
    """

    def __init__(self, env):
        super(FireReset, self).__init__(env)
        action_meanings = env.unwrapped.get_action_meanings()
        if len(action_meanings) < 3:
            raise ValueError(
                "env.unwrapped.get_action_meanings() must be of length >= 3"
                f"but is of length {len(action_meanings)}")
        if env.unwrapped.get_action_meanings()[1] != "FIRE":
            raise ValueError(
                "env.unwrapped.get_action_meanings() must have 'FIRE' "
                f"under index 1, but is {action_meanings}")

    def step(self, action):
        return self.env.step(action)

    def reset(self, **kwargs):
        self.env.reset(**kwargs)
        obs, _, done, _ = self.env.step(1)
        if done:
            self.env.reset(**kwargs)
        obs, _, done, _ = self.env.step(2)
        if done:
            self.env.reset(**kwargs)
        return obs


class StartWithRandomActions(gym.Wrapper):
    """ Makes random number of random actions at the beginning of each
    episode. """

    def __init__(self, env, max_random_actions=30):
        super(StartWithRandomActions, self).__init__(env)
        self.max_random_actions = max_random_actions
        self.real_done = True

    def step(self, action):
        obs, rew, done, info = self.env.step(action)
        self.real_done = info.get("real_done", True)
        return obs, rew, done, info

    def reset(self, **kwargs):
        obs = self.env.reset()
        if self.real_done:
            num_random_actions = np.random.randint(self.max_random_actions + 1)
            for _ in range(num_random_actions):
                obs, _, _, _ = self.env.step(self.env.action_space.sample())
            self.real_done = False
        return obs


class ImagePreprocessing(gym.ObservationWrapper):
    """ Preprocesses image-observations by possibly grayscaling and resizing. """

    def __init__(self, env, width=84, height=84, grayscale=True):
        super(ImagePreprocessing, self).__init__(env)
        self.width = width
        self.height = height
        self.grayscale = grayscale
        ospace = self.env.observation_space
        low, high, dtype = ospace.low.min(), ospace.high.max(), ospace.dtype
        if self.grayscale:
            self.observation_space = spaces.Box(
                low=low,
                high=high,
                shape=(width, height),
                dtype=dtype,
            )
        else:
            obs_shape = (width, height) + self.observation_space.shape[2:]
            self.observation_space = spaces.Box(low=low, high=high,
                                                shape=obs_shape, dtype=dtype)

    def observation(self, observation):
        """ Performs image preprocessing. """
        if self.grayscale:
            observation = cv2.cvtColor(observation, cv2.COLOR_RGB2GRAY)
        observation = cv2.resize(observation, (self.width, self.height),
                                 cv2.INTER_AREA)
        return observation


class MaxBetweenFrames(gym.ObservationWrapper):
    """ Takes maximum between two subsequent frames. """

    def __init__(self, env):
        if (isinstance(env.unwrapped, atari.AtariEnv) and
                "NoFrameskip" not in env.spec.id):
            raise ValueError(
                "MaxBetweenFrames requires NoFrameskip in atari env id")
        super(MaxBetweenFrames, self).__init__(env)
        self.last_obs = None

    def observation(self, observation):
        obs = np.maximum(observation, self.last_obs)
        self.last_obs = observation
        return obs

    def reset(self, **kwargs):
        self.last_obs = self.env.reset()
        return self.last_obs


class QueueFrames(gym.ObservationWrapper):
    """ Queues specified number of frames together along new dimension. """

    def __init__(self, env, nframes, concat=False):
        super(QueueFrames, self).__init__(env)
        self.obs_queue = deque([], maxlen=nframes)
        self.concat = concat
        ospace = self.observation_space
        if self.concat:
            oshape = ospace.shape[:-1] + (ospace.shape[-1] * nframes,)
        else:
            oshape = ospace.shape + (nframes,)
        self.observation_space = spaces.Box(
            ospace.low.min(), ospace.high.max(), oshape, ospace.dtype)

    def observation(self, observation):
        self.obs_queue.append(observation)
        return (np.concatenate(self.obs_queue, -1) if self.concat
                else np.dstack(self.obs_queue))

    def reset(self, **kwargs):
        obs = self.env.reset()
        for _ in range(self.obs_queue.maxlen - 1):
            self.obs_queue.append(obs)
        return self.observation(obs)


class SkipFrames(gym.Wrapper):
    """ Performs the same action for several steps and returns the final result.
    """

    def __init__(self, env, nskip=4):
        super(SkipFrames, self).__init__(env)
        if (isinstance(env.unwrapped, atari.AtariEnv) and
                "NoFrameskip" not in env.spec.id):
            raise ValueError("SkipFrames requires NoFrameskip in atari env id")
        self.nskip = nskip

    def step(self, action):
        total_reward = 0.0
        for _ in range(self.nskip):
            obs, rew, done, info = self.env.step(action)
            total_reward += rew
            if done:
                break
        return obs, total_reward, done, info

    def reset(self, **kwargs):
        return self.env.reset(**kwargs)


class ClipReward(gym.RewardWrapper):
    """ Modifes reward to be in {-1, 0, 1} by taking sign of it. """

    def reward(self, reward):
        return np.sign(reward)


class TFSummaries(gym.Wrapper):
    """ Writes env summaries."""

    def __init__(self, env, prefix=None, running_mean_size=100, step_var=None):
        super(TFSummaries, self).__init__(env)
        self.episode_counter = 0
        self.prefix = prefix or self.env.spec.id
        self.step_var = (step_var if step_var is not None
                         else tf.train.get_global_step())

        nenvs = getattr(self.env.unwrapped, "nenvs", 1)
        self.rewards = np.zeros(nenvs)
        self.had_ended_episodes = np.zeros(nenvs, dtype=np.bool)
        self.episode_lengths = np.zeros(nenvs)
        self.reward_queues = [deque([], maxlen=running_mean_size)
                              for _ in range(nenvs)]

    def should_write_summaries(self):
        """ Returns true if it's time to write summaries. """
        return np.all(self.had_ended_episodes)

    def add_summaries(self):
        """ Writes summaries. """
        tf.contrib.summary.scalar(
            f"{self.prefix}/total_reward",
            tf.reduce_mean([q[-1] for q in self.reward_queues]),
            step=self.step_var)
        tf.contrib.summary.scalar(
            f"{self.prefix}/reward_mean_{self.reward_queues[0].maxlen}",
            tf.reduce_mean([np.mean(q) for q in self.reward_queues]),
            step=self.step_var)
        tf.contrib.summary.scalar(
            f"{self.prefix}/episode_length",
            tf.reduce_mean(self.episode_lengths),
            step=self.step_var)
        if self.had_ended_episodes.size > 1:
            tf.contrib.summary.scalar(
                f"{self.prefix}/min_reward",
                min(q[-1] for q in self.reward_queues),
                step=self.step_var)
            tf.contrib.summary.scalar(
                f"{self.prefix}/max_reward",
                max(q[-1] for q in self.reward_queues),
                step=self.step_var)
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

        if self.should_write_summaries():
            self.add_summaries()
        return obs, rew, done, info

    def reset(self, **kwargs):
        self.rewards.fill(0)
        self.episode_lengths.fill(0)
        self.had_ended_episodes.fill(False)
        return self.env.reset(**kwargs)


def nature_dqn_env(env_id, nenvs=None, seed=None,
                   summaries=True, clip_reward=True):
    """ Wraps env as in Nature DQN paper. """
    if "NoFrameskip" not in env_id:
        raise ValueError(f"env_id must have 'NoFrameskip' but is {env_id}")
    if nenvs is not None:
        if seed is None:
            seed = list(range(nenvs))
        if isinstance(seed, int):
            seed = [seed] * nenvs
        if len(seed) != nenvs:
            raise ValueError(f"seed has length {len(seed)} but must have "
                             f"length equal to nenvs which is {nenvs}")

        env = ParallelEnvBatch([
            lambda i=i, env_seed=env_seed: nature_dqn_env(
                env_id, seed=env_seed, summaries=False, clip_reward=False)
            for i, env_seed in enumerate(seed)
        ])
        if summaries:
            env = TFSummaries(env, prefix=env_id)
        if clip_reward:
            env = ClipReward(env)
        return env

    env = gym.make(env_id)
    env.seed(seed)
    if summaries:
        env = TFSummaries(env)
    env = EpisodicLife(env)
    if "FIRE" in env.unwrapped.get_action_meanings():
        env = FireReset(env)
    env = StartWithRandomActions(env, max_random_actions=30)
    env = MaxBetweenFrames(env)
    env = SkipFrames(env, 4)
    env = ImagePreprocessing(env, width=84, height=84, grayscale=True)
    env = QueueFrames(env, 4)
    if clip_reward:
        env = ClipReward(env)
    return env
