"""
The Main Logic of the Game (War Card Game)
"""
from card import Card
from deck import Deck
from player import Player

if __name__ == '__main__':
    # Game Setup
    player_one = Player("One")
    player_two = Player("Two")
    new_deck = Deck()
    new_deck.shuffle()

    game_on: bool = True
    round_num: int = 0

    for x in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    # while game on
    while game_on:
        round_num += 1
        print(f'Round {round_num}')

        if len(player_one.all_cards) == 0:
            print('Player one, out of cards! Player Two Wins!')
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            print('Player two, out of cards! Player One Wins!')
            game_on = False
            break

        # Start a new Round
        player_one_cards: list[Card] = [player_one.remove_one()]
        player_two_cards: list[Card] = [player_two.remove_one()]

        at_war: bool = True

        while at_war:
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                at_war = False
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                at_war = False
            else:
                print('WAR!')
                if len(player_one.all_cards) < 5:
                    print('Player one unable to declare war')
                    print('Player two wins!')
                    game_on = False
                    break

                if len(player_two.all_cards) < 5:
                    print('Player two unable to declare war')
                    print('Player one wins!')
                    game_on = False
                    break

                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
