# simple programs level 1
import unittest
from gol import *

import unittest

class GOLFunctions(unittest.TestCase):
    def test_underpopulation(self):
        gol = self.setup()
        for x in range(len(gol.data[0])):
            for y in range(len(gol.data[0][0])):
                # To do, setup board and then run function
                gol.underpopulation(0, x, y)

    def setup(self):
        f, x, y = 2, 10, 10
        return GameOfLife(f, x, y)
    
    
    
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)