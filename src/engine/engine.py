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

	run_game(player_piece, ai_piece, no_of_pieces)

def run_game(player_piece, ai_piece, no_of_pieces):
	# Create new game board
	Board = board.make_board(no_of_pieces, player_piece, ai_piece)

	count = 1
	if player_piece == "W":
		human_player = True
	elif ai_piece == "W":
		human_player = False

	while True:
		print()
		if human_player:
			print(f'** Turn {count} - Player {player_piece} **')
			board.print_board(Board)
			Board_new = player.player_turn(Board, player_piece)

		else:
			print(f'Turn {count} - Player {ai_piece}')
			board.print_board(Board)
			Board_new = ai_player(Board, ai_piece, False, 5)

		if Board_new != None:
			Board = Board_new
			winner = board_evaluator.win_check(Board, player_piece, ai_piece)
			if winner == player_piece:
				print(f'Congratulations! You won.')
			elif winner == ai_piece:
				print(f'You lost. :(')
			else:
				print("The game ended in a stalemate.")

		else:
			if board_evaluator.win_check(Board, player_piece, ai_piece) == player_piece:
				print(f'Congratulations! You won.')
				return
			elif board_evaluator.win_check(Board, player_piece, ai_piece) == ai_piece:
				print(f'You lost. :(')
				return
			else:
				print("The game ended in a stalemate.")
				return

		human_player = not human_player
		count += 1