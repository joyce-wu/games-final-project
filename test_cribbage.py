import sys

from policy import CompositePolicy, RandomThrower, RandomPegger, GreedyThrower, GreedyPegger
from cribbage import Game, evaluate_policies
from my_policy import MyPolicy
from genetic_policy import GeneticPolicy
from hill_policy import HillPolicy
from hill_evaluate import HillEvaluate

def define_agent(flag):
    if flag == '--base':
        return CompositePolicy(game, GreedyThrower(game), GreedyPegger(game))
    if flag == '--greedy':
        return MyPolicy(game)
    if flag == '--hill':
        return HillPolicy(game)
    if flag == '--genetic':
        return GeneticPolicy(game)

if __name__ == "__main__":
    hill = HillEvaluate()
    hill.hill_climb()
    game = Game()

    # new_agent = define_agent(sys.argv[1])
    # baseline = define_agent(sys.argv[2])
    # games = int(sys.argv[3])
    
    # results = evaluate_policies(game, new_agent, baseline, games)
    # print("NET:", results[0])
    # print(results)