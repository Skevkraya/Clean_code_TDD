
from dataclasses import dataclass


@dataclass
class Card:
    value: int
    suit: str


def evaluate_hand(hand):
    highest_card = max(card.value for card in hand)
    return ("Carte haute", highest_card)
