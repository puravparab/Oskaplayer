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