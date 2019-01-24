class Deck:
    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        pass

    def deal(self, number_cards=1):

        if (len(self)) >= number_cards:
            deal_cards = self.cards[-number_cards:]
            self.cards = self.cards[:-number_cards]
        else:
            deal_cards = self.cards
            self.cards = []

        return deal_cards

    def __len__(self):
        return len(self.cards)
