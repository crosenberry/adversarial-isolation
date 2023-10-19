# Adversarial-Isolation
Isolation Game Using Adversarial Search  
Jacob Yealy & Caden Rosenberry  
Artificial Intelligence  

## Table of Contents
- [Introduction](#Introduction)
- [Instructions](#instructions)
- [Gameplay](#Gameplay)
- [How to win](#win-conditions)
- [Heuristics](#Heuristics)

## Introduction
- Isolation or Isola is a German boardgame from the 1970’s. The game is for two players. Each player
tries to isolate their opponent’s pawn
- The gameboard is a 6x8 grid with starting positions for each player marked on the third cell on the left
of each short side. 
- The remaining 46 cells are filled with tokens indicating that the cell could be visited
by a player.


## Instructions
- To play the game, run [main.py](main.py).
- Player 1 will begin each game, able to move one space around them and then block one space on the board.  
- Then, player 2 will do the same and turns will rotate until one player cannot move anymore, thus making them in "Isolation"
- Player 2 can be controlled by another human or by the algorithms implemented in this program.
- For legal game moves and board functionality testing, reference [Game_Logic](Game_Logic).
- To examine the heuristics used by the other player, examine [AI](AI).

## Gameplay
- The first player is chosen randomly. A player moves its pawn one cell up, down, left, right, or
diagonally from their current position to an available cell.
- An available cell still has a token in it and
does not contain the other player.
- Then the player chooses any available cell and removes the token.
This means that no player can move to that cell in a future move.


## Heuristics
Two heuristics will be used to design the game.  
The heuristics determine how the AI player plays the game.  
To change which heuristic you'd like to play against, change it in [main.py](main.py)  
- Heuristic 1 can be chosen using "heuristic_1"
- Heuristic 2 can be chosen using "heuristic_2"


