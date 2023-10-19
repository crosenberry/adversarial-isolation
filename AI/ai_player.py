# Import the DecisionMaker class from the relative module named 'decision_maker'
from .decision_maker import DecisionMaker


# Define the AIPlayer class which represents an AI player in the game
class AIPlayer:

    # Constructor for AIPlayer
    def __init__(self, board, max_depth=3, heuristic_type="heuristic_1"):
        # Store the game board
        self.board = board
        # Create an instance of DecisionMaker for making decisions
        self.decision_maker = DecisionMaker(self, board)
        # Define the maximum depth for the decision-making algorithm
        self.max_depth = max_depth
        # Define the heuristic type to use in decision making
        self.heuristic_type = heuristic_type
        # Initialize an empty set to store the positions of blocks that have been placed in the past
        self.past_blocks = set()

    # Method to get all the legal moves from a given position
    def get_legal_moves(self, board, current_position, opponent_position):
        x, y = current_position
        legal_moves = []

        # Define all possible move directions, including diagonals
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        # Iterate through each possible move direction
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            # Check if the new position is valid, not occupied by the opponent, and is free
            if board.is_valid_position(new_x, new_y) and (new_x, new_y) != opponent_position:
                if board.is_position_free((new_x, new_y)):
                    # Add the position to the list of legal moves
                    legal_moves.append((new_x, new_y))

        return legal_moves

    # Method to compute the best move for the AI player
    def compute_move(self, board, current_position, opponent_position):
        # Get all possible legal moves
        legal_moves = self.get_legal_moves(board, current_position, opponent_position)
        # If there are no legal moves, return None
        if not legal_moves:
            return None
        # Use the DecisionMaker instance to choose the best move
        return self.decision_maker.choose_move(current_position, opponent_position, self.max_depth, self.heuristic_type)

    # Method to compute the best block to place on the board
    def compute_block(self, board, current_position, opponent_position):
        best_block = None
        # Initialize a variable to track the minimum number of future moves
        min_future_moves = float('inf')

        # Iterate over all cells on the board
        for i in range(6):
            for j in range(8):
                cell = (i, j)

                # Check if the cell is free, not occupied by any player, and hasn't been blocked before
                if board.is_position_free(cell) and cell not in [current_position,
                                                                 opponent_position] and cell not in self.past_blocks:

                    # Temporarily block the cell to simulate the effects
                    board.block_cell(cell)

                    # Calculate the opponent's possible future moves if the cell were to be blocked
                    opponent_next_moves = self.get_legal_moves(board, opponent_position, current_position)
                    future_moves_count = sum(
                        len(self.get_legal_moves(board, next_move, current_position)) for next_move in
                        opponent_next_moves)

                    # Undo the block for the next iteration
                    board.unblock_cell(cell)

                    # Check if this simulated block reduces the opponent's future moves more than the previous best block
                    if future_moves_count < min_future_moves:
                        min_future_moves = future_moves_count
                        best_block = cell

        # Store the chosen block position in the past_blocks set
        if best_block:
            self.past_blocks.add(best_block)

        return best_block
