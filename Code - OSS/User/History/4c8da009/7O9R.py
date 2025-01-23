import unittest
from codefiles.task2 import matrixAddition, matrixByMatrixMultiplication, matrixScalarMultiplication
from codefiles.task1 import MatrixKeeper

class TestMatrixOperations(unittest.TestCase):

    def setUp(self):
        # Создаем объекты MatrixKeeper и задаем им матрицы для тестирования
        self.matrix_keeper1 = MatrixKeeper()
        self.matrix_keeper2 = MatrixKeeper()

        self.matrix_keeper1.matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        self.matrix_keeper2.matrix = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]

    def test_matrixAddition(self):
        result = matrixAddition(self.matrix_keeper1, self.matrix_keeper2)
        expected = [
            [10, 10, 10],
            [10, 10, 10],
            [10, 10, 10]
        ]
        self.assertEqual(result, expected)

    def test_matrixByMatrixMultiplication(self):
        # Для умножения матриц используем матрицы размером 3x3 и 3x2
        self.matrix_keeper1.matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        self.matrix_keeper2.matrix = [
            [9, 8],
            [7, 6],
            [5, 4]
        ]

        result = matrixByMatrixMultiplication(self.matrix_keeper1, self.matrix_keeper2)
        expected = [
            [38, 32],
            [101, 86],
            [164, 140]
        ]
        self.assertEqual(result, expected)

    def test_matrixScalarMultiplication(self):
        scalar = 2
        result = matrixScalarMultiplication(self.matrix_keeper1, scalar)
        expected = [
            [2, 4, 6],
            [8, 10, 12],
            [14, 16, 18]
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
