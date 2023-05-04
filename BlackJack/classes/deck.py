from globals import suits, ranks
from classes.card import Card
import random


class Deck:

    def __init__(self):
        self.deck: list[Card] = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))  # build Card objects and add them to the list

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n  ' + card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self) -> Card:
        single_card = self.deck.pop()
        return single_card
