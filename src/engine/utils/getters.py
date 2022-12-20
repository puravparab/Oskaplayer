# Return a list of coordinates for valid pieces
def get_valid_pieces(Board, curr_player, human_player):
	list_of_pieces = [] 

	# Human players can only move pieces that are not on the first row
	if human_player:
		for i in range(1, len(Board)):
			for j in range(0, len(Board[0])):
				if Board[i][j] == curr_player:
					list_of_pieces.append([i,j])

	# AI player can only move pieces that are not on the last row
	elif not human_player:
		for i in range(0, len(Board) - 1):
			for j in range(0, len(Board[0])):
				if Board[i][j] == curr_player:
					list_of_pieces.append([i,j])

	return list_of_pieces

# TODO: Add move logic
def get_valid_moves(Board, curr_player, piece_location, human_player):
	list_of_targets = []

	i = int(piece_location[1])
	j = int(piece_location[3])

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
				# Add jumping over opponent

			# Check if the right diagonally adjacent is empty
			if j + 1 < len(Board[0]):
				if Board[i-1][j+1] == "_":
					list_of_targets.append([i-1, j+1])
				# Add jumping over opponent

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
				# Add jumping over opponent

			# Check if the left diagonally adjacent is empty
			if j + 1 < len(Board[0]):
				if Board[i+1][j+1] == "_":
					list_of_targets.append([i+1, j+1])
				# Add jumping over opponent
	
	return list_of_targets