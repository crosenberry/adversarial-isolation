# Calls the GUI component to run the game.
from Interface import gui
from Game_Logic.board import IsolationBoard
from Game_Logic.player import IsolationPlayer

if __name__ == "__main__":
    # Create instances of board first
    b = IsolationBoard()

    # Then, pass the board instance to the player
    p = IsolationPlayer(b)

    # Create an instance of tkinter's root and run the game
    root = gui.tk.Tk()
    game = gui.IsolationGame(root, p, b)
    root.mainloop()