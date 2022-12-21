import sys

from policy import CompositePolicy, RandomThrower, RandomPegger, GreedyThrower, GreedyPegger
from cribbage import Game, evaluate_policies
from heuristic_policy import HeuristicPolicy
from genetic_evaluate import GeneticEvaluate
from hill_evaluate import HillEvaluate

def define_agent(flag):
    if flag == '--greedy':
        params = [0.5, 0.5, 0.5, 0.5, 0.5]
    if flag == '--hill':
        params = [0.625, 0.625, 0.625, 0.5, 0.325]
    if flag == '--genetic':
        params = [2.8056485076424815, 0.01282169511330089, 4.337214629495559, 0.513857841117974, 1.8741732405009748]
    
    return HeuristicPolicy(game, params)

if __name__ == "__main__":
    game = Game()

    new_agent = define_agent(sys.argv[1])
    baseline = define_agent(sys.argv[2])
    games = int(sys.argv[3])
    
    results = evaluate_policies(game, new_agent, baseline, games)
    print("NET:", results[0])
    print(results)