"""
The player class
"""
from card import Card


class Player:
    """
    The player
    """

    def __init__(self, name: str):
        self.name = name
        self.all_cards: list[Card] = []

    def remove_one(self) -> Card:
        """
        removes the card from player deck at beginning of the list
        """
        return self.all_cards.pop(0)

    def add_cards(self, new_cards: Card | list[Card]):
        """
        adds new cards to player deck
        :param new_cards: the new cards
        :return: None
        """
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        elif isinstance(new_cards, Card):
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
