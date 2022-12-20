import copy

from .. import board
from .. utils import getters, validators
from .minimax import *

# Handles game logic for ai player's turn
def ai_player(Board, curr_player, human_player, depth):
	board_copy = copy.deepcopy(Board)

	valid_pieces = getters.get_valid_pieces(board_copy, curr_player, human_player)
	print(valid_pieces)

	[optimal_move, score] = minimax(board_copy, curr_player, human_player, valid_pieces, depth, True)

	print(optimal_move)

	[board_copy, msg] = board.move_piece(
		board_copy, 
		curr_player, 
		human_player,
		[optimal_move[0][0], optimal_move[0][1]],
		[optimal_move[1][0], optimal_move[1][1]]
	)

	return board_copy