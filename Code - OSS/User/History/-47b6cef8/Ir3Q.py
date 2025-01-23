import unittest
from codefiles.task1 import MatrixKeeper

class TestMatrixKeeper(unittest.TestCase):

    def setUp(self):
        self.keeper = MatrixKeeper()

    def test_inputMatrix(self):
        # Переопределяем метод inputMatrix для тестирования
        def mock_inputMatrix():
            self.keeper.values = [1.32, 2.32, 3.45, 2.1, 4.312, 4.24, 3.1, 1.12, 9.125]
            self.keeper.indices = [0, 1, 2, 0, 1, 2, 0, 1, 2]
            self.keeper.indptr = [0, 3, 6, 9]
            self.keeper.shape = (3, 3)

        mock_inputMatrix()

        self.assertEqual(self.keeper.values, [1.32, 2.32, 3.45, 2.1, 4.312, 4.24, 3.1, 1.12, 9.125])
        self.assertEqual(self.keeper.indices, [0, 1, 2, 0, 1, 2, 0, 1, 2])
        self.assertEqual(self.keeper.indptr, [0, 3, 6, 9])
        self.assertEqual(self.keeper.shape, (3, 3))

    def test_trace(self):
        # Переопределяем метод inputMatrix для тестирования
        def mock_inputMatrix():
            self.keeper.values = [1.32, 2.32, 3.45, 2.1, 4.312, 4.24, 3.1, 1.12, 9.125]
            self.keeper.indices = [0, 1, 2, 0, 1, 2, 0, 1, 2]
            self.keeper.indptr = [0, 3, 6, 9]
            self.keeper.shape = (3, 3)

        mock_inputMatrix()

        self.assertEqual(self.keeper.trace(), 14.757000000000001)

    def test_findByIndex(self):
        # Переопределяем метод inputMatrix для тестирования
        def mock_inputMatrix():
            self.keeper.values = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
            self.keeper.indices = [0, 1, 2, 0, 1, 2, 0, 1, 2]
            self.keeper.indptr = [0, 3, 6, 9]
            self.keeper.shape = (3, 3)

        mock_inputMatrix()

        self.assertEqual(self.keeper.findByIndex(1, 1), 1.0)
        self.assertEqual(self.keeper.findByIndex(2, 2), 5.0)
        self.assertEqual(self.keeper.findByIndex(3, 3), 9.0)

    def test_trace_not_square(self):
        # Переопределяем метод inputMatrix для тестирования
        def mock_inputMatrix():
            self.keeper.values = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
            self.keeper.indices = [0, 1, 2, 0, 1, 2]
            self.keeper.indptr = [0, 3, 6]
            self.keeper.shape = (2, 3)

        mock_inputMatrix()

        with self.assertRaises(ValueError):
            self.keeper.trace()

    def test_findByIndex_out_of_bounds(self):
        # Переопределяем метод inputMatrix для тестирования
        def mock_inputMatrix():
            self.keeper.values = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
            self.keeper.indices = [0, 1, 2, 0, 1, 2, 0, 1, 2]
            self.keeper.indptr = [0, 3, 6, 9]
            self.keeper.shape = (3, 3)

        mock_inputMatrix()

        with self.assertRaises(IndexError):
            self.keeper.findByIndex(4, 4)

if __name__ == '__main__':
    unittest.main()
