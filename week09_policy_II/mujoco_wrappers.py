""" MuJoCo env wrappers. """
# Adapted from https://github.com/openai/baselines
import gym
import numpy as np


class RunningMeanVar:
    """ Computes running mean and variance.

    Args:
      eps (float): a small constant used to initialize mean to zero and
        variance to 1.
      shape tuple(int): shape of the statistics.
    """
    # https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Parallel_algorithm

    def __init__(self, eps=1e-4, shape=()):
        self.mean = np.zeros(shape)
        self.var = np.ones(shape)
        self.count = eps

    def update(self, batch):
        """ Updates the running statistics given a batch of samples. """
        if not batch.shape[1:] == self.mean.shape:
            raise ValueError(f"batch has invalid shape: {batch.shape}, "
                             f"expected shape {(None,) + self.mean.shape}")
        batch_mean = np.mean(batch, axis=0)
        batch_var = np.var(batch, axis=0)
        batch_count = batch.shape[0]
        self.update_from_moments(batch_mean, batch_var, batch_count)

    def update_from_moments(self, batch_mean, batch_var, batch_count):
        """ Updates the running statistics given their new values on new data. """
        self.mean, self.var, self.count = update_mean_var_count_from_moments(
            self.mean, self.var, self.count, batch_mean, batch_var, batch_count)


def update_mean_var_count_from_moments(mean, var, count,
                                       batch_mean, batch_var, batch_count):
    """ Updates running mean statistics given a new batch. """
    delta = batch_mean - mean
    tot_count = count + batch_count

    new_mean = mean + delta * batch_count / tot_count
    new_var = (
        var * (count / tot_count)
        + batch_var * (batch_count / tot_count)
        + np.square(delta) * (count * batch_count / tot_count ** 2))
    new_count = tot_count

    return new_mean, new_var, new_count


class Normalize(gym.Wrapper):
    """
    A vectorized wrapper that normalizes the observations
    and returns from an environment.
    """
    # pylint: disable=too-many-arguments

    def __init__(self, env, obs=True, ret=True,
                 clipobs=10., cliprew=10., gamma=0.99, eps=1e-8):
        super().__init__(env)
        self.obs_rmv = (RunningMeanVar(shape=self.observation_space.shape)
                        if obs else None)
        self.ret_rmv = RunningMeanVar(shape=()) if ret else None
        self.clipob = clipobs
        self.cliprew = cliprew
        self.ret = np.zeros(getattr(self.env.unwrapped, "nenvs", 1))
        self.gamma = gamma
        self.eps = eps

    def observation(self, obs):
        """ Preprocesses a given observation. """
        if not self.obs_rmv:
            return obs
        rmv_batch = (np.expand_dims(obs, 0)
                     if not hasattr(self.env.unwrapped, "nenvs")
                     else obs)
        self.obs_rmv.update(rmv_batch)
        obs = (obs - self.obs_rmv.mean) / np.sqrt(self.obs_rmv.var + self.eps)
        obs = np.clip(obs, -self.clipob, self.clipob)
        return obs

    def step(self, action):
        obs, rews, resets, info = self.env.step(action)
        self.ret = self.ret * self.gamma + rews
        obs = self.observation(obs)
        if self.ret_rmv:
            self.ret_rmv.update(self.ret)
            rews = np.clip(rews / np.sqrt(self.ret_rmv.var + self.eps),
                           -self.cliprew, self.cliprew)
        self.ret[resets] = 0.
        return obs, rews, resets, info

    def reset(self, **kwargs):
        self.ret = np.zeros(getattr(self.env.unwrapped, "nenvs", 1))
        obs = self.env.reset(**kwargs)
        return self.observation(obs)
