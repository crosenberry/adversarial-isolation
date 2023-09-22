#  Defines game board, legal moves, win conditions etc.
class IsolationBoard:
    def __init__(self, width=8, height=6):
        # Initializes the board as a 2D list of 1s
        self.board = [[1 for _ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height

    def occupy_position(self, position):
        """
        Set a position on the board to be occupied (turns the value from 1 to 0).
        :param position: tuple representing the position to occupy (x, y)
        """
        x, y = position
        if self.is_valid_position(x, y) and self.board[y][x] == 1:
            self.board[y][x] = 0
            return True
        return False

    def is_valid_position(self, x, y):
        """
        Check if the given position is within the board boundaries.
        :param x: x-coordinate of the position
        :param y: y-coordinate of the position
        :return: True if the position is valid, False otherwise
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def is_position_free(self, position):
        """
        Check if the given position is free (value of 1).
        :param position: tuple representing the position to check (x, y)
        :return: True if the position is free, False otherwise
        """
        x, y = position
        return self.is_valid_position(x, y) and self.board[y][x] == 1

    def display(self, p1_position, p2_position):
        """ Display the board with both player positions """
        for y, row in enumerate(self.board):
            display_row = []
            for x, cell in enumerate(row):
                if (x, y) == p1_position:
                    display_row.append('P1')
                elif (x, y) == p2_position:
                    display_row.append('P2')
                else:
                    display_row.append(str(cell))
            print(' '.join(display_row))