import unittest

from codefiles.task1 import MatrixKeeper

class testMatrixKeeper(unittest.TestCase):

    def setUp(self):
        self.keeper = MatrixKeeper()

    def test_inputMatrix(self):

        self.keeper.matrix = [
            [1.32, 2.32, 3.45],
            [2.1, 4.312, 4.24],
            [3.1, 1.12, 9.125]
        ]

        self.assertEqual(self.keeper.matrix, [
            [1.32, 2.32, 3.45],
            [2.1, 4.312, 4.24],
            [3.1, 1.12, 9.125]
        ])

    
    def test_trace(self):

        self.keeper.matrix = [
            [1.32, 2.32, 3.45],
            [2.1, 4.312, 4.24],
            [3.1, 1.12, 9.125]
        ]

        self.assertEqual(self.keeper.trace(), 14.757)

    def test_findByIndex(self):

        self.keeper.matrix = [
             [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0]
        ]
        self.assertEqual(self.keeper.findByIndex(1, 1), 1.0)
        self.assertEqual(self.keeper.findByIndex(2, 2), 5.0)
        self.assertEqual(self.keeper.findByIndex(3, 3), 9.0)

    def test_trace_not_square(self):
        
        self.keeper.matrix = [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0]
        ]
        with self.assertRaises(ValueError):
            self.keeper.trace()
    
    def test_findByIndex_out_of_bounds(self):
        
        self.keeper.matrix = [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0]
        ]
        with self.assertRaises(IndexError):
            self.keeper.findByIndex(4, 4)