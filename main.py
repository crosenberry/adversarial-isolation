# Calls the GUI component to run the game.
from Interface import gui
from Game_Logic.board import IsolationBoard
from Game_Logic.player import IsolationPlayer
from AI.ai_player import AIPlayer
# =============================================================================
# main.py
# Jacob Yealy & Caden Rosenberry
# Artificial Intelligence
#
# Description:
# Main.py receives an instance of the IsolationBoard and IsolationPlayer.
# Then we tie these objects to the GUI so that it can display the game as its played.
# =============================================================================

if __name__ == "__main__":
    # Create instances of board
    b = IsolationBoard()

    # Pass the board instance to the player
    p1 = IsolationPlayer(b)
    p2 = AIPlayer(b, 3, "heuristic_1")

    # Create an instance of tkinter and run the game
    root = gui.tk.Tk()
    game = gui.IsolationGame(root, p1, p2, b)
    root.mainloop()
