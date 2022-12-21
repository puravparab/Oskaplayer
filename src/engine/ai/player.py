import copy, time
from .. import board
from .. utils import getters, validators
from .minimax import *

# Handles game logic for ai player's turn
def ai_player(Board, curr_player, human_player, depth):
	board_copy = copy.deepcopy(Board)

	# Get valid pieces for the AI to move:
	valid_pieces = getters.get_valid_pieces(board_copy, curr_player, human_player)
	# If there are no valid pieces return None
	if valid_pieces == []:
		return None

	print(valid_pieces)

	t = time.process_time()
	# Run Minimax to get an optimal move for the AI
	[optimal_move, score] = minimax(board_copy, curr_player, human_player, valid_pieces, depth, True)
	elapsed_time = time.process_time() - t 
	print(f'Time elapsed (Depth: {depth}): {elapsed_time}')
	print(f'Optimal Move: {optimal_move}')

	# If there is no optimal move return None
	if optimal_move == None:
		return None

	# Execute optimal move on the board
	[board_copy, msg] = board.move_piece(
		board_copy, 
		curr_player, 
		human_player,
		[optimal_move[0][0], optimal_move[0][1]],
		[optimal_move[1][0], optimal_move[1][1]]
	)

	return board_copy