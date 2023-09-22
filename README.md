# Adversarial-Isolation
Isolation Game Using Adversarial Search  
Jacob Yealy & Caden Rosenberry  
Artificial Intelligence  

## Table of Contents
- [Introduction](#Introduction)  
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


## Gameplay
- The first player is chosen randomly. A player moves its pawn one cell up, down, left, right, or
diagonally from their current position to an available cell.
- An available cell still has a token in it and
does not contain the other player.
- Then the player chooses any available cell and removes the token.
This means that no player can move to that cell in a future move.

## Win Conditions
- The first player to isolate their opponent wins the game. A player is isolated when there are no
available squares that the player can move their pawn to


## Heuristics
Three heuristics will be used to design the game.  

### Heuristic 1:
### Heuristic 2:
### Heuristic 3:

