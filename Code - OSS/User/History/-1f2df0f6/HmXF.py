import unittest
from codefiles.task3 import MatrixKeeper, determinantOfMatrix, isMatrixInvertable, gauss

class TestMatrixOperations(unittest.TestCase):

    def setUp(self):
        self.matrix_keeper = MatrixKeeper()

    def test_determinantOfMatrix(self):

        self.matrix_keeper.matrix = [
            [1, 2, 3],
            [0, 5, 6],
            [7, 8, 9]
        ]
        result = determinantOfMatrix(self.matrix_keeper)
        expected = -24
        self.assertAlmostEqual(result, expected)

        self.matrix_keeper.matrix = [
            [4, 7],
            [2, 6]
        ]
        result = determinantOfMatrix(self.matrix_keeper)
        expected = 10
        self.assertAlmostEqual(result, expected)

        self.matrix_keeper.matrix = [[1 if i == j else 0 for j in range(100)] for i in range(100)]
        result = determinantOfMatrix(self.matrix_keeper)
        expected = 1
        self.assertAlmostEqual(result, expected)

    def test_isMatrixInvertable(self):
        self.matrix_keeper.matrix = [
            [1, 2, 3],
            [0, 5, 6],
            [7, 8, 9]
        ]
        result = isMatrixInvertable(self.matrix_keeper)
        self.assertTrue(result)

        self.matrix_keeper.matrix = [
            [1, 2, 3],
            [4, 6, 8],
            [7, 10, 12]
        ]
        result = isMatrixInvertable(self.matrix_keeper)
        self.assertTrue(result)

    def test_gauss(self):
        matrix = [
            [1, 2, 3],
            [0, 5, 6],
            [7, 8, 9]
        ]
        result = gauss(matrix)
        expected = -24
        self.assertAlmostEqual(result, expected)

        matrix = [
            [4, 7],
            [2, 6]
        ]
        result = gauss(matrix)
        expected = 10
        self.assertAlmostEqual(result, expected)

        matrix = [
            [5]
        ]
        result = gauss(matrix)
        expected = 5
        self.assertAlmostEqual(result, expected)

        matrix = [[1 if i == j else 0 for j in range(100)] for i in range(100)]
        result = gauss(matrix)
        expected = 1
        self.assertAlmostEqual(result, expected)

        matrix = [
            [1, 2],
            [2, 4]
        ]
        result = gauss(matrix)
        expected = 0
        self.assertAlmostEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
