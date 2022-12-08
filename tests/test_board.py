import sys
import unittest

sys.path.insert(0, '..')

from src.engine.board import *

class TestMovePiece(unittest.TestCase):
	def test(self):

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

if __name__ == 'main':
	unittest.main()