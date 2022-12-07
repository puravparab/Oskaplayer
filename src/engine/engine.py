from . import board

def engine(player_piece, no_of_pieces):
	if player_piece == "W":
		ai_piece = "B"
	elif player_piece == "B":
		ai_piece = "W"
	else:
		print("Error: Player piece incorrect")
		exit()

	Board = board.make_board(no_of_pieces, player_piece, ai_piece)
	board.print_board(Board)