from engine.engine import *

def oskaplayer():
	print("**Oskaplayer**")
	print("*Implementation by Purav Parab* \n")

	while(True):
		# Player chooses the color of his piece
		# White plays first
		# Black plays second
		player_piece = ""
		while(True):
			player_piece = input("Choose a color White(W) or Black(B):")
			if player_piece == 'W' or player_piece == 'B':
				player_list = {
					"W": "White",
					"B": "Black" 
				}
				print("You will play as " + player_list[player_piece] + "!\n")

				# Prompt user for no of starting pieces
				no_of_pieces = int(input("Enter the number of starting pieces: "))
				break
			else:
				print("<Error: please enter either W or B> \n")

		# Run oskaplayer game engine
		engine(player_piece, no_of_pieces)

		# Check if user wants to restart the game
		while(True):
			user_input = input("Play another game? (Enter Y for Yes or N for No): ")
			if user_input == 'Y':
				break
			elif user_input == 'N':
				exit()
			else:
				print("<Error: please enter either Y or N> \n")

if __name__ == "__main__":
	oskaplayer()