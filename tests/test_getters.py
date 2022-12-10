import sys
import unittest

sys.path.insert(0, '..')

from src.engine.utils.getters import *

class TestValidMoves(unittest.TestCase):
	def test_get_valid_moves_human(self):
		# Move B from back row
		self.assertEqual(
			get_valid_moves([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"B", "[4,0]", True
			),
			[[3,1]]
		)

		self.assertEqual(
			get_valid_moves([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"B", "[4,2]", True
			),
				[[3,1], [3,3]]
		)

		# Move B from the center of the board
		self.assertEqual(
			get_valid_moves([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', 'B', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', '_', '*', 'B', '*', 'B']],
				"B", "[2,2]", True
			),
				[[1,1], [1,3]]
		)

		# Move B from the front row
		self.assertEqual(
			get_valid_moves([
				['W', '*', 'B', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', '_', '*', 'B', '*', 'B']],
				"B", "[0,2]", True
			),
				[]
		)

		# B is blocked by other B pieces
		self.assertEqual(
			get_valid_moves([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', 'B', '*', 'B', '*', '*'],
				['*', '_', '*', 'B', '*', '_', '*'], 
				['B', '*', '_', '*', '_', '*', '_']],
				"B", "[3,3]", True
			),
			[]
		)

	def test_get_valid_moves_ai(self):
		# Move W from front row
		self.assertEqual(
			get_valid_moves([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"W", "[0,0]", False
			),
			[[1,1]]
		)

		self.assertEqual(
			get_valid_moves([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"W", "[0,2]", False
			),
				[[1,1], [1,3]]
		)

		# Move w from the center of the board
		self.assertEqual(
			get_valid_moves([
				['W', '*', 'W', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', 'W', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', '_', '*', 'B', '*', 'B']],
				"W", "[2,2]", False
			),
				[[3,1], [3,3]]
		)

		# Move W from the back row
		self.assertEqual(
			get_valid_moves([
				['W', '*', '_', '*', 'W', '*', 'W'], 
				['*', '_', '*', '_', '*', '_', '*'], 
				['*', '*', '_', '*', '_', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'W', '*', 'B', '*', 'B']],
				"W", "[4,2]", False
			),
				[]
		)

		# W is blocked by other B pieces
		self.assertEqual(
			get_valid_moves([
				['_', '*', '_', '*', '_', '*', 'W'], 
				['*', '_', '*', 'W', '*', '_', '*'], 
				['*', '*', 'W', '*', 'W', '*', '*'],
				['*', '_', '*', '_', '*', '_', '*'], 
				['B', '*', 'B', '*', 'B', '*', 'B']],
				"W", "[1,3]", False
			),
			[]
		)

if __name__ == "main":
	unittest.main()