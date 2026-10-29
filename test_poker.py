import unittest

from poker import Card, evaluate_hand


class TestPoker(unittest.TestCase):

    def test_high_card(self):
        hand = [
            Card(2, "♥"), Card(5, "♠"), Card(8, "♦"),
            Card(10, "♣"), Card(13, "♥")
        ]
        self.assertEqual(evaluate_hand(hand), ("Carte haute", 13))


if __name__ == "__main__":
    unittest.main()