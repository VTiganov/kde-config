from codefiles.task1 import MatrixKeeper
from typing import List, Tuple

def determinantOfMatrix(matrix_keeper: MatrixKeeper) -> float:
    """Вычисляет определитель матрицы в CSR формате."""
    if matrix_keeper.values is None:
        raise ValueError("Матрица не задана.")

    if matrix_keeper.shape[0] != matrix_keeper.shape[1]:
        raise ValueError("Определитель можно вычислить только для квадратной матрицы.")

    n = matrix_keeper.shape[0]
    values = matrix_keeper.values
    indices = matrix_keeper.indices
    indptr = matrix_keeper.indptr

    # Применяем метод Гаусса напрямую для CSR формата
    swap_count = 0
    for i in range(n):
        # Находим строку с максимальным элементом в столбце i
        pivot_row = -1
        pivot_value = 0
        for j in range(indptr[i], indptr[i+1]):
            if indices[j] == i:
                pivot_value = values[j]
                pivot_row = i
                break
        if pivot_row == -1:
            # Ищем строку ниже текущей, где есть элемент в столбце i
            for j in range(i + 1, n):
                for k in range(indptr[j], indptr[j+1]):
                    if indices[k] == i:
                        pivot_row = j
                        pivot_value = values[k]
                        break
                if pivot_row != -1:
                    break

        if pivot_value == 0:
            raise ValueError("Матрица вырожденная, определитель равен нулю.")

        if pivot_row != i:
            # Поменять строки местами
            for j in range(indptr[pivot_row], indptr[pivot_row+1]):
                indices[j] = indices[j] + (i - pivot_row) * (indices[j] != i)
            swap_count += 1

        # Приводим строки ниже текущей
        for j in range(i + 1, n):
            for k in range(indptr[j], indptr[j+1]):
                if indices[k] == i:
                    factor = values[k] / pivot_value
                    for l in range(indptr[j], indptr[j+1]):
                        if indices[l] > i:
                            indices[l] -= factor * values[l]
                        else:
                            values[l] -= factor * values[l]
    
    determinant = 1.0
    for i in range(n):
        determinant *= values[i]

    return (-1) ** swap_count * determinant

def isMatrixInvertable(matrix_keeper: MatrixKeeper) -> bool:
    """Проверяет, существует ли обратная матрица (detA != 0)."""
    try:
        det = determinantOfMatrix(matrix_keeper)
        return det != 0
    except ValueError:
        return False

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
