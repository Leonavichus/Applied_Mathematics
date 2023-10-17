import numpy as np

# Функция для метода Зейделя


def seidel_method(A, B, x_init, tolerance=1e-10):
    n = len(B)
    x = x_init.copy()

    while True:
        x_new = x.copy()
        for i in range(n):
            sum_val = np.dot(A[i, :], x_new) - A[i, i] * x_new[i]
            x_new[i] = (B[i] - sum_val) / A[i, i]
        if np.max(np.abs(x_new - x)) < tolerance:
            return x_new
        x = x_new


# Коэффициенты матрицы A
A = np.array([[5, -2, -1],
              [-2, 6, 2],
              [-1, 2, 7]], dtype=float)

# Вектор B
B = np.array([-5, 0, 7], dtype=float)

# Начальное приближение
initial_guess = np.zeros(3)

# Применение метода Зейделя
solution = seidel_method(A, B, initial_guess)
print("Решение методом Зейделя:", solution)
