# Tic-Tac-Toe-Minimax-Game
This is a TicTacToe Game that  uses Minimax Algorithm 

INTRODUCTION 

The game tic-tac-toe, including a simple computer player. The game is played on a 3 × 3 board; the human player goes first and places an “X” on the board, then the computer places an “O”, and so on, until either one player gets three in a row (a winning position) or there are no more moves (a draw).
OBJECTIVE

This game is very popular and is fairly simple by itself. It is actually a two player game. In this game, there is a board with n x n squares. In our game, it is 3 x 3 squares. The goal of Tic-Tac-Toe is to be one of the players (Human or Computer) to get three same symbols in a row - horizontally, vertically or diagonally - on a 3 x 3 grid. 

THEORY OF THE GAME:

A player can choose between two symbols with his opponent, usual games use “X”and “O”. If first player choose “X” then the second player have to play with “O” and vice versa. 
A player marks any of the 3x3 squares with his symbol (may be “X” or “O”) and his aim is to create a straight line horizontally or vertically or diagonally with two intensions: 
	a) Create a straight line before his opponent to win the game. 
	b) Restrict his opponent from creating a straight line first. 
In case logically no one can create a straight line with his own symbol, the game results a tie. Hence there are only three possible results – a player wins, his opponent (computer) wins or it’s a draw.

THE PROBLEM

Your task in this project is to implement the game tic-tac-toe, including an undefeatable computer player. The game is played on a 3 × 3 board; the human player goes first or second and places an “X” on the board, then the computer places an “O”, and so on, until either one player gets three in a row (a winning position) or there are no more moves (a draw).

ANALYSIS OF THE MINIMAX FUNCTIONS

The key to the Minimax algorithm is a back and forth between the two players, where the player whose "turn it is" desires to pick the move with the maximum score. In turn, the scores for each of the available moves are determined by the opposing player deciding which of its available moves has the minimum score. And the scores for the opposing players’ moves are again determined by the turn-taking player trying to maximize its score and so on all the way down the move tree to an end state.
A description for the algorithm, assuming X is the "turn taking player," would look something like:
•	If the game is over, return the score from X's perspective.

•	Otherwise get a list of new game states for every possible move

•	Create a scores list

•	For each of these states add the minimax result of that state to the scores list

•	If it's X's turn, return the maximum score from the scores list

•	If it's O's turn, return the minimum score from the scores list


CONCLUSION

In this project, I implemented a Tic Tac Toe in version of the minimax algorithm, Creating this algorithm that is perfect and will never loose. This algorithm will walk through all the different game states and look into the future. We have to carefully craft it so it always selects the best move.
