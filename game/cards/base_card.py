class BaseCard:

    def __init__(self, name, cost):

        self.name = name
        self.cost = cost

    def can_play(self, state):

        return state.energy >= self.cost

    def play(self, state):

        raise NotImplementedError