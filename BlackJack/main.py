from classes.chips import Chips
from classes.deck import Deck
from classes.hand import Hand


def take_bet(chips: Chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?: '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print(f"Sorry, your bet can't exceed {chips.total}")
            else:
                break


def hit(deck: Deck, hand: Hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck: Deck, hand: Hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's': ")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print('Sorry try again.')
            continue
        break


def show_some(player: Hand, dealer: Hand):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player: Hand, dealer: Hand, chips: Chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player: Hand, dealer: Hand, chips: Chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player: Hand, dealer: Hand, chips: Chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player: Hand, dealer: Hand, chips: Chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


if __name__ == '__main__':
    playing: bool = True
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11.')

    # Create Deck and shuffle the deck, deal two cards to each player
    current_deck = Deck()
    current_deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(current_deck.deal())
    player_hand.add_card(current_deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(current_deck.deal())
    dealer_hand.add_card(current_deck.deal())

    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:
        # Prompt for player to hit or stand
        hit_or_stand(current_deck, player_hand)
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(current_deck, dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

        # Inform Player of their chips total
        print("\nPlayer's winnings stand at", player_chips.total)

        # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n': ")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break
