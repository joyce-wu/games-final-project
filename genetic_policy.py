from cribbage import Game
from policy import CribbagePolicy, CompositePolicy, GreedyThrower, GreedyPegger
import scoring
import itertools as it
import random
from deck import Deck

class GeneticPolicy(CribbagePolicy):
    def __init__(self, game):
        self._game = game
        self._policy = CompositePolicy(game, GreedyThrower(game), GreedyPegger(game))
        self._throw_indices = self._game.throw_indices()