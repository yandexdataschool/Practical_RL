"""
A thin wrapper for openAI gym environments that maintains a set of parallel games and has a method to generate
interaction sessions given agent one-step applier function.
"""

import numpy as np

# A whole lot of space invaders


class EnvPool(object):
    def __init__(self, agent, make_env, n_parallel_games=1):
        """
        A special class that handles training on multiple parallel sessions
        and is capable of some auxilary actions like evaluating agent on one game session (See .evaluate()).

        :param agent: Agent which interacts with the environment.
        :param make_env: Factory that produces environments OR a name of the gym environment.
        :param n_games: Number of parallel games. One game by default.
        :param max_size: Max pool size by default (if appending sessions). By default, pool is not constrained in size.
        """
        # Create atari games.
        self.agent = agent
        self.make_env = make_env
        self.envs = [self.make_env() for _ in range(n_parallel_games)]

        # Initial observations.
        self.prev_observations = [env.reset() for env in self.envs]

        # Agent memory variables (if you use recurrent networks).
        self.prev_memory_states = agent.get_initial_state(n_parallel_games)

        # Whether particular session has just been terminated and needs
        # restarting.
        self.just_ended = [False] * len(self.envs)

    def interact(self, n_steps=100, verbose=False):
        """Generate interaction sessions with ataries (openAI gym atari environments)
        Sessions will have length n_steps. Each time one of games is finished, it is immediately getting reset
        and this time is recorded in is_alive_log (See returned values).

        :param n_steps: Length of an interaction.
        :returns: observation_seq, action_seq, reward_seq, is_alive_seq
        :rtype: a bunch of tensors [batch, tick, ...]
        """

        def env_step(i, action):
            if not self.just_ended[i]:
                new_observation, cur_reward, is_done, info = \
                    self.envs[i].step(action)
                if is_done:
                    # Game ends now, will finalize on next tick.
                    self.just_ended[i] = True

                # note: is_alive=True in any case because environment is still
                # alive (last tick alive) in our notation.
                return new_observation, cur_reward, True, info
            else:
                # Reset environment, get new observation to be used on next
                # tick.
                new_observation = self.envs[i].reset()

                # Reset memory for new episode.
                initial_memory_state = self.agent.get_initial_state(
                    batch_size=1)
                for m_i in range(len(new_memory_states)):
                    new_memory_states[m_i][i] = initial_memory_state[m_i][0]

                if verbose:
                    print("env %i reloaded" % i)

                self.just_ended[i] = False

                return new_observation, 0, False, {'end': True}

        history_log = []

        for i in range(n_steps - 1):
            new_memory_states, readout = self.agent.step(
                self.prev_memory_states, self.prev_observations)
            actions = self.agent.sample_actions(readout)

            new_observations, cur_rewards, is_alive, infos = zip(
                *map(env_step, range(len(self.envs)), actions))

            # Append data tuple for this tick.
            history_log.append(
                (self.prev_observations, actions, cur_rewards, is_alive))

            self.prev_observations = new_observations
            self.prev_memory_states = new_memory_states

        # add last observation
        dummy_actions = [0] * len(self.envs)
        dummy_rewards = [0] * len(self.envs)
        dummy_mask = [1] * len(self.envs)
        history_log.append(
            (self.prev_observations,
             dummy_actions,
             dummy_rewards,
             dummy_mask))

        # cast to numpy arrays, transpose from [time, batch, ...] to [batch,
        # time, ...]
        history_log = [
            np.array(tensor).swapaxes(0, 1)
            for tensor in zip(*history_log)
        ]
        observation_seq, action_seq, reward_seq, is_alive_seq = history_log

        return observation_seq, action_seq, reward_seq, is_alive_seq
