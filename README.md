<p align="center">
</p>

<p align="center">
	<h1 align="center">
		OSKAPLAYER
	</h1>
	<p align="center">
	    The board game Oska featuring an AI opponent running minimax with alpha-beta pruning
	</p
</p>

<p align="center">
    <a href="#How it works">Overview</a>
	&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
	<a href="#Rules">RULES</a>
	&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
	<a href="#Installation">INSTALLATION</a>
</p>

# Overview
Oska is played on a board like the one shown below. The two players face each other across the
board. Each player begins with n pieces, with all of the player pieces on placed on the row closest to them.

Oskaplayer is an implementation of the board game with one human player facing an AI opponent. The AI opponent plays the game using [minimax][minimax-link] with [alpha-beta pruning][alpha-beta-link] to find the most optimal move to play.
```
   0 1 2 3 4 5 6
0  W   W   W   W
1    _   _   _
2      _   _
3    _   _   _
4  B   B   B   B
```

# Rules
* #### Opening
    The player with the whte piece moves first and players alternate moves after that.

* #### Movement
    A piece may be moved forward on the diagonal, one space at a time, to an empty space.

* #### Capturing
    A piece may jump forward on the diagonal over an opponent's piece to an empty space, thereby capturing the opponent's piece and removing it from the board. Multiple jumps are not allowed. Also, even if a capture is possible, it does not have to be made if other moves are possible.

* #### Endgame (Win)
    A player wins if all of the opponent's pieces have been removed from the board. A player can also win if all of their remaining pieces have been moved to the opponent's starting row. (A player may want to sacrifice pieces in order to have fewer pieces to move to the opponent's starting row. But this approach carries some risk in that every sacrificed piece brings the player closer to having all of his or her pieces removed from the board, thereby losing the game.)

* #### Endgame (Loss)
    A player might lose if they have no remaining pieces left. A player may also lose if the opponent has met the above win conditions.

* #### Endgame (Win)
    Stalemate occurs if a player has no legal moves left.

# Installation

Clone the respository
```
https://github.com/puravparab/Oskaplayer.git
```
Change the working directory to Chattrr
```
cd Oskaplayer
```
Install pipenv to your machine
```
pip install --user pipenv
```
Install dependencies from Pipfile
```
pipenv sync
```
Run the virtual environment
```
pipenv shell
```
Run the game
```
cd src
python oskaplayer.py
```

---

[oska-link]: https://boardgamegeek.com/boardgame/19495/oska
[minimax-link]: https://en.wikipedia.org/wiki/Minimax
[alpha-beta-link]: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning