
from dataclasses import dataclass


@dataclass
class Card:
    value: int
    suit: str



from collections import Counter


def evaluate_hand(hand):
    values = [card.value for card in hand]
    value_counts = Counter(values)

    if 3 in value_counts.values():
        return ("Brelan", 30)

    highest_card = max(values)
    return ("Carte haute", highest_card)

