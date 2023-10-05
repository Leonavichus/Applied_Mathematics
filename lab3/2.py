import numpy as np

# Функция для решения системы уравнений методом прогонки (методом Томаса)


def thomas_algorithm(A, b):
    n = len(b)

    # Инициализация массивов для хранения прогоночных коэффициентов
    alpha = np.zeros(n - 1)
    beta = np.zeros(n)

    # Прямой проход
    alpha[0] = -A[0, 1] / A[0, 0]
    beta[0] = b[0] / A[0, 0]

    for i in range(1, n - 1):
        denominator = A[i, i] + A[i, i - 1] * alpha[i - 1]
        alpha[i] = -A[i, i + 1] / denominator
        beta[i] = (b[i] - A[i, i - 1] * beta[i - 1]) / denominator

    # Обратный проход
    x = np.zeros(n)
    x[n - 1] = (b[n - 1] - A[n - 1, n - 2] * beta[n - 2]) / \
        (A[n - 1, n - 1] + A[n - 1, n - 2] * alpha[n - 2])

    for i in range(n - 2, -1, -1):
        x[i] = alpha[i] * x[i + 1] + beta[i]

    return x


# Система уравнений и вектор b
A = np.array([[2.0, -1.0, 0.0, 0.0],
              [2.0, 5.0, -3.0, 0.0],
              [0.0, -1.0, 6.0, -4.0],
              [0.0, 0.0, -3.0, 4.0]])

b = np.array([3.0, -6.0, 3.0, 1.0])

# Решение системы методом прогонки и вывод результата
x = thomas_algorithm(A, b)
print("Решение методом прогонки:", x)
