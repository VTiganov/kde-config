import unittest
from codefiles.task3 import MatrixKeeper, determinantOfMatrix, isMatrixInvertable, gauss

class TestMatrixOperations(unittest.TestCase):

    def setUp(self):
        self.matrix_keeper = MatrixKeeper()

    def test_determinantOfMatrix(self):
        # Заполняем матрицы в формате CSR
        self.matrix_keeper.values = [1, 2, 3, 5, 6, 7, 8, 9]
        self.matrix_keeper.indices = [0, 1, 2, 1, 2, 0, 1, 2]
        self.matrix_keeper.indptr = [0, 3, 5, 8]
        self.matrix_keeper.shape = (3, 3)

        result = determinantOfMatrix(self.matrix_keeper)
        expected = -24
        self.assertAlmostEqual(result, expected)

        self.matrix_keeper.values = [4, 7, 2, 6]
        self.matrix_keeper.indices = [0, 1, 0, 1]
        self.matrix_keeper.indptr = [0, 2, 4]
        self.matrix_keeper.shape = (2, 2)

        result = determinantOfMatrix(self.matrix_keeper)
        expected = 10
        self.assertAlmostEqual(result, expected)

        self.matrix_keeper.values = [1] * 100
        self.matrix_keeper.indices = list(range(100))
        self.matrix_keeper.indptr = list(range(0, 101))
        self.matrix_keeper.shape = (100, 100)

        result = determinantOfMatrix(self.matrix_keeper)
        expected = 1
        self.assertAlmostEqual(result, expected)

    def test_isMatrixInvertable(self):
        self.matrix_keeper.values = [1, 2, 3, 5, 6, 7, 8, 9]
        self.matrix_keeper.indices = [0, 1, 2, 1, 2, 0, 1, 2]
        self.matrix_keeper.indptr = [0, 3, 5, 8]
        self.matrix_keeper.shape = (3, 3)

        result = isMatrixInvertable(self.matrix_keeper)
        self.assertTrue(result)

        self.matrix_keeper.values = [1, 2, 3, 4, 6, 8, 7, 10, 12]
        self.matrix_keeper.indices = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        self.matrix_keeper.indptr = [0, 3, 6, 9]
        self.matrix_keeper.shape = (3, 3)

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
