from .decision_maker import DecisionMaker

class AIPlayer:
    def __init__(self, board, max_depth=3, heuristic_type="heuristic_1"):
        self.board = board
        self.decision_maker = DecisionMaker(self, board)
        self.max_depth = max_depth
        self.heuristic_type = heuristic_type
        self.past_blocks = set()  # A set to store past blocks

    def get_legal_moves(self, board, current_position, opponent_position):
        x, y = current_position
        legal_moves = []

        # Define possible moves in each direction, including diagonals
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if board.is_valid_position(new_x, new_y) and (new_x, new_y) != opponent_position:
                if board.is_position_free((new_x, new_y)):
                    legal_moves.append((new_x, new_y))

        return legal_moves

    def compute_move(self, board, current_position, opponent_position):
        legal_moves = self.get_legal_moves(board, current_position, opponent_position)
        if not legal_moves:
            return None  # Return None if no legal moves are available
        return self.decision_maker.choose_move(current_position, opponent_position, self.max_depth, self.heuristic_type)

    def compute_block(self, board, current_position, opponent_position):
        best_block = None
        min_future_moves = float('inf')

        # Iterate over all cells on the board
        for i in range(6):
            for j in range(8):
                cell = (i, j)

                # Ensure the cell is not already blocked, isn't occupied by either player, and hasn't been blocked before
                if board.is_position_free(cell) and cell not in [current_position,
                                                                 opponent_position] and cell not in self.past_blocks:

                    # Simulate a block at this cell
                    board.block_cell(cell)

                    # Calculate the possible future moves for the opponent two steps ahead
                    opponent_next_moves = self.get_legal_moves(board, opponent_position, current_position)
                    future_moves_count = sum(
                        len(self.get_legal_moves(board, next_move, current_position)) for next_move in
                        opponent_next_moves)

                    # Restore the cell (remove the block) for the next iteration
                    board.unblock_cell(cell)

                    # Check if this block is better than the previous best block
                    if future_moves_count < min_future_moves:
                        min_future_moves = future_moves_count
                        best_block = cell

        # Add the chosen block to the past_blocks set
        if best_block:
            self.past_blocks.add(best_block)

        return best_block

