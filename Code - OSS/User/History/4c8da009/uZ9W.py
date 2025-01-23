import unittest
from codefiles.task2 import matrixAddition, matrixByMatrixMultiplication, matrixScalarMultiplication
from codefiles.task1 import MatrixKeeper

class TestMatrixOperations(unittest.TestCase):

    def setUp(self):
        # Создаем объекты MatrixKeeper и задаем им матрицы для тестирования
        self.matrix_keeper1 = MatrixKeeper()
        self.matrix_keeper2 = MatrixKeeper()

        # Заполняем матрицы в формате CSR
        self.matrix_keeper1.values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.matrix_keeper1.indices = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        self.matrix_keeper1.indptr = [0, 3, 6, 9]
        self.matrix_keeper1.shape = (3, 3)

        self.matrix_keeper2.values = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.matrix_keeper2.indices = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        self.matrix_keeper2.indptr = [0, 3, 6, 9]
        self.matrix_keeper2.shape = (3, 3)

    def test_matrixAddition(self):
        result = matrixAddition(self.matrix_keeper1, self.matrix_keeper2)
        expected_values = [10, 10, 10, 10, 10, 10, 10, 10, 10]
        expected_indices = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        expected_indptr = [0, 3, 6, 9]
        expected_shape = (3, 3)

        self.assertEqual(result[0], expected_values)
        self.assertEqual(result[1], expected_indices)
        self.assertEqual(result[2], expected_indptr)
        self.assertEqual(result[3], expected_shape)

    def test_matrixByMatrixMultiplication(self):
        # Для умножения матриц используем матрицы размером 3x3 и 3x2
        self.matrix_keeper1.values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.matrix_keeper1.indices = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        self.matrix_keeper1.indptr = [0, 3, 6, 9]
        self.matrix_keeper1.shape = (3, 3)

        self.matrix_keeper2.values = [9, 8, 7, 6, 5, 4]
        self.matrix_keeper2.indices = [0, 1, 0, 1, 0, 1]
        self.matrix_keeper2.indptr = [0, 2, 4, 6]
        self.matrix_keeper2.shape = (3, 2)

        result = matrixByMatrixMultiplication(self.matrix_keeper1, self.matrix_keeper2)
        expected_values = [38, 32, 101, 86, 164, 140]
        expected_indices = [0, 1, 0, 1, 0, 1]
        expected_indptr = [0, 2, 4, 6]
        expected_shape = (3, 2)

        self.assertEqual(result[0], expected_values)
        self.assertEqual(result[1], expected_indices)
        self.assertEqual(result[2], expected_indptr)
        self.assertEqual(result[3], expected_shape)

    def test_matrixScalarMultiplication(self):
        scalar = 2
        result = matrixScalarMultiplication(self.matrix_keeper1, scalar)
        expected_values = [2, 4, 6, 8, 10, 12, 14, 16, 18]
        expected_indices = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        expected_indptr = [0, 3, 6, 9]
        expected_shape = (3, 3)

        self.assertEqual(result[0], expected_values)
        self.assertEqual(result[1], expected_indices)
        self.assertEqual(result[2], expected_indptr)
        self.assertEqual(result[3], expected_shape)

if __name__ == '__main__':
    unittest.main()
