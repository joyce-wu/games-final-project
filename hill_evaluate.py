
from cribbage import Game
from policy import CribbagePolicy, CompositePolicy, GreedyThrower, GreedyPegger
import itertools as it
from deck import Deck
from heuristic_policy import HeuristicPolicy

class HillEvaluate():
    def __init__(self):
        self._params = [0.5, 0.5, 0.5, 0.5, 0.5]

    def evaluate_score(self, parameters):
        game = Game()
        baseline_greedy = CompositePolicy(game, GreedyThrower(game), GreedyPegger(game))
        hill_climb = HeuristicPolicy(game, parameters)
        num_wins = 0

        for g in range(1000):
            results = game.play(hill_climb, baseline_greedy, lambda mess: None)
            if results[0] > 0:
                num_wins += 1
        
        return num_wins
    
    def hill_climb(self):
        best_params = self._params
        best_score = self.evaluate_score(best_params)
        step_size = 0.5

        curr_params = best_params
        found_max = False

        while not found_max:
            changed = False
            for idx in range(5):
                step = curr_params[idx] * step_size
                add_params = curr_params
                add_params[idx] += step
                add_score = self.evaluate_score(add_params)
                if add_score > best_score:
                    best_score = add_score
                    best_params = add_params
                    curr_params = add_params
                    changed = True
                else:
                    subtract_params = curr_params
                    subtract_params[idx] -= step
                    substract_score = self.evaluate_score(subtract_params)

                    if substract_score > best_score:
                        best_score = substract_score
                        best_params = subtract_params
                        curr_params = subtract_params
                        changed = True
            
            if not changed:
                found_max = True
            
            step_size *= 0.5

        return best_params