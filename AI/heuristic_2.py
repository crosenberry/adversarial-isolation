class IsolationHeuristic2:
    def __init__(self, board_instance):
        self.board = board_instance

    def get_adjacent_cells(self, location):
        x, y = location
        possible_adjacent = [
            (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
            (x, y - 1),                     (x, y + 1),
            (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
        ]
        return [loc for loc in possible_adjacent if self.board.is_valid_position(loc[0], loc[1])]

    def count_high_density_cells(self, board_state):
        count = 0
        for row in range(len(board_state)):
            for col in range(len(board_state[0])):
                location = (row, col)
                if board_state[row][col] != 0:  # Adjusted to check if cell is not empty
                    adjacent_cells = self.get_adjacent_cells(location)
                    if sum(1 for cell in adjacent_cells if board_state[cell[0]][cell[1]] != 0) >= 3:
                        count += 1
        return count

    def heuristic_move_v2(self, current_location, next_location, board_state, get_available_cells_func):
        current_cells = get_available_cells_func(current_location, board_state)
        next_cells = get_available_cells_func(next_location, board_state)

        if current_cells - next_cells > 0:
            return 1
        elif current_cells - next_cells == 0:
            return 0
        else:
            return -1

    def heuristic_token_v2(self, opponent_location, board_state_after_removal, board_state, get_available_cells_func):
        current_density = self.count_high_density_cells(board_state)
        new_density = self.count_high_density_cells(board_state_after_removal)

        if get_available_cells_func(opponent_location, board_state_after_removal) == 0:
            return 100
        else:
            return new_density - current_density

    def evaluate(self, current_location, opponent_location):
        board_after_move = self.board.simulate_move(current_location, opponent_location)
        move_value = self.heuristic_move_v2(current_location, opponent_location, self.board.get_board_state(),
                                            self.get_adjacent_cells)
        token_value = self.heuristic_token_v2(opponent_location, board_after_move, self.board.get_board_state(),
                                              self.get_adjacent_cells)
        return move_value + token_value
