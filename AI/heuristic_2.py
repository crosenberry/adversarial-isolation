def get_adjacent_cells(location):
    x, y = location
    # List possible adjacent locations.
    # You may need to adjust this if movement is restricted by the board boundaries.
    possible_adjacents = [
        (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
        (x, y - 1),                     (x, y + 1),
        (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
    ]
    return [loc for loc in possible_adjacents if 0 <= loc[0] < 6 and 0 <= loc[1] < 8]  # Ensure valid board locations


def count_high_density_cells(board_state):
    count = 0
    for row in range(len(board_state)):
        for col in range(len(board_state[0])):
            location = (row, col)
            if board_state[row][col]:  # If the cell is not empty
                adjacent_cells = get_adjacent_cells(location)
                if sum(1 for cell in adjacent_cells if board_state[cell[0]][cell[1]]) >= 3:
                    count += 1
    return count


def heuristic_move_v2(current_location, next_location, board_state, get_available_cells_func):
    current_cells = get_available_cells_func(current_location, board_state)
    next_cells = get_available_cells_func(next_location, board_state)

    if current_cells - next_cells > 0:
        return 1
    elif current_cells - next_cells == 0:
        return 0
    else:
        return -1


def heuristic_token_v2(opponent_location, board_state_after_removal, board_state, get_available_cells_func):
    current_density = count_high_density_cells(board_state)
    new_density = count_high_density_cells(board_state_after_removal)

    if get_available_cells_func(opponent_location, board_state_after_removal) == 0:
        return 100
    else:
        return new_density - current_density
# Implements the second heuristic for the adversarial isolation game
