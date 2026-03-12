from game.cards.base_card import BaseCard


class Defend(BaseCard):

    def __init__(self):

        super().__init__("Defend", 1)

        self.block = 5

    def play(self, state):

        state.energy -= self.cost

        state.player_block += self.block