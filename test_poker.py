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


if __name__ == "__main__":
    unittest.main()