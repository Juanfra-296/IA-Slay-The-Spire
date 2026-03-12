from game.cards.strike import Strike
from game.cards.defend import Defend
from game.cards.bash import Bash


def ironclad_starter_deck():

    deck = []

    for _ in range(5):
        deck.append(Strike())

    for _ in range(4):
        deck.append(Defend())

    deck.append(Bash())

    return deck