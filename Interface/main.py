import tkinter as tk

class IsolationGame:
    def __init__(self, master):
        self.master = master
        master.title("Isolation Game")

        # Initialize a 6x8 grid
        self.buttons = [[None for _ in range(8)] for _ in range(6)]

        # Initialize Players' positions and set tokens in remaining cells
        for i in range(6):
            for j in range(8):
                if i == 2 and j == 0:  # Player 1 starting position
                    self.buttons[i][j] = tk.Button(master, text="P1", width=10, height=3)
                elif i == 3 and j == 7:  # Player 2 starting position on the opposite side
                    self.buttons[i][j] = tk.Button(master, text="P2", width=10, height=3)
                else:  # All other cells with tokens
                    self.buttons[i][j] = tk.Button(master, text="O", width=10, height=3)

                self.buttons[i][j].grid(row=i, column=j)

    def start_game(self):
        pass  # Your game logic goes here


root = tk.Tk()
game = IsolationGame(root)
root.mainloop()
