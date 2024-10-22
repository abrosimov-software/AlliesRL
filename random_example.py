''' An example of playing randomly in RLCard
'''
import argparse
import pprint

import rlcard
from rlcard.agents import RandomAgent
from rlcard.utils import set_seed

def run(args):
    # Make environment
    env = rlcard.make(
        args.env,
        config={
            'seed': 42,
            'num_players': 3
        }
    )

    # Seed numpy, torch, random
    set_seed(42)

    # Set agents
    agent1 = RandomAgent(num_actions=env.num_actions)
    agent2 = RandomAgent(num_actions=env.num_actions)
    env.set_agents([agent1, agent2])

    # Generate data from the environment
    trajectories, player_wins = env.run(is_training=False)
    # Print out the trajectories
    print('\nTrajectories:')
    print(trajectories)
    print('\nSample raw observation:')
    pprint.pprint(trajectories[0][0]['raw_obs'])
    print('\nSample raw legal_actions:')
    pprint.pprint(trajectories[0][0]['raw_legal_actions'])
    print(len(trajectories[0]))
    print(len(trajectories[1]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Random example in RLCard")
    parser.add_argument(
        '--env',
        type=str,
        default='leduc-holdem',
        choices=[
            'blackjack',
            'leduc-holdem',
            'limit-holdem',
            'doudizhu',
            'mahjong',
            'no-limit-holdem',
            'uno',
            'gin-rummy',
            'bridge',
        ],
    )

    args = parser.parse_args()

    run(args)