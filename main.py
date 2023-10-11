# Calls the GUI component to run the game.
from Interface import gui
from Game_Logic.board import IsolationBoard
from Game_Logic.player import IsolationPlayer

if __name__ == "__main__":
    # Create instances of board
    b = IsolationBoard()

    # Pass the board instance to the player
    p = IsolationPlayer(b)

    # Create an instance of tkinter and run the game
    root = gui.tk.Tk()
    game = gui.IsolationGame(root, p, b)
    root.mainloop()