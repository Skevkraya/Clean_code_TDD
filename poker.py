
from dataclasses import dataclass
from collections import Counter

@dataclass
class Card:
    value: int
    suit: str


def is_straight(hand):
    values = sorted(card.value for card in hand)
    return values == list(range(values[0], values[0] + 5))




def evaluate_hand(hand):
    values = [card.value for card in hand]
    value_counts = Counter(values)

    if 3 in value_counts.values():
        return ("Brelan", 30)

    if is_straight(hand):
        return ("Suite", 40)

    return ("Carte haute", max(values))


    

