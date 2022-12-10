import sys
import unittest

sys.path.insert(0, '..')

from src.engine.board import *

class TestMovePiece(unittest.TestCase):
	def test_human_move_forward(self):
		# Move B to the diagonally adjacent space to its right
		self.assertEqual(
			move_piece([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"B", True, [4,0], [3,1]),
			[[
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', 'B', '*', '_', '*', '_', '*'], 
				['_', '*', 'B', '*', 'B', '*', 'B']],
				"Valid move"
			],
			None
		)

		self.assertEqual(
			move_piece([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', 'B', '*', '_', '*', '_', '*'], 
				['_', '*', 'B', '*', 'B', '*', 'B']],
				"B", True, [3,1], [2,2]),
			[[
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', 'B', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['_', '*', 'B', '*', 'B', '*', 'B']],
				"Valid move"
			],
			None
		)

		# Move W to the diagonally adjacent space to its right
		self.assertEqual(
			move_piece([
				['B', '*', 'B', '*', 'B', '*', 'B'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['W', '*', 'W', '*', 'W', '*', 'W']],
				"W", True, [4,0], [3,1]),
			[[
				['B', '*', 'B', '*', 'B', '*', 'B'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', 'W', '*', '_', '*', '_', '*'], 
				['_', '*', 'W', '*', 'W', '*', 'W']],
				"Valid move"
			],
			None
		)

		# Move B forward to an invalid void space
		self.assertEqual(
			move_piece([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"B", True, [4,0], [3,2]),
			[[
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"Invalid move"
			],
			None
		)

		# Move B forward to space below it
		self.assertEqual(
			move_piece([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"B", True, [4,2], [3,2]),
			[[
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"Invalid move"
			],
			None
		)

		# Make B do a double jump to an empty space
		self.assertEqual(
			move_piece([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"B", True, [4,2], [2,4]),
			[[
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', 'B', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', '_', '*', 'B', '*', 'B']],
				"Valid move"
			],
			None
		)

	def test_ai_move_forward(self):
		# Move W to the diagonally adjacent space to its right
		self.assertEqual(
			move_piece([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"W", False, [0,0], [1,1]),
			[[
				['_', '*', 'W', '*', 'W', '*', 'W'], 
				['*', 'W', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"Valid move"
			],
			None
		)

		self.assertEqual(
			move_piece([
				['_', '*', 'W', '*', 'W', '*', 'W'], 
				['*', 'W', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"W", False, [1,1], [2,2]),
			[[
				['_', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', 'W', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"Valid move"
			],
			None
		)

		# Move B to the diagonally adjacent space to its right
		self.assertEqual(
			move_piece([
				['B', '*', 'B', '*', 'B', '*', 'B'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['W', '*', 'W', '*', 'W', '*', 'W']],
				"B", False, [0,0], [1,1]),
			[[
				['_', '*', 'B', '*', 'B', '*', 'B'], 
				['*', 'B', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['W', '*', 'W', '*', 'W', '*', 'W']],
				"Valid move"
			],
			None
		)

		# Move W forward to an invalid void space
		self.assertEqual(
			move_piece([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"W", False, [0,0], [1,2]),
			[[
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"Invalid move"
			],
			None
		)

		# Move W forward to space below it
		self.assertEqual(
			move_piece([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"W", False, [0,0], [1,0]),
			[[
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"Invalid move"
			],
			None
		)

		# Make W do an double jump to an empty space
		self.assertEqual(
			move_piece([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"W", False, [0,0], [2,2]),
			[[
				['_', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', 'W', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"Valid move"
			],
			None
		)

	def test_out_of_bounds(self):
		# move B player out of bounds
		self.assertEqual(
			move_piece([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"B", True, [4,0], [3,-1]),
			[[
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"Invalid move"
			],
			None
		)

		self.assertEqual(
			move_piece([
				['W', '*', 'B', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['_', '*', 'B', '*', 'B', '*', 'B']],
				"B", True, [0,2], [-1,0]),
			[[
				['W', '*', 'B', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['_', '*', 'B', '*', 'B', '*', 'B']],
				"Invalid move"
			],
			None
		)

		# Select location outside of the board
		self.assertEqual(
			move_piece([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"B", True, [5,0], [4,0]),
			[[
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"Invalid move"
			],
			None
		)

	def test_move_backwards(self):
		# Move B to the downwards
		self.assertEqual(
			move_piece([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', 'B', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', '_', '*', 'B', '*', 'B']],
				"B", True, [2,2], [3,1]),
			[[
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', 'B', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', '_', '*', 'B', '*', 'B']],
				"Invalid move"
			],
			None
		)

		# Move B to the downwards
		self.assertEqual(
			move_piece([
				['W', '*', '_', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', 'W', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"W", False, [2,2], [1,1]),
			[[
				['W', '*', '_', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', 'W', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"Invalid move"
			],
			None
		)

	def test_collisions(self):
		# Move B on to W piece
		self.assertEqual(
			move_piece([
				['W', '*', '_', '*', 'W', '*', 'W'], 
				['*', '_', '*', 'W', '*', '_', '*'], 
				['*', '*', 'B', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', '_', '*', 'B', '*', 'B']],
				"B", True, [2,2], [1,3]),
			[[
				['W', '*', '_', '*', 'W', '*', 'W'], 
				['*', '_', '*', 'W', '*', '_', '*'], 
				['*', '*', 'B', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', '_', '*', 'B', '*', 'B']],
				"Invalid move"
			],
			None
		)

		# Move W on to B piece
		self.assertEqual(
			move_piece([
				['W', '*', '_', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', 'W', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"W", False, [3,3], [4,2]),
			[[
				['W', '*', '_', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', 'W', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"Invalid move"
			],
			None
		)

if __name__ == 'main':
	unittest.main()