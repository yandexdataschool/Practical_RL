""" Environment wrappers. """
from collections import defaultdict, deque

import cv2
import gymnasium as gym
import numpy as np
from gymnasium import ObservationWrapper, RewardWrapper, Wrapper
from gymnasium.spaces import Box
from gymnasium.wrappers import RecordVideo
from shimmy.atari_env import AtariEnv
from tensorboardX import SummaryWriter

from env_batch import ParallelEnvBatch

cv2.ocl.setUseOpenCL(False)


class EpisodicLife(Wrapper):
    """Sets done flag to true when agent dies."""

    def __init__(self, env):
        super().__init__(env)
        self.lives = 0
        self.real_done = True

    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)
        self.real_done = terminated or truncated
        info["real_done"] = self.real_done
        lives = self.env.unwrapped.ale.lives()
        if 0 < lives < self.lives:
            terminated = True
        self.lives = lives
        return obs, reward, terminated, truncated, info

    def reset(self, **kwargs):
        if self.real_done:
            obs, info = self.env.reset(**kwargs)
        else:
            obs, _, terminated, truncated, info = self.env.step(0)
            if terminated or truncated:
                obs, info = self.env.reset(**kwargs)
        self.lives = self.env.unwrapped.ale.lives()
        return obs, info


class FireReset(Wrapper):
    """Makes fire action when reseting environment.

    Some environments are fixed until the agent makes the fire action,
    this wrapper makes this action so that the epsiode starts automatically.
    """

    def __init__(self, env):
        super().__init__(env)
        action_meanings = env.unwrapped.get_action_meanings()
        if len(action_meanings) < 3:
            raise ValueError(
                "env.unwrapped.get_action_meanings() must be of length >= 3"
                f"but is of length {len(action_meanings)}"
            )
        if env.unwrapped.get_action_meanings()[1] != "FIRE":
            raise ValueError(
                "env.unwrapped.get_action_meanings() must have 'FIRE' "
                f"under index 1, but is {action_meanings}"
            )

    def step(self, action):
        return self.env.step(action)

    def reset(self, **kwargs):
        self.env.reset(**kwargs)
        obs, _, terminated, truncated, _ = self.env.step(1)
        if terminated or truncated:
            self.env.reset(**kwargs)
        obs, _, terminated, truncated, _ = self.env.step(2)
        if terminated or truncated:
            self.env.reset(**kwargs)
        return obs, {}


class StartWithRandomActions(Wrapper):
    """Makes random number of random actions at the beginning of each
    episode."""

    def __init__(self, env, max_random_actions=30):
        super().__init__(env)
        self.max_random_actions = max_random_actions
        self.real_done = True

    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)
        self.real_done = info.get("real_done", True)
        return obs, reward, terminated, truncated, info

    def reset(self, **kwargs):
        obs, info = self.env.reset(**kwargs)
        if self.real_done:
            num_random_actions = self.unwrapped.np_random.integers(
                low=1, high=self.max_random_actions + 1
            )
            for _ in range(num_random_actions):
                obs, _, _, _, info = self.env.step(self.env.action_space.sample())
            self.real_done = False
        return obs, info


class ImagePreprocessing(ObservationWrapper):
    """Preprocesses image-observations by possibly grayscaling and resizing."""

    def __init__(self, env, height=84, width=84, grayscale=True):
        super().__init__(env)
        self.height = height
        self.width = width
        self.grayscale = grayscale
        ospace = self.env.observation_space
        low, high, dtype = ospace.low.min(), ospace.high.max(), ospace.dtype
        if self.grayscale:
            self.observation_space = Box(
                low=low,
                high=high,
                shape=(height, width),
                dtype=dtype,
            )
        else:
            self.observation_space = Box(
                low=low,
                high=high,
                shape=(height, width, *self.observation_space.shape[2:]),
                dtype=dtype,
            )

    def observation(self, observation):
        """Performs image preprocessing."""
        if self.grayscale:
            observation = cv2.cvtColor(observation, cv2.COLOR_RGB2GRAY)
        observation = cv2.resize(observation, (self.width, self.height), cv2.INTER_AREA)
        return observation


