import unittest
from board import IsolationBoard

class TestIsolationBoard(unittest.TestCase):
    """
        Test class for the IsolationBoard class.

        This test class provides a collection of tests to ensure the correct
        functionality and behavior of the IsolationBoard class. It covers board
        initialization, position occupation, validation checks, and free position checks.

        """
    def setUp(self):
        self.board = IsolationBoard()

    def test_initialization(self):
        # Ensure board initializes with correct width and height
        self.assertEqual(len(self.board.board), 8)  # Number of rows
        self.assertEqual(len(self.board.board[0]), 6)  # Number of columns

        # Ensure board is initialized to all 1s
        for row in self.board.board:
            for cell in row:
                self.assertEqual(cell, 1)

    def test_occupy_position(self):
        # Valid position
        self.assertTrue(self.board.occupy_position((2, 3)))
        self.assertEqual(self.board.board[3][2], 0)  # Ensure it's updated

        # Invalid position
        self.assertFalse(self.board.occupy_position((9, 7)))

    def test_is_valid_position(self):
        # Valid positions
        self.assertTrue(self.board.is_valid_position(0, 0))
        self.assertTrue(self.board.is_valid_position(5, 7))

        # Invalid positions
        self.assertFalse(self.board.is_valid_position(8, 6))
        self.assertFalse(self.board.is_valid_position(-1, -1))

    def test_is_position_free(self):
        # By default, all positions are free
        self.assertTrue(self.board.is_position_free((4, 4)))

        # Occupy a position
        self.board.occupy_position((4, 4))
        self.assertFalse(self.board.is_position_free((4, 4)))

if __name__ == '__main__':
    unittest.main()
