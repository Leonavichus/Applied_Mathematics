import numpy as np

# Функция для метода скорейшего спуска (метода градиентного спуска)


def steepest_descent(A, B, x, tolerance=1e-10):
    r = B - np.dot(A, x)
    p = r
    while np.max(np.abs(r)) > tolerance:
        Ap = np.dot(A, p)
        alpha = np.dot(r, r) / np.dot(p, Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        p = r

    return x


# Коэффициенты матрицы A
A = np.array([[5, -2, -1],
              [-2, 6, 2],
              [-1, 2, 7]], dtype=float)

# Вектор B
B = np.array([-5, 0, 7], dtype=float)

# Начальное приближение
initial_guess = np.zeros(3)

# Применение метода скорейшего спуска без ограничения по числу итераций
solution = steepest_descent(A, B, initial_guess)
print("Решение методом скорейшего спуска (методом градиентного спуска):", solution)
