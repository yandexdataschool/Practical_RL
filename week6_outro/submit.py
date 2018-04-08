import sys
import numpy as np
sys.path.append("..")
import grading


def submit_bandits(scores, email, token):
    epsilon_greedy_agent = None
    ucb_agent = None
    thompson_sampling_agent = None

    for agent in scores:
        if "EpsilonGreedyAgent" in agent.name:
            epsilon_greedy_agent = agent.name
        if "UCBAgent" in agent.name:
            ucb_agent = agent.name
        if "ThompsonSamplingAgent" in agent.name:
            thompson_sampling_agent = agent.name

    assert epsilon_greedy_agent is not None
    assert ucb_agent is not None
    assert thompson_sampling_agent is not None

    grader = grading.Grader("VL9tBt7zEeewFg5wtLgZkA")
    grader.set_answer(
        "YQLYE",
        (int(scores[epsilon_greedy_agent][int(1e4) - 1]) - 
         int(scores[epsilon_greedy_agent][int(5e3) - 1])))

    grader.set_answer(
        "FCHOZ",
        (int(scores[epsilon_greedy_agent][int(1e4) - 1]) - 
         int(scores[ucb_agent][int(1e4) - 1])))

    grader.set_answer(
        "0JWHl",
        (int(scores[epsilon_greedy_agent][int(5e3) - 1]) -
         int(scores[ucb_agent][int(5e3) - 1])))

    grader.set_answer(
        "4rH5M",
        (int(scores[epsilon_greedy_agent][int(1e4) - 1]) -
         int(scores[thompson_sampling_agent][int(1e4) - 1])))

    grader.set_answer(
        "TvOqm",
        (int(scores[epsilon_greedy_agent][int(5e3) - 1]) -
         int(scores[thompson_sampling_agent][int(5e3) - 1])))

    grader.submit(email, token)


def submit_mcts(total_reward, email, token):
    grader = grading.Grader("Giz88DiCEei4TA70mSDOBg")
    grader.set_answer("L1HgT", int(total_reward))
    grader.submit(email, token)
