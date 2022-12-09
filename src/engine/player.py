import copy
from .utils import getters

# Handles game logic for human player's turn
def player_turn(Board, curr_player):
	board_copy = copy.deepcopy(Board)

	# Ask user to choose a piece and where to move it
	while True:
		selected_piece = input("Select piece to move (enter co-ordinates): ")

		print(getters.get_valid_pieces(board_copy, curr_player, True))

		target_location = input("Select a target location (enter co-ordinates): ")

		user_confirmation = input(
			"Are you sure you want to move W from " + selected_piece + " to " + target_location + "? (Y or N): ")

		if user_confirmation == "Y":
			break

		print('\n')

	return board_copy