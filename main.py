# Calls the GUI component to run the game.
from Interface import gui
from Game_Logic import player
from Game_Logic import board


if __name__ == "__main__":
    # Create instances of player and board
    p = player.IsolationPlayer()
    b = board.IsolationBoard()

    # Create an instance of tkinter's root and run the game
    root = gui.tk.Tk()
    game = gui.IsolationGame(root, p, b)
    root.mainloop()