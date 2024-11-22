# simple programs level 1
import unittest
from task1 import *

import unittest

class TestTicTacToeFunctions(unittest.TestCase):
    def test_print_board(self):
        print('board display')
        print_board()

    def test_check_win(self):
        board[0][0] = 'X'
        board[0][1] = 'X'
        board[0][2] = 'X'
        self.assertTrue(check_win('X'))

    def test_check_draw(self):
        for i in range(3):
            for j in range(3):
                board[i][j] = 'X'
        self.assertTrue(check_draw())

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)