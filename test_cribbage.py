import sys

from policy import CompositePolicy, RandomThrower, RandomPegger, GreedyThrower, GreedyPegger
from cribbage import Game, evaluate_policies
from heuristic_policy import HeuristicPolicy
from hill_evaluate import HillEvaluate
from genetic_evaluate import GeneticEvaluate

def define_agent(flag):
    if flag == '--base':
        return CompositePolicy(game, GreedyThrower(game), GreedyPegger(game))
    if flag == '--greedy':
        params = [0.5, 0.5, 0.5, 0.5, 0.5]
    if flag == '--hill':
        params = [0.625, 0.5, 0.5, 0.5, 0.5] # TO REPLACE
    if flag == '--genetic':
        genetic = GeneticEvaluate()
        params = genetic.genetic()
    
    return HeuristicPolicy(game, params)

if __name__ == "__main__":
    # hill = HillEvaluate()
    # hill.hill_climb()
    game = Game()

    new_agent = define_agent(sys.argv[1])
    baseline = define_agent(sys.argv[2])
    games = int(sys.argv[3])
    
    results = evaluate_policies(game, new_agent, baseline, games)
    print("NET:", results[0])
    print(results)