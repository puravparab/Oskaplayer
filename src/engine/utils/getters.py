# Return a list of coordinates for valid pieces
def get_valid_pieces(Board, curr_player, human_player):
	list_of_pieces = [] 

	# Human players can only move pieces that are not on the first row
	if human_player:
		for i in range(1, len(Board)):
			for j in range(0, len(Board[0])):
				if Board[i][j] == curr_player:
					valid_moves = get_valid_moves(Board, curr_player, f'[{i},{j}]', human_player)
					if valid_moves != []:
						list_of_pieces.append([i,j])

	# AI player can only move pieces that are not on the last row
	elif not human_player:
		for i in range(0, len(Board) - 1):
			for j in range(0, len(Board[0])):
				if Board[i][j] == curr_player:
					valid_moves = get_valid_moves(Board, curr_player, f'[{i},{j}]', human_player)
					if valid_moves != []:
						list_of_pieces.append([i,j])

	return list_of_pieces

# TODO: Add move logic
def get_valid_moves(Board, curr_player, piece_location, human_player):
	list_of_targets = []

	i = int(piece_location[1])
	j = int(piece_location[3])

	if curr_player == "W":
		opponent = "B"
	elif curr_player == "B":
		opponent = "W"

	# Human players can only move upwards
	if human_player:
		# No valid moves if the piece is on the first row
		if i == 0:
			return list_of_targets
		else:
			# Check if the left diagonally adjacent is empty
			if j - 1 >= 0:
				if Board[i-1][j-1] == "_":
					list_of_targets.append([i-1, j-1])
				# Jump over opponent diagonally
				elif Board[i-1][j-1] == opponent:
					if i - 2 >= 0 and j - 2 >= 0 and Board[i-2][j-2] == "_":
						list_of_targets.append([i-2, j-2])

			# Check if the right diagonally adjacent is empty
			if j + 1 < len(Board[0]):
				if Board[i-1][j+1] == "_":
					list_of_targets.append([i-1, j+1])
				# Jump over opponent diagonally
				elif Board[i-1][j+1] == opponent:
					if i - 2 >= 0 and j + 2 < len(Board[0]) and Board[i-2][j+2] == "_":
						list_of_targets.append([i-2, j+2])

	# Ai player can only go downwards
	elif not human_player:
		# No valid moves if the piece is on the last row
		if i == len(Board) - 1:
			return list_of_targets
		else:
			# Check if the left diagonally adjacent is empty
			if j - 1 >= 0:
				if Board[i+1][j-1] == "_":
					list_of_targets.append([i+1, j-1])
				# Jump over opponent diagonally
				elif Board[i+1][j-1] == opponent:
					if i + 2 < len(Board) and j - 2 >= 0 and Board[i+2][j-2] == "_":
						list_of_targets.append([i+2, j-2])

			# Check if the left diagonally adjacent is empty
			if j + 1 < len(Board[0]):
				if Board[i+1][j+1] == "_":
					list_of_targets.append([i+1, j+1])
				# Jump over opponent diagonally
				elif Board[i+1][j+1] == opponent:
					if i + 2 < len(Board) and j + 2 < len(Board[0]) and Board[i+2][j+2] == "_":
						list_of_targets.append([i+2, j+2])
	
	return list_of_targets