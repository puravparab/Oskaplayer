from . import board, board_evaluator, player
from .ai.player import *

def engine(player_piece, no_of_pieces):
	if player_piece == "W":
		ai_piece = "B"
	elif player_piece == "B":
		ai_piece = "W"
	else:
		print("Error: Player piece incorrect")
		exit()

	# Create new board
	Board = board.make_board(no_of_pieces, player_piece, ai_piece)
	board.print_board(Board)

	Board_new = Board
	if player_piece == "W":
		while True:
			# Test player turn:
			Board_new = player.player_turn(Board_new, player_piece)
			board.print_board(Board_new)
			
			# Test AI turn:
			Board_new = ai_player(Board_new, ai_piece, False, 2)
			board.print_board(Board_new)

	else:
		while True:			
			# Test AI turn:
			Board_new = ai_player(Board_new, ai_piece, False, 2)
			board.print_board(Board_new)

			# Test player turn:
			Board_new = player.player_turn(Board_new, player_piece)
			board.print_board(Board_new)