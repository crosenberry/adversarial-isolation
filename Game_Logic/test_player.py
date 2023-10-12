import unittest
from board import IsolationBoard
from player import IsolationPlayer

class TestIsolationPlayer(unittest.TestCase):
    """
    Test class for the IsolationPlayer class.

    This test class provides a collection of tests to ensure the correct
    functionality and behavior of the IsolationPlayer class. It covers player
    initialization using a board object, making a move, and blocking.

    """
    def setUp(self):
        self.board = IsolationBoard()
        self.player = IsolationPlayer(self.board)

    def test_make_move(self):
        # Set opponent position.
        opp_position = (5, 5)

        # Try a legal move
        self.assertTrue(self.player.make_move((2, 2), (3, 3), opp_position))
        # Try an illegal move (beyond one step)
        self.assertFalse(self.player.make_move((2, 2), (5, 5), opp_position))

    def test_make_block(self):
        self.assertTrue(self.player.make_block((4, 4)))
        self.assertFalse(self.player.make_block((4, 4)))  # Blocking the same position again

if __name__ == '__main__':
    unittest.main()
