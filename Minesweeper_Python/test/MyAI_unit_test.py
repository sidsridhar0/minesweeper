import unittest
import os
import sys
sys.path.append(os.path.abspath('../src'))
from MyAI import MyAI
from MyAI import Tile

class TestMyAI(unittest.TestCase):
	def setUp(self):
		self._rowDimension = 4
		self._colDimension = 4
		self._mine_num = 2
		self.ai = MyAI(4, 4, 2, 1, 1)

	def test_init(self):
		self.assertEqual(self.ai._rowDimension, self._rowDimension)
		self.assertEqual(self.ai._colDimension, self._colDimension)
		self.assertEqual(self.ai._mine_num, self._mine_num)
		self.assertEqual(self.ai._last_visited, (1,1))
		self.assertEqual(self.ai._last_action, 1)
		self.assertEqual(self.ai._frontier, dict())
		self.assertEqual(self.ai._mines, set())
		self.assertEqual(self.ai._safe, [])
		self.assertEqual(self.ai._flagged_tiles, set())

		self.assertTrue(isinstance(list(self.ai._unvisited)[0], tuple))
		with self.assertRaises(KeyError):
			self.assertTrue(self.ai._board[(0,0)])	

		self.assertTrue(isinstance(self.ai._board[(1,1)], Tile))
		self.assertTrue(len(self.ai._board) == self._rowDimension * self._colDimension)
		self.assertTrue(len(self.ai._unvisited) == self._rowDimension * self._colDimension)


		



	
if __name__ == '__main__':
    unittest.main()
