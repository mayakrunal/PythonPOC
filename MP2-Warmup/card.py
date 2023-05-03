"""
The Card Class
Suit,Rank,Value
"""
from globals import values


class Card:
    """
    The Card Class
    """

    def __init__(self, suit: str, rank: str):
        """
        create a new card
        :param suit: The suit of the card
        :param rank: the rank of the card
        """
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        """
        Print the instance of the class
        """
        return self.rank + " of " + self.suit
