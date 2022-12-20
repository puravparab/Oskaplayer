import copy, math
from .. import board, board_evaluator
from .. utils import getters, validators

"""
MINIMAX ALGORITHM

Parameters:
	1) Board:  Current Board state
	2) curr_player: Piece to be player (W or B)
	3) human_player: Is the curr_player a human
	4) valid_pieces: List of valid pieces
	5) depth: How far should the minimax search go (depth = 1 includes max and min steps)
	6) is_max: Should this minimax step select maximum score

Returns:
	1) optimal_move: An array containing a piece coordinate and the move coordinate
	2) score: Score of the optimal move

"""
def minimax(Board, curr_player, human_player, valid_pieces, depth, is_max):
	move_permutations = []
	if depth > 0:
		for i in range(0, len(valid_pieces)):
			piece_coordinate = str(valid_pieces[i]).replace(" ", "")
			valid_targets = getters.get_valid_moves(Board, curr_player, piece_coordinate, human_player)
			print("Valid targets for " + curr_player + ": " + str(valid_targets))
			for j in range(0, len(valid_targets)):
				board_copy = copy.deepcopy(Board)
				[board_copy, msg] = board.move_piece(
					board_copy, 
					curr_player, 
					human_player,
					[valid_pieces[i][0], valid_pieces[i][1]], 
					[valid_targets[j][0], valid_targets[j][1]]
				)

				board.print_board(board_copy)

				if curr_player == "W": 
					opponent = "B"
				elif curr_player == "B":
					opponent = "W"

				valid_pieces_next_move = getters.get_valid_pieces(board_copy, opponent, not human_player)
				[optimal_move, score] = minimax(board_copy, opponent, not human_player, valid_pieces_next_move, depth-1, not is_max)

				print(str(valid_pieces[i]) + " to " + str(valid_targets[j]) + ": " + str(score))
				move_permutations.append([[valid_pieces[i], valid_targets[j]], score])

				print("------------")
				print()

		print("Depth: " + str(depth))
		print("Running max? " + str(is_max))

		# Find move with the maximum or minimum score
		max_index = 0
		current_max = -math.inf
		min_index = 0
		current_min = math.inf

		for i in range(0, len(move_permutations)):
			print(move_permutations[i])
			if is_max:
				if current_max < move_permutations[i][1]:
					current_max = move_permutations[i][1]
					max_index = i
			else:
				if current_min > move_permutations[i][1]:
					current_min = move_permutations[i][1]
					min_index = i

		if is_max: 
			print("Optimal move: " + str([move_permutations[max_index][0], move_permutations[max_index][1]]))
			return [move_permutations[max_index][0], move_permutations[max_index][1]]
		else:
			print("Optimal move: " + str([move_permutations[min_index][0], move_permutations[min_index][1]]))
			return [move_permutations[min_index][0], move_permutations[min_index][1]]

	elif depth == 0:
		score = board_evaluator.evaluator(Board, curr_player, human_player)
		return [[], score]

