# Implements first heuristic for adversarial isolation
class IsolationHeuristic1:
    def __init__(self, board_instance):
        self.board = board_instance

    def get_available_cells(self, location):
        """
        Get the number of available cells surrounding a given location.

        :param location: Tuple representing the location.
        :return: Number of available cells.
        """
        x, y = location
        legal_moves = []
        # Define possible moves in each direction, including diagonals
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if self.board.is_valid_position(new_x, new_y) and self.board.is_position_free((new_x, new_y)):
                legal_moves.append((new_x, new_y))

        return len(legal_moves)

    def heuristic_move(self, current_location, next_location):
        """
        Calculate the heuristic value for moving a pawn.

        :param current_location: Tuple representing the current location of the pawn.
        :param next_location: Tuple representing the next location of the pawn.
        :return: The heuristic value of the move.
        """
        current_cells = self.get_available_cells(current_location)
        next_cells = self.get_available_cells(next_location)

        if current_cells - next_cells > 0:
            return 1
        elif current_cells - next_cells == 0:
            return 0
        else:
            return -1

    def heuristic_token(self, opponent_location):
        """
        Calculate the heuristic value for removing a token.

        :param opponent_location: Tuple representing the opponent's location.
        :return: The heuristic value of removing the token.
        """
        current_available_cells = self.get_available_cells(opponent_location)
        original_available_cells = self.get_available_cells(opponent_location) # this is not altered in this context

        if current_available_cells == 0:  # a.k.a WINNER
            return 100
        elif current_available_cells < original_available_cells:
            return 2
        else:
            return 0

    def evaluate(self, current_location, opponent_location):
        move_value = self.heuristic_move(current_location, opponent_location)
        token_value = self.heuristic_token(opponent_location)
        return move_value + token_value
