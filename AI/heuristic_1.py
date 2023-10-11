# Implements first heuristic for adversarial isolation
class IsolationHeuristic1:
    def __init__(self):
        # Initialize the board state, locations, etc. as needed
        pass

    def get_available_cells(self, location, board_state):
        """
        Get the number of available cells surrounding a given location.

        :param location: Tuple representing the location.
        :param board_state: A representation of the current board state.
        :return: Number of available cells.
        """
        # Implement this function based on your game’s rules and board representation.
        pass

    def heuristic_move(self, current_location, next_location, board_state):
        """
        Calculate the heuristic value for moving a pawn.

        :param current_location: Tuple representing the current location of the pawn.
        :param next_location: Tuple representing the next location of the pawn.
        :param board_state: A representation of the current board state.
        :return: The heuristic value of the move.
        """
        current_cells = self.get_available_cells(current_location, board_state)
        next_cells = self.get_available_cells(next_location, board_state)

        if current_cells - next_cells > 0:
            return 1
        elif current_cells - next_cells == 0:
            return 0
        else:
            return -1

    def heuristic_token(self, opponent_location, board_state_after_removal):
        """
        Calculate the heuristic value for removing a token.

        :param opponent_location: Tuple representing the opponent's location.
        :param board_state_after_removal: The board state after the proposed token is removed and the player’s proposed move is made.
        :return: The heuristic value of removing the token.
        """
        current_available_cells = self.get_available_cells(opponent_location, board_state_after_removal)
        original_available_cells = self.get_available_cells(opponent_location, board_state)
        # Assuming board_state is the original state

        if current_available_cells == 0:  # a.k.a WINNER
            return 100
        elif current_available_cells < original_available_cells:
            return 2
        else:
            return 0


# Example usage:
#game = IsolationGame()
#current_loc = (2, 2)
#next_loc = (3, 3)
#opponent_loc = (4, 4)
#board_state = []  # This should be your board representation
#board_state_after_removal = []  # This should be your board representation after removing a token and making a move

#heuristic_value_move = game.heuristic_move(current_loc, next_loc, board_state)
#heuristic_value_token = game.heuristic_token(opponent_loc, board_state_after_removal)

#print(f"Heuristic Value for Move: {heuristic_value_move}")
#print(f"Heuristic Value for Token Removal: {heuristic_value_token}")
