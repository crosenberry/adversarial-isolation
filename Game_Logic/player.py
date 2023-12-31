# Defines the Player class, including methods for making moves
from .board import IsolationBoard

class IsolationPlayer:
    """
    IsolationPlayer Class - Logic handler for players in the Isolation Game.

    This class provides the essential game logic for the players, determining
    legal moves, blocking positions, and managing the player's interactions
    with the game board.

    Attributes:
        board (IsolationBoard object): An instance of the board class representing the game state.

    Methods:
        get_legal_moves(current_position, opponent_position):
            Determine all legal moves a player can make from a given position, considering the opponent's position.

        make_block(position):
            Marks a specific board position as blocked.

        make_move(current_position, new_position, opponent_position):
            Validates if a move from the current position to a new position is legal.

        get_user_move_and_block(current_position, player_name):
            Interactively prompt the user for their desired move and block positions.

    Note:
        The game assumes a 6x8 board, and the player can move in all 8 cardinal and diagonal directions from
        their current position unless blocked by the opponent or by blocked cells.
    """

    def __init__(self, board):
        self.board = board

    def get_legal_moves(self, current_position, opponent_position):
        x, y = current_position
        legal_moves = []

        # Define possible moves in each direction, including diagonals
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if self.board.is_valid_position(new_x, new_y) and (
                    new_x, new_y) != opponent_position and self.board.is_position_free((new_x, new_y)):
                legal_moves.append((new_x, new_y))

        return legal_moves

    def make_block(self, position):
        """ Block a position on the board. """
        return self.board.block_cell(position)

    def make_move(self, current_position, new_position, opponent_position):
        """ Attempt to move the player to a new position. """
        if new_position in self.get_legal_moves(current_position, opponent_position):
            return True
        return False

    def get_user_move_and_block(self, current_position, opponent_position, player_name):
        """ Prompt the user for a move and a block, returning both coordinates """
        legal_moves = self.get_legal_moves(current_position, opponent_position)
        print(f"{player_name}'s turn!")
        print("Potential moves:", legal_moves)

        while True:
            try:
                move_x, move_y = map(int, input("Enter your move (x y): ").split())
                if (move_x, move_y) not in legal_moves:
                    print("Invalid move. Try again.")
                    continue

                block_x, block_y = map(int, input("Enter a position to block (x y): ").split())
                if self.board.is_position_free((block_x, block_y)):
                    return (move_x, move_y), (block_x, block_y)
                else:
                    print("Invalid block position. Try again.")
            except ValueError:
                print("Invalid input. Enter coordinates as 'x y'. Try again.")


# Test the combined functionality (only run for testing)
if __name__ == "__main__":
    board = IsolationBoard()
    player = IsolationPlayer(board)

    p1_position = (0, 2)
    p2_position = (5, 3)
    board.display(p1_position, p2_position)

    while True:
        move, block = player.get_user_move_and_block(p1_position, p2_position, "P1")
        if not player.make_move(p1_position, move, p2_position):
            print("Invalid move for P1. Try again.")
            continue
        if not player.make_block(block):
            print("Invalid block for P1. Try again.")
            continue
        p1_position = move
        board.display(p1_position, p2_position)

        move, block = player.get_user_move_and_block(p2_position, p1_position, "P2")
        if not player.make_move(p2_position, move, p1_position):
            print("Invalid move for P2. Try again.")
            continue
        if not player.make_block(block):
            print("Invalid block for P2. Try again.")
            continue
        p2_position = move
        board.display(p1_position, p2_position)
