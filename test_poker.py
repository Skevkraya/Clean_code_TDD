import unittest

from poker import Card, evaluate_hand


class TestPoker(unittest.TestCase):

    def test_high_card(self):
        hand = [
            Card(2, "♥"), Card(5, "♠"), Card(8, "♦"),
            Card(10, "♣"), Card(13, "♥")
        ]
        self.assertEqual(evaluate_hand(hand), ("Carte haute", 13))

    def test_three_of_a_kind(self):
        hand = [
            Card(7, "♥"), Card(7, "♠"), Card(7, "♦"),
            Card(2, "♣"), Card(13, "♥")
        ]

        self.assertEqual(evaluate_hand(hand), ("Brelan", 30))

    
    def test_straight(self):
        hand = [
            Card(5, "♥"), Card(6, "♠"), Card(7, "♦"),
            Card(8, "♣"), Card(9, "♥")
        ]

        self.assertEqual(evaluate_hand(hand), ("Suite", 40))


    def test_flush(self):
        hand = [
            Card(2, "♥"), Card(5, "♥"), Card(7, "♥"),
            Card(10, "♥"), Card(13, "♥")
        ]

        self.assertEqual(evaluate_hand(hand), ("Couleur", 45))

    

    def test_full(self):
        hand = [
            Card(2, "♥"), Card(2, "♠"), Card(2, "♦"),
            Card(9, "♣"), Card(9, "♠")
        ]

        self.assertEqual(evaluate_hand(hand), ("Full", 50))
    
    
    def test_four_of_a_kind(self):
        hand = [
            Card(8, "♥"), Card(8, "♠"), Card(8, "♦"),
            Card(8, "♣"), Card(2, "♥")
        ]

        self.assertEqual(evaluate_hand(hand), ("Carré", 60))




if __name__ == "__main__":
    unittest.main()