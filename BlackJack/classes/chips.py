class Chips:
    def __init__(self):
        self.total = 100  # This can be set to default value or supplied by user
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
