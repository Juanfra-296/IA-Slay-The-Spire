from enum import Enum


class ActionType(Enum):
    PLAY_CARD_0 = 0
    PLAY_CARD_1 = 1
    PLAY_CARD_2 = 2
    PLAY_CARD_3 = 3
    PLAY_CARD_4 = 4
    END_TURN = 5


class ActionSpace:

    def __init__(self):
        self.actions = list(ActionType)

    def size(self):
        return len(self.actions)

    def get_action(self, index):
        return self.actions[index]