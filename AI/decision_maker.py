# Import the heuristic functions to be used in decision making
from .heuristic_1 import IsolationHeuristic1
from .heuristic_2 import IsolationHeuristic2

# Define the DecisionMaker class which makes decisions on the best move
class DecisionMaker:

    # Constructor for DecisionMaker
    def __init__(self, player, board):
        # Reference to the AI player
        self.player = player
        # Reference to the game board
        self.board = board
        # Define positive infinity for alpha-beta pruning
        self.infinity = float('inf')
        # Define negative infinity for alpha-beta pruning
        self.neg_infinity = float('-inf')
        # Map of heuristics, associating heuristic name to the class
        self.heuristics = {
            "heuristic_1": IsolationHeuristic1,
            "heuristic_2": IsolationHeuristic2
        }

    # Alpha-beta pruning algorithm for decision making
    def alphabeta(self, depth, alpha, beta, maximizing_player, current_position, opponent_position, heuristic_type):
        # Base case: if the search depth reaches 0 or there are no legal moves
        if depth == 0 or not self.player.get_legal_moves(self.board, current_position, opponent_position):
            return self.evaluate_board(current_position, opponent_position, heuristic_type)

        # If it's the maximizing player's turn
        if maximizing_player:
            value = self.neg_infinity
            for move in self.player.get_legal_moves(self.board, current_position, opponent_position):
                value = max(value, self.alphabeta(depth - 1, alpha, beta, False, move, current_position, heuristic_type))
                alpha = max(alpha, value)
                if alpha >= beta:  # Alpha-beta pruning
                    break
            return value
        else:  # If it's the minimizing player's turn
            value = self.infinity
            for move in self.player.get_legal_moves(self.board, opponent_position, current_position):
                value = min(value, self.alphabeta(depth - 1, alpha, beta, True, opponent_position, move, heuristic_type))
                beta = min(beta, value)
                if beta <= alpha:  # Alpha-beta pruning
                    break
            return value

    # Method to choose the best move using the alpha-beta pruning algorithm
    def choose_move(self, current_position, opponent_position, max_depth, heuristic_type="heuristic_1"):
        best_value = self.neg_infinity
        best_move = None
        for move in self.player.get_legal_moves(self.board, current_position, opponent_position):
            value = self.alphabeta(max_depth - 1, self.neg_infinity, self.infinity, False, move, current_position, heuristic_type)
            if value > best_value:
                best_value = value
                best_move = move
        # Print the heuristic value for the best move
        print(f"Heuristic value: {best_value}")
        return best_move

    # Method to evaluate the board using the chosen heuristic
    def evaluate_board(self, current_position, opponent_position, heuristic_type):
        # Get the appropriate heuristic class from the map
        heuristic_class = self.heuristics[heuristic_type]
        # Instantiate the heuristic class
        heuristic_instance = heuristic_class(self.board)
        # Evaluate and return the heuristic value
        return heuristic_instance.evaluate(current_position, opponent_position)