class MaxBetweenFrames(ObservationWrapper):
    """Takes maximum between two subsequent frames."""

    def __init__(self, env):
        if isinstance(env.unwrapped, AtariEnv) and "NoFrameskip" not in env.spec.id:
            raise ValueError("MaxBetweenFrames requires NoFrameskip in atari env id")
        super().__init__(env)
        self.last_obs = None

    def observation(self, observation):
        obs = np.maximum(observation, self.last_obs)
        self.last_obs = observation
        return obs

    def reset(self, **kwargs):
        self.last_obs, info = self.env.reset(**kwargs)
        return self.last_obs, info


class QueueFrames(ObservationWrapper):
    """Queues specified number of frames together along new dimension."""

    def __init__(self, env, nframes, concat=False):
        super().__init__(env)
        self.obs_queue = deque([], maxlen=nframes)
        self.concat = concat
        ospace = self.observation_space
        if self.concat:
            oshape = ospace.shape[:-1] + (ospace.shape[-1] * nframes,)
        else:
            oshape = ospace.shape + (nframes,)
        self.observation_space = Box(
            ospace.low.min(), ospace.high.max(), oshape, ospace.dtype
        )

    def observation(self, observation):
        self.obs_queue.append(observation)
        return (
            np.concatenate(self.obs_queue, -1)
            if self.concat
            else np.dstack(self.obs_queue)
        )

    def reset(self, **kwargs):
        obs, info = self.env.reset(**kwargs)
        for _ in range(self.obs_queue.maxlen - 1):
            self.obs_queue.append(obs)
        return self.observation(obs), info


class SkipFrames(Wrapper):
    """Performs the same action for several steps and returns the final result."""

    def __init__(self, env, nskip=4):
        super().__init__(env)
        if isinstance(env.unwrapped, AtariEnv) and "NoFrameskip" not in env.spec.id:
            raise ValueError("SkipFrames requires NoFrameskip in atari env id")
        self.nskip = nskip

    def step(self, action):
        total_reward = 0.0
        for _ in range(self.nskip):
            obs, reward, terminated, truncated, info = self.env.step(action)
            total_reward += reward
            if terminated or truncated:
                break
        return obs, total_reward, terminated, truncated, info

    def reset(self, **kwargs):
        return self.env.reset(**kwargs)


class ClipReward(RewardWrapper):
    """Modifes reward to be in {-1, 0, 1} by taking sign of it."""

    def reward(self, reward):
        return np.sign(reward)


class SwapImageAxes(ObservationWrapper):
    """
    Image shape to num_channels x height x width and normalization
    """

    def __init__(self, env):
        super().__init__(env)
        old_shape = self.observation_space.shape
        self.observation_space = Box(
            low=0.0,
            high=1.0,
            shape=(old_shape[-1], old_shape[0], old_shape[1]),
            dtype=np.float32,
        )

    def observation(self, observation):
        return np.transpose(observation, (2, 0, 1)).astype(np.float32) / 255.0


class SummariesBase(Wrapper):
    """Env summaries writer base."""

    def __init__(self, env, prefix=None, running_mean_size=100, step_var=None):
        super().__init__(env)
        self.episode_counter = 0
        self.prefix = prefix or self.env.spec.id
        self.step_var = step_var or 0

        self.nenvs = getattr(self.env.unwrapped, "nenvs", 1)
        self.rewards = np.zeros(self.nenvs)
        self.had_ended_episodes = np.zeros(self.nenvs, dtype=bool)
        self.episode_lengths = np.zeros(self.nenvs)
        self.reward_queues = [
            deque([], maxlen=running_mean_size) for _ in range(self.nenvs)
        ]

    def should_write_summaries(self):
        """Returns true if it's time to write summaries."""
        return np.all(self.had_ended_episodes)

    def add_summaries(self):
        """Writes summaries."""
        self.add_summary(
            f"Episodes/total_reward", np.mean([q[-1] for q in self.reward_queues])
        )
        self.add_summary(
            f"Episodes/reward_mean_{self.reward_queues[0].maxlen}",
            np.mean([np.mean(q) for q in self.reward_queues]),
        )
        self.add_summary(f"Episodes/episode_length", np.mean(self.episode_lengths))
        if self.had_ended_episodes.size > 1:
            self.add_summary(
                f"Episodes/min_reward",
                min(q[-1] for q in self.reward_queues),
            )
            self.add_summary(
                f"Episodes/max_reward",
                max(q[-1] for q in self.reward_queues),
            )
        self.episode_lengths.fill(0)
        self.had_ended_episodes.fill(False)

    def step(self, action):
        obs, rew, terminated, truncated, info = self.env.step(action)
        self.rewards += rew
        self.episode_lengths[~self.had_ended_episodes] += 1

        info_collection = [info] if isinstance(info, dict) else info
        terminated_collection = (
            [terminated] if isinstance(terminated, bool) else terminated
        )
        truncated_collection = [truncated] if isinstance(truncated, bool) else truncated
        done_indices = [
            i
            for i, info in enumerate(info_collection)
            if info.get(
                "real_done", terminated_collection[i] or truncated_collection[i]
            )
        ]
        for i in done_indices:
            if not self.had_ended_episodes[i]:
                self.had_ended_episodes[i] = True
            self.reward_queues[i].append(self.rewards[i])
            self.rewards[i] = 0

        self.step_var += self.nenvs
        if self.should_write_summaries():
            self.add_summaries()
        return obs, rew, terminated, truncated, info

    def reset(self, **kwargs):
        self.rewards.fill(0)
        self.episode_lengths.fill(0)
        self.had_ended_episodes.fill(False)
        return self.env.reset(**kwargs)


