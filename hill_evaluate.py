
import random
from cribbage import Game
from policy import CribbagePolicy, CompositePolicy, GreedyThrower, GreedyPegger
import itertools as it
from deck import Deck
from heuristic_policy import HeuristicPolicy

# log: first tried with smaller number of games to test for functionality
# playing around with parameter range for heuristics to see if it made a difference
# tuning step size to see if it makes a difference
# tried to do it stochastically first by choosing random parameter to tune at a time
# tries to implement hill climbing by choosing parameter with steepest ascent
# takes a really long time to evaluate and getting different results every time
# a lot of plateauing can happen
class HillEvaluate():
    def __init__(self):
        self._params = [random.uniform(0, 5), random.uniform(0, 5), random.uniform(0, 5), random.uniform(0, 5), random.uniform(0, 5)] #[0.5, 0.5, 0.5, 0.5, 0.5]
    
    def evaluate_score(self, parameters):
        game = Game()
        baseline_greedy = CompositePolicy(game, GreedyThrower(game), GreedyPegger(game))
        hill_climb = HeuristicPolicy(game, parameters)
        num_wins = 0

        for g in range(1000): # run 1000 game iterations # take the average win rate
            results = game.play(hill_climb, baseline_greedy, lambda mess: None)
            if results[0] > 0:
                num_wins += 1
        
        return num_wins
    
    def hill_climb(self):
        best_params = self._params
        best_score = self.evaluate_score(best_params)
        step_size = 0.25

        curr_params = best_params
        found_max = False
        
        print(best_score)
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

                    print(substract_score)
                    if substract_score > best_score:
                        best_score = substract_score
                        best_params = subtract_params
                        curr_params = add_params
                        changed = True
            
            if not changed:
                found_max = True

            # param_idx = random.randint(0, 3)
            # step = curr_params[param_idx] * step_size

            # add_params = curr_params
            # add_params[param_idx] += step
            # add_score = self.evaluate_score(add_params)

            # print(add_score)
            # print(best_params)
            # if add_score > best_score:
            #     best_score = add_score
            #     best_params = add_params
            #     curr_params = add_params
            # else:
            #     subtract_params = curr_params
            #     subtract_params[param_idx] -= step
            #     substract_score = self.evaluate_score(subtract_params)

            #     print(substract_score)
            #     if substract_score > best_score:
            #         best_score = substract_score
            #         best_params = subtract_params
            #         curr_params = add_params
            #     else:
            #         found_max = True

        print(best_params)
        return best_params