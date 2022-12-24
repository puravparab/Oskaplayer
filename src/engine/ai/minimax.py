import copy, math
from .. import board, board_evaluator
from .. utils import getters, validators

# NODE Class
class Node:
	def __init__(self, score, nodeList, parentNode, Board):
		self.score = score
		self.nodeList = nodeList
		self.parentNode = parentNode
		self.Board = Board
		self.optimal_move = []

"""
MINIMAX ALGORITHM

Params:
	- Board: Current board state
	- curr_node: current node
	- curr_player: current player (W or B)
	- human_player: Is the current player a human?
	- valid_places: List of valid pieces
	- depth: current depth
	- max_depth: maximum depth allowed
	- is_max: should the minimax algorithm choose the maximum score?

Returns:
	- optimal_move: An array containing the piece location and target location of the optimal move
	- score: Score of the optimal move

"""
def minimax(Board, curr_node, curr_player, human_player, valid_pieces, depth, max_depth, is_max):
	# If leaf node is reached
	if depth == max_depth:
		return [[], board_evaluator.evaluator(Board, curr_player, human_player)]

	nodeList = []
	move_permutations = []

	for i in range(0, len(valid_pieces)):
		piece_coordinate = str(valid_pieces[i]).replace(" ", "")
		# Get all valid moves for a specific piece
		valid_targets = getters.get_valid_moves(Board, curr_player, piece_coordinate, human_player)

		# Iterate through all valid moves for specific piece
		for j in range(0, len(valid_targets)):
			board_copy = copy.deepcopy(Board)
			# Move piece on the board
			[board_copy, msg] = board.move_piece(
					board_copy, 
					curr_player, 
					human_player,
					[valid_pieces[i][0], valid_pieces[i][1]], 
					[valid_targets[j][0], valid_targets[j][1]]
				)

			# Create new child node
			child_node = Node(None, [], curr_node, board_copy)

			if curr_player == "W": 
				opponent = "B"
			elif curr_player == "B":
				opponent = "W"

			# Get valid pieces for the opponent on new board state
			valid_pieces_next_move = getters.get_valid_pieces(board_copy, opponent, not human_player)
			if valid_pieces_next_move != []:
				# If valid pieces exist execute minimax on new board state
				[optimal_move, score] = minimax(board_copy, child_node, opponent, not human_player, valid_pieces_next_move, depth+1, max_depth, not is_max)
				child_node.optimal_move.append(optimal_move)
			else:
				score = board_evaluator.evaluator(board_copy, opponent, not human_player)
				child_node.optimal_move.append([])
				
			child_node.score = score
			curr_node.nodeList.append(child_node)
			# Store moves and their respective scores
			move_permutations.append([[valid_pieces[i], valid_targets[j]], score])

	# Find move with the maximum or minimum score
	max_index = 0
	current_max = -math.inf
	min_index = 0
	current_min = math.inf

	# Iterate through all possible branches an pick the most optimal one using minimax
	for i in range(0, len(move_permutations)):
		# MAX
		if is_max:
			if current_max < move_permutations[i][1]:
				current_max = move_permutations[i][1]
				curr_node.score = current_max
				max_index = i
		# MIN
		else:
			if current_min > move_permutations[i][1]:
				current_min = move_permutations[i][1]
				curr_node.score = current_min
				min_index = i

	# Return optimal move and score found using minimax for this node
	if is_max:
		return [move_permutations[max_index][0], move_permutations[max_index][1]]
	else:
		return [move_permutations[min_index][0], move_permutations[min_index][1]]