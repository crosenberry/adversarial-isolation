from .heuristic_1 import heuristic_1  # adjust the import based on your actual implementation
from .heuristic_2 import heuristic_2  # adjust the import based on your actual implementation


class DecisionMaker:
    def __init__(self, game):
        self.game = game

    def decide_move(self):
        moves = self.game.get_legal_moves()
        ranked_moves = []

        for move in moves:
            heuristic_value_move = heuristic_1(self.game, move)
            heuristic_value_token = heuristic_2(self.game, move)
            total_heuristic = heuristic_value_move + heuristic_value_token
            ranked_moves.append((move, total_heuristic))

        ranked_moves.sort(key=lambda x: x[1], reverse=True)

        # If you have multiple moves with the same heuristic value,
        # you might want to break ties here.

        # Returning the move associated with the highest heuristic value.
        return ranked_moves[0][0] if ranked_moves else None

# Then, you can use this DecisionMaker class in your main game loop or wherever you handle turn-taking.
