from task1 import MatrixKeeper
from typing import List, Tuple

def csrToDense(values: List[float], indices: List[int], indptr: List[int], shape: Tuple[int, int]) -> List[List[float]]:
    """Преобразует CSR формат в плотный формат."""
    n, m = shape
    dense_matrix = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for idx in range(indptr[i], indptr[i+1]):
            dense_matrix[i][indices[idx]] = values[idx]
    return dense_matrix

def determinantOfMatrix(matrix_keeper: MatrixKeeper) -> float:
    """Вычисляет определитель матрицы. Размер матрицы: до 100x100."""
    if matrix_keeper.values is None:
        raise ValueError("Матрица не задана.")

    if matrix_keeper.shape[0] != matrix_keeper.shape[1]:
        raise ValueError("Определитель можно вычислить только для квадратной матрицы.")

    dense_matrix = csrToDense(matrix_keeper.values, matrix_keeper.indices, matrix_keeper.indptr, matrix_keeper.shape)
    return gauss(dense_matrix)

def isMatrixInvertable(matrix_keeper: MatrixKeeper) -> bool:
    """Проверяет, существует ли обратная матрица (detA != 0)."""
    try:
        det = determinantOfMatrix(matrix_keeper)
        return det != 0
    except ValueError:
        return False


from typing import List

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

    while True:
        print("\nВыберите из предложенных опций:")
        print("1: Ввести матрицу вручную.")
        print("2: Вычислить определитель матрицы.")
        print("3: Проверить, существует ли обратная матрица.")
        print("4: Выйти из программы.\n")

        try:
            option = int(input("Введите номер соответствующей опции: "))
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.\n")
            continue

        if option == 1:
            matrix_keeper.inputMatrix()
        elif option == 2:
            try:
                det = determinantOfMatrix(matrix_keeper)
                print(f"Определитель матрицы: {det}\n")
            except ValueError as e:
                print(e)
        elif option == 3:
            try:
                is_invertable = isMatrixInvertable(matrix_keeper)
                if is_invertable:
                    print("Матрица обратима.\n")
                else:
                    print("Матрица необратима.\n")
            except ValueError as e:
                print(e)
        elif option == 4:
            print("Выход из программы.\n")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите опцию от 1 до 4.\n")

if __name__ == "__main__":
    main()
