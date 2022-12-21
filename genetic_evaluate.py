# log:
# Increased number of generations from 5 --> 20 to get an increase in score from -0.007 to 0.028 against greedy
# Increased number of chromosomes in population from 5 --> 10 and got -0.009

import random
from cribbage import Game
from policy import CribbagePolicy, CompositePolicy, GreedyThrower, GreedyPegger
from heuristic_policy import HeuristicPolicy

class GeneticEvaluate():
    def __init__(self):
        self.best_params = None

    def evaluate_score(self, parameters):
        game = Game()
        baseline_greedy = CompositePolicy(game, GreedyThrower(game), GreedyPegger(game))
        genetic = HeuristicPolicy(game, parameters)
        num_wins = 0

        for g in range(1000): # run 1000 game iterations # take the average win rate
            results = game.play(genetic, baseline_greedy, lambda mess: None)
            if results[0] > 0:
                num_wins += 1
        
        return num_wins

    # Start with a random population of "chromosomes" (i.e. sets of heuristics)
    # Create a single chromosome representing a strategy
    def create_chromosome(self):
        chromosome = [random.uniform(0, 5), random.uniform(0, 5), random.uniform(0, 5), random.uniform(0, 5), random.uniform(0, 5)]
        return chromosome

    def generate_population(self, size):
        population = []
        for i in range(size):
            chromosome = self.create_chromosome()
            population.append(chromosome)
        return population

    # Select parents by fitness
    def selection(self, pop, scores):
        # compute the fitness sum
        fitness_sum = sum(scores)
        # choose 2 parents with probability proportional to their fitness
        p1 = random.uniform(0, fitness_sum)
        p2 = random.uniform(0, fitness_sum)
        # find the corresponding individuals
        i1 = 0
        i2 = 0
        s = 0
        for i in range(len(scores)):
            s += scores[i]
            if s >= p1:
                i1 = i
            break
        s = 0
        for i in range(len(scores)):
            s += scores[i]
            if s >= p2:
                i2 = i
            break
        return (pop[i1], pop[i2])

    def crossover(self, p1, p2):
        # choose a crossover point
        cxpoint = random.randint(1, len(p1)-1)
        # create the offspring
        o1 = p1[:cxpoint] + p2[cxpoint:]
        o2 = p2[:cxpoint] + p1[cxpoint:]
        return (o1, o2)

    def mutate(self, child):
        place = random.randint(0, 4)
        value = random.uniform(0, 5)
        child[place] = value
        return child


    def genetic(self):
        # Setting population size
        population = self.generate_population(5)

        # Step 1: Evaluate each individual
        scores = [self.evaluate_score(chromosome) for chromosome in population]

        # Limiting number of generations
        for i in range(2):
            # Step 2: Select 2 parents out of population for crossover (bias towards more fit individuals)
            parents = self.selection(population, scores)

            # Step 3: Crossover to create the offspring
            offspring = self.crossover(parents[0], parents[1])

            # Step 4 and 5: Offspring replace parents, mutate the offspring
            offspring = [self.mutate(x) for x in offspring]

            # create the new population
            population = offspring

            # compute the fitness of the new population
            scores = [self.evaluate_score(chromosome) for chromosome in population]

        # return the best individual
        best_individual = max(zip(population, scores), key=lambda x: x[1])
        return best_individual[0]
