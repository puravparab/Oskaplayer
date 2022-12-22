"""
Scoring Algorithm:

A: Current player
B: Opponent player

Step 1) 
	For each row:
		# of A pieces in the row * (relative index) ^ 2

	Sum the above values for each row -> sumA 

Step 2)
	Repeat step 1 for B player -> sumB

Step 3)
	# of B pieces - # of A pieces -> diffBA

Step 4)
	Score = (Total - # of A pieces) * sumA - (Total - # of B pieces) * sumB + diffBA

Score:
	+ve: Move favors A
	-ve: Move favors B
	0: Move does not favor any player
	
"""
def evaluator(Board, curr_player, human_player):
	length = len(Board)

	A_list = [0] * length
	B_list = [0] * length
	# Total count of A and B pieces on the board
	A_count = 0
	B_count = 0

	# Iterate through the board and count no of pieces for each player
	for i in range(0, length):
		A_per_row = 0
		B_per_row = 0
		for j in range(0, len(Board[0])):
			value = Board[i][j]

			if value == "W" or value =="B":
				if value == curr_player:
					A_per_row += 1
					A_count += 1
				if value != curr_player:
					B_per_row += 1
					B_count += 1

		# Add no of pieces to relative index in the list
		if human_player:
			A_list[length-i-1] = A_per_row
			B_list[i] = B_per_row
		else:
			A_list[i] = A_per_row
			B_list[length-i-1] = B_per_row


	total_pieces = A_count + B_count
	# Calculate sumA and sumB:
	sumA = 0
	sumB = 0
	for i in range(0, length):
		sumA += A_list[i] * pow(i, 2)
		sumB += B_list[i] * pow(i, 2)

	# Calculate diffBA:
	diffBA = B_count - A_count

	# Calculate score:
	score = (B_count * sumA) - (A_count * sumB) + diffBA
	return score

"""
Function takes in the board state and current player and determines if they have won
"""
def win_check(Board, curr_player):
	count = 0
	for i in range(0, len(Board)):
		for j in range(0, len(Board[0])):
			if curr_player == "B":
				if i == len(Board) - 1 and count > 0:
					return False
				if Board[i][j] == "B":
					count += 1

			if curr_player == "W":
				if i > 0 and Board[i][j] == "W":
					return False
				if Board[i][j] == "W":
					count += 1

	return True