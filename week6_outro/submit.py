import sys
sys.path.append("..")


def test_bandits(agents, scores):
    test_outputs = {}
    
    epsilon_greedy_agent = None
    ucb_agent = None
    thompson_sampling_agent = None

    for agent in agents:
        if "EpsilonGreedyAgent" in agent.name:
            epsilon_greedy_agent = agent.name
        if "UCBAgent" in agent.name:
            ucb_agent = agent.name
        if "ThompsonSamplingAgent" in agent.name:
            thompson_sampling_agent = agent.name

    assert epsilon_greedy_agent is not None
    assert ucb_agent is not None
    assert thompson_sampling_agent is not None

    test_outputs['Epsilon greedy agent'] = int(scores[epsilon_greedy_agent][int(1e4) - 1]) - int(scores[epsilon_greedy_agent][int(5e3) - 1])
    
    test_outputs['UCB agent 1'] = int(scores[epsilon_greedy_agent][int(1e4) - 1]) - int(scores[ucb_agent][int(1e4) - 1])

    test_outputs['UCB agent 2'] = int(scores[epsilon_greedy_agent][int(5e3) - 1]) - int(scores[ucb_agent][int(5e3) - 1])

    test_outputs['Thompson sampling agent 1'] = int(scores[epsilon_greedy_agent][int(1e4) - 1]) - int(scores[thompson_sampling_agent][int(1e4) - 1])
    
    test_outputs['Thompson sampling agent 2'] = int(scores[epsilon_greedy_agent][int(5e3) - 1]) - int(scores[thompson_sampling_agent][int(5e3) - 1])

    return test_outputs


def test_mcts(total_reward):
    return int(total_reward)
