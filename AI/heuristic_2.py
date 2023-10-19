# Implements the second heuristic for the adversarial game called isolation
class IsolationHeuristic2:
    def __init__(self, board_instance):
        # Initialize with the current board instance
        self.board = board_instance

    def get_available_cells(self, location):
        """
        Get the available cells surrounding a given location.

        :param location: Tuple representing the location on the board.
        :return: List of available cells adjacent to the location.
        """
        x, y = location
        legal_moves = []

        # Define possible moves in each of the 8 directions, including diagonals
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            # Check if the new position is valid and unoccupied
            if self.board.is_valid_position(new_x, new_y) and self.board.is_position_free((new_x, new_y)):
                legal_moves.append((new_x, new_y))

        return legal_moves

    def count_high_density_cells(self):
        """
        Count the number of cells that are surrounded by a high number (>= 3) of available cells.

        :return: Count of high density cells.
        """
        count = 0
        for row in range(self.board.height):
            for col in range(self.board.width):
                location = (col, row)

                # Check if the cell is occupied or blocked
                if self.board.is_valid_position(*location) and not self.board.is_position_free(location):
                    adjacent_cells = self.get_available_cells(location)

                    # If the cell has 3 or more available adjacent cells
                    if len(adjacent_cells) >= 3:
                        count += 1
        return count

    def heuristic_move_v2(self, current_location, next_location):
        """
        Calculate the heuristic value for moving from current to next location,
        based on the difference in available cells.

        :param current_location: Tuple representing the current location.
        :param next_location: Tuple representing the intended next location.
        :return: Heuristic value of the move.
        """
        current_cells = len(self.get_available_cells(current_location))
        next_cells = len(self.get_available_cells(next_location))

        if current_cells - next_cells > 0:
            return 1
        elif current_cells - next_cells == 0:
            return 0
        else:
            return -1

    def heuristic_token_v2(self, opponent_location):
        """
        Calculate the heuristic value for an opponent's location
        based on change in high-density cells after blocking it.

        :param opponent_location: Tuple representing the opponent's location.
        :return: Heuristic value after blocking the opponent's cell.
        """
        current_density = self.count_high_density_cells()

        # Simulate blocking the opponent's cell
        self.board.block_cell(opponent_location)
        new_density = self.count_high_density_cells()

        # Revert the block simulation
        self.board.unblock_cell(opponent_location)

        # If blocking the cell results in the opponent having no moves, it's a win
        if self.get_available_cells(opponent_location) == 0:
            return 100
        else:
            return new_density - current_density

    def evaluate(self, current_location, opponent_location):
        """
        Evaluate the board's state by summing up the move and token heuristic values.

        :param current_location: Current location of the player's pawn.
        :param opponent_location: Current location of the opponent's pawn.
        :return: Combined heuristic value of the board's state.
        """
        move_value = self.heuristic_move_v2(current_location, opponent_location)
        token_value = self.heuristic_token_v2(opponent_location)

        # Return the total heuristic value
        return move_value + token_value
