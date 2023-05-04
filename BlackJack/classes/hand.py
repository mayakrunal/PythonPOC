from classes.card import Card
from globals import values


class Hand:
    def __init__(self):
        self.cards: list[Card] = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card: Card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to aces

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10  # change ace value to 1
            self.aces -= 1
