# Defines the Player class, including methods for making moves
from board import IsolationBoard


class IsolationPlayer:
    def __init__(self, board):
        self.board = board

    def get_legal_moves(self, current_position):
        x, y = current_position
        legal_moves = []

        # Define possible moves in each direction, including diagonals
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            while self.board.is_valid_position(new_x, new_y) and self.board.is_position_free((new_x, new_y)):
                legal_moves.append((new_x, new_y))
                new_x += dx
                new_y += dy

        return legal_moves

    def make_move(self, position):
        # Note that moving does not "occupy" a position anymore in the sense of making it a 0.
        return self.board.is_valid_position(*position) and self.board.is_position_free(position)

    def make_block(self, position):
        return self.board.occupy_position(position)

    def get_user_move_and_block(self, current_position):
        """ Prompt the user for a move and a block, returning both coordinates """
        legal_moves = self.get_legal_moves(current_position)
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


# Test the combined functionality
if __name__ == "__main__":
    board = IsolationBoard()
    player = IsolationPlayer(board)

    current_pos = (4, 3)
    player.make_move(current_pos)
    board.display(player_position=current_pos)

    while True:
        move, block = player.get_user_move_and_block(current_pos)
        if not player.make_move(move):
            print("Invalid move. Try again.")
            continue

        if not player.make_block(block):
            print("Invalid block. Try again.")
            continue

        current_pos = move  # Update the current position
        board.display(player_position=current_pos)
