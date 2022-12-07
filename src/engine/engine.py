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
	print_board(Board)


"""
Create new board
	W = white piece
	B = black piece
	* = void space (not part of board)
	_ = empty space (part of board)

"""
def make_board(no_of_pieces, player_piece, ai_piece):
	length = 2*no_of_pieces - 3
	Board = []
	row_length = no_of_pieces
	void_space = no_of_pieces - 1
	
	for i in range(0, length):
		row = []

		# How much void space do we need
		inner_voidspace = row_length - 1
		outer_voidspace = void_space - inner_voidspace

		# Add void space to start of row
		for j in range(0, math.floor(outer_voidspace/2)):
			row.append("*")

		# Add center of the row (valid board space and inner void space)
		is_void_space = False
		for j in range(0, row_length + inner_voidspace):
			if is_void_space:
				row.append("*")
				is_void_space = False
			else:
				if i == 0:
					row.append(ai_piece)
				elif i == length - 1:
					row.append(player_piece)
				else:
					row.append("_")
				is_void_space = True

		# Add void space to end of row
		for j in range(0, math.floor(outer_voidspace/2)):
			row.append("*")

		# How many valid board space and void space on next row
		if i < math.floor(length / 2):
			row_length -= 1
			void_space += 1
		else:
			row_length += 1
			void_space -= 1

		# Add row to Board
		Board.append(row)

	return Board


"""
Prints out board

Example format for a board with 4 starting pieces:

W W W W
 _ _ _
  _ _ 
 _ _ _
B B B B

"""
def print_board(Board):
	for i in range(0, len(Board)):
		for j in range(0, len(Board[i])):
			if Board[i][j] == "*":
				print(" ", end=" ")
			else:
				print(Board[i][j], end=" ")
		print()