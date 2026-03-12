import random

from environment.game_state import GameState
from environment.action_space import ActionSpace
from game.deck import Deck
from game.starter_decks import ironclad_starter_deck

class STSEnv:

    def __init__(self):

        self.action_space = ActionSpace()

        self.reset()

    def reset(self):
        self.deck = Deck(ironclad_starter_deck())

        self.deck.draw(5)
        
        self.state = GameState(
            player_hp=80,
            player_max_hp=80,
            energy=3,
            gold=99,
            deck_size=10,
            discard_size=0,
            hand_size=5,
            enemy_hp=40,
            enemy_block=0,
            enemy_intent=1
        )

        self.done = False

        return self.state.to_vector()

    def step(self, action):

        reward = 0

        # simulación simple (por ahora)
        damage = random.randint(4, 10)

        self.state.enemy_hp -= damage

        if self.state.enemy_hp <= 0:
            reward = 100
            self.done = True

        return self.state.to_vector(), reward, self.done, {}

    def render(self):

        print("Player HP:", self.state.player_hp)
        print("Enemy HP:", self.state.enemy_hp)