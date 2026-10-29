
from dataclasses import dataclass
from collections import Counter

@dataclass
class Card:
    value: int
    suit: str

def is_three_of_a_kind(hand):
    values = [card.value for card in hand]
    value_counts = Counter(values)
    return 3 in value_counts.values()

def is_straight(hand):
    values = sorted(card.value for card in hand)
    return values == list(range(values[0], values[0] + 5))

def is_flush(hand):
    suits = {card.suit for card in hand}
    return len(suits) == 1


def is_full(hand):
    value_counts = Counter(card.value for card in hand)
    return sorted(value_counts.values()) == [2, 3]


def is_four_of_a_kind(hand):
    value_counts = Counter(card.value for card in hand)
    return 4 in value_counts.values()






def evaluate_hand(hand):
    values = [card.value for card in hand]
    value_counts = Counter(values)
    if is_four_of_a_kind(hand):
        return ("Carré", 60)
    
    if is_full(hand):
        return ("Full", 50)

    if is_three_of_a_kind(hand):
        return ("Brelan", 30)

    if is_straight(hand):
        return ("Suite", 40)
    
    if is_flush(hand):
        return ("Couleur", 45)




    return ("Carte haute", max(values))


    

