"""
The Deck Class
"""
import random

from card import Card
from globals import suits, ranks


class Deck:
    """
    Holds 52 Cards (A Deck)
    """

    def __init__(self):
        """
        creates a new Deck
        """
        self.all_cards: list[Card] = []
        # create all the 52 cards
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        """
        Shuffle the cards
        """
        random.shuffle(self.all_cards)

    def deal_one(self) -> Card:
        """
        pop one card
        :return: return the pop card
        """
        return self.all_cards.pop()
