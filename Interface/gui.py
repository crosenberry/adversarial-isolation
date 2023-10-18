import tkinter as tk

class IsolationGame:
    """
    IsolationGame - GUI Visual of the Isolation Game.

    This class provides a graphical interface for playing the Isolation Game. The game board is represented
    as a 6x8 grid, with players P1 and P2 starting from fixed positions. Players take turns making a move
    and then blocking any spot on the board. The GUI updates in real-time, displaying each player's moves,
    blocks, and game messages in a side info box.

    Attributes:
        master (tkinter object): The GUI object.
        player (IsolationPlayer object): An instance of the player class responsible for game logic.
        board (IsolationBoard object): An instance of the board class representing the game state.
        p1_position (tuple): Current position of Player 1.
        p2_position (tuple): Current position of Player 2.
        current_player (str): Indicates which player's turn it is ("P1" or "P2").
        is_block_phase (bool): Flag to indicate if the current player is in the block phase.
        buttons (list): A 6x8 list representing the grid buttons.
        info_box (tkinter.Text): Text widget to display game messages and logs.

    Methods:
        end_game(result_message): Ends the game and displays the given result message.
        on_click(i, j): Handles the logic when a button is clicked on the board.
        switch_player(): Switches the active player.
    """

    def __init__(self, master, human_player, ai_player, board):
        self.master = master
        self.human_player = human_player
        self.ai_player = ai_player
        self.board = board
        self.p1_position = (2, 0)
        self.p2_position = (3, 7)
        self.current_player = "P1"
        self.is_block_phase = False

        master.title("Isolation Game")

        # Initialize a 6x8 grid
        self.buttons = [[None for _ in range(8)] for _ in range(6)]

        # Create Text widget for game info
        self.info_box = tk.Text(master, width=30, height=20)
        self.info_box.grid(row=0, column=8, rowspan=6)
        self.info_box.insert(tk.END, "Game started with Player 1's turn!")

        # Initialize Players' positions and set tokens in remaining cells
        for i in range(6):
            for j in range(8):
                self.buttons[i][j] = tk.Button(
                    master,
                    text="O",
                    width=10,
                    height=3,
                    command=lambda x=i, y=j: self.on_click(x, y)
                )
                self.buttons[i][j].grid(row=i, column=j)

        # Setting initial positions for P1 and P2
        self.buttons[self.p1_position[0]][self.p1_position[1]].config(text="P1")
        self.buttons[self.p2_position[0]][self.p2_position[1]].config(text="P2")

    def end_game(self, result_message):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)
        self.info_box.insert(tk.END, f"\nGame Over! {result_message}")

    def on_click(self, i, j):
        if self.current_player == "P1":
            # Check if there are any legal moves left for Player 1
            if not self.human_player.get_legal_moves(self.p1_position, self.p2_position):  # Provide Player 2's position
                self.end_game("Player 2 Wins!")
                return

            if not self.is_block_phase:  # Move Phase for P1
                if self.human_player.make_move(self.p1_position, (i, j), self.p2_position):
                    self.buttons[self.p1_position[0]][self.p1_position[1]].config(text="O")
                    self.p1_position = (i, j)
                    self.buttons[i][j].config(text="P1")
                    self.info_box.insert(tk.END, f"\n{self.current_player} moved to ({i}, {j})")
                    self.is_block_phase = True
            else:  # Block Phase for P1
                if (i, j) not in [self.p1_position, self.p2_position] and self.human_player.make_block((i, j)):
                    self.buttons[i][j].config(text="X")
                    self.buttons[i][j].config(state=tk.DISABLED)
                    self.info_box.insert(tk.END, f"\n{self.current_player} blocked position ({i}, {j})")
                    self.is_block_phase = False
                    self.switch_player()
                    self.info_box.insert(tk.END, f"\n{self.current_player}'s turn!")
                    self.ai_move()  # Invoke AI move immediately after switching to Player 2
        else:
            # Player 2's turn is handled by ai_move()
            pass

    def ai_move(self):
        # AI determines its move
        i, j = self.ai_player.compute_move(self.p2_position, self.p1_position)  # Gets the AI's move

        # Move AI to the new position
        self.buttons[self.p2_position[0]][self.p2_position[1]].config(text="O")
        self.p2_position = (i, j)
        self.buttons[i][j].config(text="P2")
        self.info_box.insert(tk.END, f"\n{self.current_player} moved to ({i}, {j})")

        # Now, for the block phase, AI determines which cell to block
        # NOTE: You will need to implement compute_block method in the AIPlayer class!
        block_i, block_j = self.ai_player.compute_block(self.p2_position,
                                                        self.p1_position)
        self.buttons[block_i][block_j].config(text="X")
        self.buttons[block_i][block_j].config(state=tk.DISABLED)
        self.info_box.insert(tk.END, f"\n{self.current_player} blocked position ({block_i}, {block_j})")

        # Switch back to Player 1 for the next turn
        self.switch_player()
        self.info_box.insert(tk.END, f"\n{self.current_player}'s turn!")

    def switch_player(self):
        if self.current_player == "P1":
            self.current_player = "P2"
        else:
            self.current_player = "P1"
