from .decision_maker import DecisionMaker

class AIPlayer:
    def __init__(self, board, max_depth=3, heuristic_type="heuristic_1"):
        self.board = board
        self.decision_maker = DecisionMaker(self, board)
        self.max_depth = max_depth
        self.heuristic_type = heuristic_type

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

    def compute_move(self, current_position, opponent_position):
        return self.decision_maker.choose_move(current_position, opponent_position, self.max_depth, self.heuristic_type)

    def compute_block(self, current_position, opponent_position):
        # Initialize the cell to block and its resultant moves to the maximum possible
        best_block = None
        min_available_moves = float('inf')

        # Iterate over all cells on the board
        for i in range(6):
            for j in range(8):
                if (i, j) != current_position and (i, j) != opponent_position:
                    # Simulate a block at this cell
                    self.board.block_cell((i, j))

                    # Calculate number of moves available for the human player after the block
                    available_moves_after_block = len(self.get_legal_moves(opponent_position, current_position))

                    # Restore the cell (remove the block) for the next iteration
                    self.board.unblock_cell((i, j))

                    # Check if this block is better than the previous best block
                    if available_moves_after_block < min_available_moves:
                        min_available_moves = available_moves_after_block
                        best_block = (i, j)

        return best_block
