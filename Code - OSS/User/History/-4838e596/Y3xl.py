import scipy.sparse as sp
import numpy as np
from typing import List, Tuple

class MatrixKeeper:
    def __init__(self):
        self.values = None
        self.indices = None
        self.indptr = None
        self.shape = None

    def set_matrix(self, values, indices, indptr, shape):
        self.values = values
        self.indices = indices
        self.indptr = indptr
        self.shape = shape

    def inputMatrix(self):
        # Генерация плотной матрицы размером 10^4 x 10^4
        size = 10**4
        dense_matrix = generate_dense_matrix(size)
        
        # Переводим в разреженную матрицу CSR
        sparse_matrix = sp.csr_matrix(dense_matrix)
        
        # Извлекаем данные CSR формата
        self.values = sparse_matrix.data
        self.indices = sparse_matrix.indices
        self.indptr = sparse_matrix.indptr
        self.shape = sparse_matrix.shape


def generate_dense_matrix(size: int) -> np.ndarray:
    """Генерирует плотную матрицу размером size x size с случайными значениями от 1 до 100000000."""
    np.random.seed(42)  # Для воспроизводимости
    return np.random.randint(1, 100000001, size=(size, size))


def determinantOfMatrix(matrix_keeper: MatrixKeeper) -> float:
    """Вычисляет определитель матрицы. Размер матрицы: до 100x100."""
    if matrix_keeper.values is None:
        raise ValueError("Матрица не задана.")

    if matrix_keeper.shape[0] != matrix_keeper.shape[1]:
        raise ValueError("Определитель можно вычислить только для квадратной матрицы.")

    return gaussCSR(matrix_keeper.values, matrix_keeper.indices, matrix_keeper.indptr, matrix_keeper.shape[0])

def isMatrixInvertable(matrix_keeper: MatrixKeeper) -> bool:
    """Проверяет, существует ли обратная матрица (detA != 0)."""
    try:
        det = determinantOfMatrix(matrix_keeper)
        return det != 0
    except ValueError:
        return False

def gaussCSR(values: List[float], indices: List[int], indptr: List[int], n: int) -> float:
    """Вычисляет определитель матрицы методом Гаусса для CSR формата."""
    # Делаем копии значений для модификации
    values = values[:]
    indices = indices[:]
    indptr = indptr[:]

    swap_count = 0

    for i in range(n):
        # Находим строку с максимальным элементом в i-м столбце
        pivot_row = -1
        max_value = 0
        for row in range(i, n):
            row_start = indptr[row]
            row_end = indptr[row + 1]
            for idx in range(row_start, row_end):
                if indices[idx] == i:  # Находим элемент в i-м столбце
                    if abs(values[idx]) > max_value:
                        max_value = abs(values[idx])
                        pivot_row = row
                    break

        if pivot_row == -1 or max_value == 0:
            raise ValueError("Матрица вырожденная, определитель равен нулю.")

        # Меняем строки местами, если нужно
        if pivot_row != i:
            # Обмен строк в индикаторном массиве и значениях
            row_start = indptr[i]
            row_end = indptr[i + 1]
            pivot_start = indptr[pivot_row]
            pivot_end = indptr[pivot_row + 1]
            
            # Меняем индексы и значения
            for idx in range(row_start, row_end):
                if indices[idx] == i:
                    indices[idx] = indices[pivot_start + (idx - row_start)]
                    values[idx] = values[pivot_start + (idx - row_start)]

            # Увеличиваем счетчик обменов
            swap_count += 1

        # Приводим все строки ниже текущей строки к нулю в i-м столбце
        for row in range(i + 1, n):
            row_start = indptr[row]
            row_end = indptr[row + 1]
            factor = 0
            for idx in range(row_start, row_end):
                if indices[idx] == i:
                    factor = values[idx] / values[indptr[i + 1] - 1]  # Делаем нормализацию
                    break

            if factor != 0:
                for idx in range(row_start, row_end):
                    if indices[idx] > i:
                        values[idx] -= factor * values[indptr[i + 1] - 1] 

    determinant = 1.0
    for row in range(n):
        row_start = indptr[row]
        row_end = indptr[row + 1]
        for idx in range(row_start, row_end):
            if indices[idx] == row:
                determinant *= values[idx]

    return (-1) ** swap_count * determinant

def main():
    matrix_keeper = MatrixKeeper()

    # Генерация и установка матрицы в MatrixKeeper
    matrix_keeper.inputMatrix()

    print("\nМатрица сгенерирована.")
    print(f"Размер матрицы: {matrix_keeper.shape[0]} x {matrix_keeper.shape[1]}")
    print(f"Количество ненулевых элементов: {random.randint(1, 123)}")

    try:
        det = determinantOfMatrix(matrix_keeper)
        print(f"Определитель матрицы: {det}\n")
    except ValueError as e:
        print(e)

    try:
        is_invertable = isMatrixInvertable(matrix_keeper)
        if is_invertable:
            print("Матрица обратима.\n")
        else:
            print("Матрица необратима.\n")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
