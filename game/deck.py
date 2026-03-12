import random


class Deck:

    def __init__(self, cards):

        self.draw_pile = cards[:]
        self.discard_pile = []
        self.hand = []

        random.shuffle(self.draw_pile)

    def draw(self, amount=1):

        for _ in range(amount):

            if len(self.draw_pile) == 0:

                self.shuffle_discard_into_draw()

            if len(self.draw_pile) == 0:
                return

            card = self.draw_pile.pop()

            self.hand.append(card)

    def shuffle_discard_into_draw(self):

        self.draw_pile = self.discard_pile
        self.discard_pile = []

        random.shuffle(self.draw_pile)

    def discard_hand(self):

        self.discard_pile.extend(self.hand)

        self.hand = []

    def play_card(self, index, state):

        if index >= len(self.hand):
            return

        card = self.hand[index]

        if not card.can_play(state):
            return

        card.play(state)

        self.discard_pile.append(card)

        self.hand.pop(index)