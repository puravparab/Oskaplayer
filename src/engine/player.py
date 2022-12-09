import copy
from .utils import getters, validators

# Handles game logic for human player's turn
def player_turn(Board, curr_player):
	board_copy = copy.deepcopy(Board)

	# Ask user to choose a piece and where to move it
	while True:
		# User selects the piece they want to play
		while True:
			# Get valid pieces
			valid_pieces = getters.get_valid_pieces(board_copy, curr_player, True)
			print("Choose from the following pieces - " + str(valid_pieces))
			selected_piece = input("Enter the coordinates of the piece you want to move: ")
			print()

			# Validate if the user selected piece is valid
			# If not repeat loop until valid piece is selected
			if validators.valid_coordinate(valid_pieces, selected_piece):
				break
			else:
				print("<Error!: Please enter coordinates in the format [a,b]>")

		target_location = input("Select a target location (enter co-ordinates): ")

		user_confirmation = input(
			"Are you sure you want to move W from " + selected_piece + " to " + target_location + "? (Y or N): ")

		if user_confirmation == "Y":
			break

		print('\n')

	return board_copy