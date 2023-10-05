import numpy as np
import scipy.linalg as la

# Функция для решения системы уравнений методом Гаусса


def solve_gauss(A, b):
    n = len(b)
    for i in range(n):
        # Выбираем строку с максимальным по модулю элементом в качестве опорной
        pivot_row = i
        for j in range(i + 1, n):
            if abs(A[j, i]) > abs(A[pivot_row, i]):
                pivot_row = j

        # Переставляем строки матрицы A и элементы вектора b
        A[[i, pivot_row]] = A[[pivot_row, i]]
        b[i], b[pivot_row] = b[pivot_row], b[i]

        # Приводим матрицу A к треугольному виду
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # Обратный ход метода Гаусса для нахождения решения
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x

# Функция для решения системы уравнений методом LU-разложения


def solve_lu(A, b):
    # Получение матриц L, U и перестановок P через LU-разложение
    P, L, U = la.lu(A)

    # Решение системы с учетом перестановок
    y = la.solve_triangular(L, P @ b)  # Решение Ly = Pb
    x = la.solve_triangular(U, y)  # Решение Ux = y

    return x


# Система уравнений и вектор b
A = np.array([[1.0, -2.0, -1.0],
              [3.0, 4.0, 2.0],
              [-2.0, 5.0, 1.0]])

b = np.array([-5.0, 0.0, 7.0])

# Решение системы методом Гаусса и вывод результата
x_gauss = solve_gauss(A, b)
print("Решение методом Гаусса:", x_gauss)

# Решение системы методом LU-разложения и вывод результата
x_lu = solve_lu(A, b)
print("Решение методом LU-разложения:", x_lu)
