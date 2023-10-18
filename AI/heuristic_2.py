class IsolationHeuristic2:
    def __init__(self, board_instance):
        self.board = board_instance

    def get_available_cells(self, location):
        x, y = location
        legal_moves = []
        # Define possible moves in each direction, including diagonals
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if self.board.is_valid_position(new_x, new_y) and self.board.is_position_free((new_x, new_y)):
                legal_moves.append((new_x, new_y))

        return legal_moves

    def count_high_density_cells(self):
        count = 0
        for row in range(self.board.height):
            for col in range(self.board.width):
                location = (col, row)
                if self.board.is_valid_position(*location) and not self.board.is_position_free(location):  # Check if cell is occupied or blocked
                    adjacent_cells = self.get_available_cells(location)
                    if len(adjacent_cells) >= 3:
                        count += 1
        return count

    def heuristic_move_v2(self, current_location, next_location):
        current_cells = len(self.get_available_cells(current_location))
        next_cells = len(self.get_available_cells(next_location))

        if current_cells - next_cells > 0:
            return 1
        elif current_cells - next_cells == 0:
            return 0
        else:
            return -1

    def heuristic_token_v2(self, opponent_location):
        current_density = self.count_high_density_cells()
        # Simulate blocking the cell
        self.board.block_cell(opponent_location)
        new_density = self.count_high_density_cells()
        # Revert the block simulation
        self.board.unblock_cell(opponent_location)

        if self.get_available_cells(opponent_location) == 0:
            return 100
        else:
            return new_density - current_density

    def evaluate(self, current_location, opponent_location):
        move_value = self.heuristic_move_v2(current_location, opponent_location)
        token_value = self.heuristic_token_v2(opponent_location)
        return move_value + token_value
