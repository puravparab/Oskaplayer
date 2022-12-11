import sys
import unittest

sys.path.insert(0, '..')

from src.engine.utils.validators import *

class TestValidCoordinate(unittest.TestCase):
	def test_valid_coordinate(self):
		self.assertEqual(
			valid_coordinate([[4,0], [4,2], [4,4], [4,6]], "[4,0]"),
			True)

		self.assertEqual(
			valid_coordinate([[4,0], [4,2], [4,4], [4,6]], "[4,    0]"),
			True)

		self.assertEqual(
			valid_coordinate([[4,0], [4,2], [4,4], [4,6]], "[4   ,0]"),
			True)

		self.assertEqual(
			valid_coordinate([[4,0], [4,2], [4,4], [4,6]], "[3,0]"),
			False)

if __name__ == "main":
	unittest.main()