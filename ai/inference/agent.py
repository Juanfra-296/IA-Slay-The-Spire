import random


class RandomAgent:

    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, state):

        action_index = random.randint(
            0,
            self.action_space.size() - 1
        )

        return action_index