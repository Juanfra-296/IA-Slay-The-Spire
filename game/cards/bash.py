from game.cards.base_card import BaseCard


class Bash(BaseCard):

    def __init__(self):

        super().__init__("Bash", 2)

        self.damage = 8

    def play(self, state):

        state.energy -= self.cost

        damage = max(0, self.damage - state.enemy_block)

        state.enemy_block = max(0, state.enemy_block - self.damage)

        state.enemy_hp -= damage