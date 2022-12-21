from cribbage import Game
from policy import CribbagePolicy, CompositePolicy, GreedyThrower, GreedyPegger
import scoring
import itertools as it
import random
from deck import Deck

class HeuristicPolicy(CribbagePolicy):
    def __init__(self, game, heuristic_params):
        self._game = game
        self._policy = CompositePolicy(game, GreedyThrower(game), GreedyPegger(game))
        self._throw_indices = self._game.throw_indices()
        self._heuristic_params = heuristic_params
    
    def my_score_split(self, hand, indices, turn_cards, crib):
        keep = []
        throw = []
        for i in range(len(hand)):
            if i in indices:
                throw.append(hand[i])
            else:
                keep.append(hand[i])
            
        total = 0
        for turn_card in turn_cards:
            total += scoring.score(self._game, keep, turn_card, False)[0] + crib * scoring.score(self._game, throw, turn_card, True)[0]
        
        return keep, throw, total
    
    def keep(self, hand, scores, am_dealer):
        crib = 1 if am_dealer else -1

        deck = Deck(self._game.all_ranks(), self._game.all_suits(), 1)
        deck.remove(hand)
        turn_cards = deck.peek(deck.size())
        random.shuffle(self._throw_indices)

        max_keep, max_throw, max_score = self.my_score_split(hand, self._throw_indices[0], turn_cards, crib)

        for i in range(1, len(self._throw_indices)):
            keep, throw, score = self.my_score_split(hand, self._throw_indices[i], turn_cards, crib)

            if score > max_score:
                max_keep = keep
                max_throw = throw
                max_score = score

            if score == max_throw:
                throw1 = self._game.rank_value(throw[0].rank())
                throw2 = self._game.rank_value(throw[1].rank())
                if am_dealer:
                    if (throw1 + throw2 == 5 or throw1 == 5 or throw2 == 5 or throw1 + throw2 == 15):
                        max_keep = keep
                        max_throw = throw
                    
                    if abs(throw1 - throw2) < abs(self._game.rank_value(max_throw[0].rank()) - self._game.rank_value(max_throw[1].rank())):
                        max_keep = keep
                        max_throw = throw
                else:
                    if (throw1 != 5 and throw2 != 5 and throw1 + throw2 != 15):
                        if abs(throw1 - throw2) > abs(self._game.rank_value(max_throw[0].rank()) - self._game.rank_value(max_throw[1].rank())):
                            max_keep = keep
                            max_throw = throw

        return max_keep, max_throw

    def peg(self, cards, history, scores, am_dealer):
        rank_count = { rank: 0 for rank in self._game.all_ranks() }
        for card in cards:
            rank_count[card.rank()] += 1

        random.shuffle(cards)
        best_card = None
        best_score = None

        for card in cards:
            score = history.score(self._game, card, 0 if am_dealer else 1)
            card_value = self._game.rank_value(card.rank())

            if score is not None:
                if history.is_start_round() and card_value <= 4:
                    score += self._heuristic_params[0]

                if history.total_points() < 15 and history.total_points() + card_value > 15:
                    score += self._heuristic_params[1]

                if 15 - history.total_points() == card_value:
                    score += self._heuristic_params[2]
                
                if rank_count[card.rank()] >= 2 and history.total_points() + 3 * card_value <= self._game.pegging_limit():
                    score += self._heuristic_params[3]
                
                if history.has_passed(0 if am_dealer else 1) and rank_count[card.rank()] >= 2 and 2 * card_value <= self._game.pegging_limit():
                    score += self._heuristic_params[4]

                if best_score is None or score > best_score:
                    best_card = card
                    best_score = score
    
        return best_card