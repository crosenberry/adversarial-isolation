# Implements the first heuristic for the adversarial game called isolation
class IsolationHeuristic1:
    def __init__(self, board_instance):
        # Initialize with the current board instance
        self.board = board_instance

    def get_available_cells(self, location):
        """
        Get the number of available cells surrounding a given location.

        :param location: Tuple representing the location on the board.
        :return: Number of available cells adjacent to the location.
        """
        x, y = location
        legal_moves = []

        # Define possible moves in each of the 8 directions including diagonals
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            # Check if the new position is valid and not blocked/occupied
            if self.board.is_valid_position(new_x, new_y) and self.board.is_position_free((new_x, new_y)):
                legal_moves.append((new_x, new_y))

        # Return the count of legal moves from the location
        return len(legal_moves)

    def heuristic_move(self, current_location, next_location):
        """
        Calculate the heuristic value based on moving from current to next location.

        :param current_location: Tuple representing the current location of the pawn.
        :param next_location: Tuple representing the intended next location of the pawn.
        :return: The heuristic value of the move.
        """
        # Calculate available cells from current and next locations
        current_cells = self.get_available_cells(current_location)
        next_cells = self.get_available_cells(next_location)

        # Determine the value based on change in available cells
        if current_cells - next_cells > 0:
            return 1
        elif current_cells - next_cells == 0:
            return 0
        else:
            return -1

    def heuristic_token(self, opponent_location):
        """
        Calculate the heuristic value based on the opponent's position after removing a token.

        :param opponent_location: Tuple representing the opponent's location.
        :return: The heuristic value of the move after removing the token.
        """
        # Calculate available cells from the opponent's location
        current_available_cells = self.get_available_cells(opponent_location)
        original_available_cells = self.get_available_cells(opponent_location)

        # Determine the value based on the opponent's available moves
        if current_available_cells == 0:  # Indicates a winning move
            return 100
        elif current_available_cells < original_available_cells:
            return 2
        else:
            return 0

    def evaluate(self, current_location, opponent_location):
        """
        Evaluate the board's state by summing up the move and token heuristic values.

        :param current_location: Current location of the player's pawn.
        :param opponent_location: Current location of the opponent's pawn.
        :return: Combined heuristic value of the board's state.
        """
        move_value = self.heuristic_move(current_location, opponent_location)
        token_value = self.heuristic_token(opponent_location)

        # Return the total heuristic value
        return move_value + token_value
