import random
from .heuristic_1 import IsolationHeuristic1
from .heuristic_2 import IsolationHeuristic2

class DecisionMaker:
    def __init__(self, player, board):
        self.player = player
        self.board = board
        self.infinity = float('inf')
        self.neg_infinity = float('-inf')
        self.heuristics = {
            "heuristic_1": IsolationHeuristic1,
            "heuristic_2": IsolationHeuristic2
        }

    def alphabeta(self, depth, alpha, beta, maximizing_player, current_position, opponent_position, heuristic_type):
        if depth == 0 or not self.player.get_legal_moves(self.board, current_position, opponent_position):
            return self.evaluate_board(current_position, opponent_position, heuristic_type)

        if maximizing_player:
            value = self.neg_infinity
            for move in self.player.get_legal_moves(self.board, current_position, opponent_position):
                value = max(value, self.alphabeta(depth - 1, alpha, beta, False, move, current_position, heuristic_type))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
            value = self.infinity
            for move in self.player.get_legal_moves(self.board, opponent_position, current_position):
                value = min(value, self.alphabeta(depth - 1, alpha, beta, True, opponent_position, move, heuristic_type))
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value

    def choose_move(self, current_position, opponent_position, max_depth, heuristic_type="heuristic_1"):
        best_value = self.neg_infinity
        best_move = None
        for move in self.player.get_legal_moves(self.board, current_position, opponent_position):
            value = self.alphabeta(max_depth - 1, self.neg_infinity, self.infinity, False, move, current_position, heuristic_type)
            if value > best_value:
                best_value = value
                best_move = move
        print(f"Heuristic value: {best_value}")  # Print heuristic value
        return best_move

    def evaluate_board(self, current_position, opponent_position, heuristic_type):
        heuristic_class = self.heuristics[heuristic_type]
        heuristic_instance = heuristic_class(self.board)
        return heuristic_instance.evaluate(current_position, opponent_position)