class TensorboardSummaries(SummariesBase):
    """Writes env summaries using Tensorboard."""

    def __init__(self, env, prefix=None, running_mean_size=100, step_var=None):
        super().__init__(env, prefix, running_mean_size, step_var)
        self.writer = SummaryWriter(f"logs/{self.prefix}")

    def add_summary(self, name, value):
        if isinstance(value, dict):
            self.writer.add_scalars(name, value, self.step_var)
        else:
            self.writer.add_scalar(name, value, self.step_var)


class NumpySummaries(SummariesBase):

    _summaries = defaultdict(list)

    @classmethod
    def get_values(cls, name):
        return cls._summaries[name]

    @classmethod
    def clear(cls):
        cls._summaries = defaultdict(list)

    def __init__(self, env, prefix=None, running_mean_size=100, step_var=None):
        super().__init__(env, prefix, running_mean_size, step_var)

    def add_summary(self, name, value):
        self._summaries[name].append((self.step_var, value))


def get_summaries_class(summaries):
    summaries_class_map = {
        "Numpy": NumpySummaries,
        "Tensorboard": TensorboardSummaries,
    }
    if summaries in summaries_class_map:
        return summaries_class_map[summaries]

    raise NotImplementedError(
        f"Unknown summaries: {summaries}. Supported summaries: {summaries_class_map.keys()}"
    )


# magic for parallel launching of environments
class _thunk:
    def __init__(self, i, env_id, **kwargs):
        self.env_id = env_id
        self.i = i
        self.kwargs = kwargs

    def __call__(self):
        return nature_dqn_env(
            self.env_id,
            summaries=False,
            clip_reward=False,
            **self.kwargs,
        )


def nature_dqn_env(env_id, nenvs=None, seed=None, summaries="Numpy", clip_reward=True):
    """Wraps env as in Nature DQN paper."""
    if "NoFrameskip" not in env_id:
        raise ValueError(f"env_id must have 'NoFrameskip' but is {env_id}")
    if nenvs is not None:
        if seed is None:
            seed = list(range(nenvs))
        if isinstance(seed, int):
            seed = [seed] * nenvs
        if len(seed) != nenvs:
            raise ValueError(
                f"seed has length {len(seed)} but must have "
                f"length equal to nenvs which is {nenvs}"
            )

        thunks = [_thunk(i, env_id) for i in range(nenvs)]
        env = ParallelEnvBatch(make_env=thunks, seeds=seed)

        if summaries:
            summaries_class = get_summaries_class(summaries)
            env = summaries_class(env, prefix=env_id)
        if clip_reward:
            env = ClipReward(env)
        return env

    env = gym.make(env_id, render_mode="rgb_array")
    if summaries:
        env = TensorboardSummaries(env)
    env = EpisodicLife(env)
    if "FIRE" in env.unwrapped.get_action_meanings():
        env = FireReset(env)
    env = StartWithRandomActions(env, max_random_actions=30)
    env = MaxBetweenFrames(env)
    env = SkipFrames(env, 4)
    env = ImagePreprocessing(env, width=84, height=84, grayscale=True)
    env = QueueFrames(env, 4)
    env = SwapImageAxes(env)
    if clip_reward:
        env = ClipReward(env)
    return env
