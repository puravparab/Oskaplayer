import math

def engine(player_piece, no_of_pieces):
	if player_piece == "W":
		ai_piece = "B"
	elif player_piece == "B":
		ai_piece = "W"
	else:
		print("Error: Player piece incorrect")
		exit()

	Board = make_board(no_of_pieces, player_piece, ai_piece)
	print(Board)
	print_board(Board)

"""
Create new board
	W = white piece
	B = black piece
	X = void space (not part of board)
	_ = empty space (part of board)

"""
def make_board(no_of_pieces, player_piece, ai_piece):
	length = 2*no_of_pieces - 3

	Board = []
	row_length = no_of_pieces
	for i in range(0, length):
		row = []
		for j in range(0, row_length):
			if i == 0:
				row.append(ai_piece)
			elif i == length - 1:
				row.append(player_piece)
			else:
				row.append("_")
				
		if i < math.floor(length / 2):
			row_length -= 1
		else:
			row_length += 1

		Board.append(row)

	return Board

def print_board(Board):
	for i in range(0, len(Board)):
		for j in range(0, len(Board[i])):
			print(Board[i][j], end=" ")
		print()