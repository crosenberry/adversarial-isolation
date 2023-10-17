import random


class DecisionMaker:

    def __init__(self, game_instance):
        self.game = game_instance
        self.infinity = float('inf')
        self.neg_infinity = float('-inf')

    def alphabeta(self, depth, alpha, beta, maximizing_player, board_state, heuristic_type):
        if depth == 0 or self.game.is_game_over(board_state):
            return self.evaluate_board(board_state, heuristic_type)

        possible_moves = self.game.get_possible_moves(board_state)
        random.shuffle(possible_moves)  # Randomize moves to prevent bias

        if maximizing_player:
            value = self.neg_infinity
            for move in possible_moves:
                new_board_state = self.game.make_move(board_state, move)
                value = max(value, self.alphabeta(depth - 1, alpha, beta, False, new_board_state, heuristic_type))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
            value = self.infinity
            for move in possible_moves:
                new_board_state = self.game.make_move(board_state, move)
                value = min(value, self.alphabeta(depth - 1, alpha, beta, True, new_board_state, heuristic_type))
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value

    def choose_move(self, board_state, max_depth, heuristic_type="heuristic_1"):
        best_value = self.neg_infinity
        best_move = None

        for depth in range(1, max_depth + 1):
            alpha = self.neg_infinity
            beta = self.infinity
            possible_moves = self.game.get_possible_moves(board_state)
            random.shuffle(possible_moves)  # Randomize moves to prevent bias
            for move in possible_moves:
                new_board_state = self.game.make_move(board_state, move)
                move_value = self.alphabeta(depth - 1, alpha, beta, False, new_board_state, heuristic_type)
                if move_value > best_value:
                    best_value = move_value
                    best_move = move
        return best_move
