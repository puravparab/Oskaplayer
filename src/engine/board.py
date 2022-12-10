import math
import copy

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

	for i in range(0, len(Board[0]) + 1):
		if(i == 0):
			print(" ", end=" ")
		else:
			print(i - 1, end=" ")
	print()

	for i in range(0, len(Board)):
		print(i, end=" ")
		for j in range(0, len(Board[i])):
			if Board[i][j] == "*":
				print(" ", end=" ")
			else:
				print(Board[i][j], end=" ")
		print()
	print("\n")


"""
Moves piece to valid location

Function assumes that input is in this format:
[
	['B', '*', 'B', '*', 'B', '*', 'B'], 
	['*', '_', '*', '_', '*', '_', '*'], 
	['*', '*', '_', '*', '_', '*', '*'], 
	['*', '_', '*', '_', '*', '_', '*'], 
	['W', '*', 'W', '*', 'W', '*', 'W']]

where
	W = white piece
	B = black piece
	* = void space (not part of board)
	_ = empty space (part of board)

"""
def move_piece(Board, curr_player, human_player, curr_location, desired_location):
	# Make a deepcopy of the board
	Board_copy = copy.deepcopy(Board)

	# Check if curr_location or desired_location is out of bounds
	if (
		curr_location[0] >= 0 and curr_location[0] < len(Board) and
		curr_location[1] >= 0 and curr_location[1] < len(Board[0]) and
		desired_location[0] >= 0 and desired_location[0] < len(Board) and
		desired_location[1] >= 0 and desired_location[1] < len(Board[0])
	):

		# Store value at both locations
		at_curr_location = Board[curr_location[0]][curr_location[1]]
		at_desired_location = Board[desired_location[0]][desired_location[1]]

		# Check if current location has the curr_player piece on it and 
		# if desired location has the "_" char
		if at_curr_location == curr_player and at_desired_location == "_":

			# Check if the targeted piece will move in the right direction
			# (Upwards for a human player and downwards for the AI player)
			# 
			# Also checks if the piece moves to an diagonally adjacent empty space
			if (
				((human_player and curr_location[0] > desired_location[0]) or
				(not human_player and curr_location[0] < desired_location[0]))
				and
				(curr_location[1] == desired_location[1] + 1 or curr_location[1] == desired_location[1] - 1)):

				Board_copy[curr_location[0]][curr_location[1]] = "_"
				Board_copy[desired_location[0]][desired_location[1]] = curr_player
				return [Board_copy, "Valid move"]
				
	return [Board_copy, "Invalid move"]