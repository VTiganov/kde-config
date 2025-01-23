
from codefiles.task1 import MatrixKeeper

from typing import List, Optional, Tuple

def matrixAddition(matrix_keeper1: MatrixKeeper, matrix_keeper2: MatrixKeeper) -> Optional[Tuple[List[float], List[int], List[int], Tuple[int, int]]]:
    """Сложение двух матриц в CSR формате"""

    if matrix_keeper1.values is None or matrix_keeper2.values is None:
        raise ValueError("Одна или обе матрицы не были введены.")

    if matrix_keeper1.shape != matrix_keeper2.shape:
        raise ValueError("Матрицы должны быть одного размера для сложения.")

    result_values = []
    result_indices = []
    result_indptr = [0]
    n, m = matrix_keeper1.shape

    for i in range(n):
        row_values = []
        row_indices = []
        row_dict = {}

        # Проходим по элементам первой матрицы
        for idx in range(matrix_keeper1.indptr[i], matrix_keeper1.indptr[i+1]):
            col = matrix_keeper1.indices[idx]
            value = matrix_keeper1.values[idx]
            row_dict[col] = row_dict.get(col, 0) + value

        # Проходим по элементам второй матрицы
        for idx in range(matrix_keeper2.indptr[i], matrix_keeper2.indptr[i+1]):
            col = matrix_keeper2.indices[idx]
            value = matrix_keeper2.values[idx]
            row_dict[col] = row_dict.get(col, 0) + value

        # Добавляем ненулевые элементы в результат
        for col, value in row_dict.items():
            if value != 0:
                row_values.append(value)
                row_indices.append(col)

        result_values.extend(row_values)
        result_indices.extend(row_indices)
        result_indptr.append(len(result_values))

    return result_values, result_indices, result_indptr, matrix_keeper1.shape


def matrixByMatrixMultiplication(matrix_keeper1: MatrixKeeper, matrix_keeper2: MatrixKeeper) -> Optional[Tuple[List[float], List[int], List[int], Tuple[int, int]]]:
    """Умножение матрицы на матрицу в CSR формате"""

    if matrix_keeper1.values is None or matrix_keeper2.values is None:
        raise ValueError("Одна или обе матрицы не были введены.")

    if matrix_keeper1.shape[1] != matrix_keeper2.shape[0]:
        raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы.")

    result_values = []
    result_indices = []
    result_indptr = [0]
    n, m = matrix_keeper1.shape[0], matrix_keeper2.shape[1]

    for i in range(n):
        row_values = []
        row_indices = []
        row_dict = {}

        # Проходим по элементам первой матрицы
        for idx in range(matrix_keeper1.indptr[i], matrix_keeper1.indptr[i+1]):
            col = matrix_keeper1.indices[idx]
            value = matrix_keeper1.values[idx]

            # Проходим по элементам второй матрицы
            for j in range(matrix_keeper2.indptr[col], matrix_keeper2.indptr[col+1]):
                col2 = matrix_keeper2.indices[j]
                value2 = matrix_keeper2.values[j]
                row_dict[col2] = row_dict.get(col2, 0) + value * value2

        # Добавляем ненулевые элементы в результат
        for col, value in row_dict.items():
            if value != 0:
                row_values.append(value)
                row_indices.append(col)

        result_values.extend(row_values)
        result_indices.extend(row_indices)
        result_indptr.append(len(result_values))

    return result_values, result_indices, result_indptr, (n, m)

    return result

def matrixScalarMultiplication(matrix_keeper: MatrixKeeper, scalar: float) -> Optional[Tuple[List[float], List[int], List[int], Tuple[int, int]]]:
    """Умножение матрицы на скаляр в CSR формате"""

    if matrix_keeper.values is None:
        raise ValueError("Матрица не была введена.")

    result_values = [value * scalar for value in matrix_keeper.values]
    result_indices = matrix_keeper.indices
    result_indptr = matrix_keeper.indptr
    result_shape = matrix_keeper.shape

    return result_values, result_indices, result_indptr, result_shape


def main():
    matrix_keeper1 = MatrixKeeper()
    matrix_keeper2 = MatrixKeeper()

    while True:
        print("\nВыберите из предложенных опций:")
        print("1: Ввести первую матрицу вручную.")
        print("2: Ввести вторую матрицу вручную.")
        print("3: Сложить две матрицы.")
        print("4: Умножить матрицу на матрицу.")
        print("5: Умножить матрицу на скаляр.")
        print("6: Выйти из программы.\n")

        try:
            option = int(input("Введите номер соответствующей опции: "))
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.\n")
            continue

        if option == 1:
            matrix_keeper1.inputMatrix()
        elif option == 2:
            matrix_keeper2.inputMatrix()
        elif option == 3:
            try:
                result = matrixAddition(matrix_keeper1, matrix_keeper2)
                print("Результат сложения матриц:")
                print("values:", result[0])
                print("indices:", result[1])
                print("indptr:", result[2])
                print("shape:", result[3])
            except ValueError as e:
                print(e)
        elif option == 4:
            try:
                result = matrixByMatrixMultiplication(matrix_keeper1, matrix_keeper2)
                print("Результат умножения матриц:")
                print("values:", result[0])
                print("indices:", result[1])
                print("indptr:", result[2])
                print("shape:", result[3])
            except ValueError as e:
                print(e)
        elif option == 5:
            try:
                matrix_choice = int(input("Выберите матрицу для умножения на скаляр (1 - первая матрица, 2 - вторая матрица): "))
                if matrix_choice == 1:
                    matrix_keeper = matrix_keeper1
                elif matrix_choice == 2:
                    matrix_keeper = matrix_keeper2
                else:
                    raise ValueError("Некорректный выбор матрицы.")

                scalar = float(input("Введите скаляр: "))
                result = matrixScalarMultiplication(matrix_keeper, scalar)
                print("Результат умножения матрицы на скаляр:")
                print("values:", result[0])
                print("indices:", result[1])
                print("indptr:", result[2])
                print("shape:", result[3])
            except ValueError as e:
                print(e)
        elif option == 6:
            print("Выход из программы.\n")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите опцию от 1 до 6.\n")

if __name__ == "__main__":
    main()
