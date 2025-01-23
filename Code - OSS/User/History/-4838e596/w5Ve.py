from codefiles.task1 import MatrixKeeper
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

def gauss(matrix: List[List[float]]) -> float:
    """Вычисляет определитель матрицы методом Гаусса."""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]  # Для матрицы 1x1
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]  # Для матрицы 2x2

    swap_count = 0

    for i in range(n):
        max_row = max(range(i, n), key=lambda r: abs(matrix[r][i]))
        if matrix[max_row][i] == 0:
            raise ValueError("Матрица вырожденная, определитель равен нулю.")

        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            swap_count += 1

        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]

    determinant = 1.0
    for i in range(n):
        determinant *= matrix[i][i]

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
