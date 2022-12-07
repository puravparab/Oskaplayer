from engine.engine import *

def oskaplayer():
	print("**Oskaplayer**")
	print("*Implementation by Purav Parab* \n")

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
			break
		else:
			print("Error: please enter either W or B \n")

	engine(player_piece, 4)

if __name__ == "__main__":
	oskaplayer()