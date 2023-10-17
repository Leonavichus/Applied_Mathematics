import numpy as np

# Итерационный метод наименьших невязок


def conjugate_gradient(A, B, x, tolerance=1e-10):
    r = B - np.dot(A, x)
    p = r
    while np.max(np.abs(r)) > tolerance:
        Ap = np.dot(A, p)
        alpha = np.dot(r, r) / np.dot(p, Ap)
        x = x + alpha * p
        r_new = r - alpha * Ap
        beta = np.dot(r_new, r_new) / np.dot(r, r)
        p = r_new + beta * p
        r = r_new

    return x


# Коэффициенты матрицы A
A = np.array([[5, -2, -1],
              [-2, 6, 2],
              [-1, 2, 7]], dtype=float)

# Вектор B
B = np.array([-5, 0, 7], dtype=float)

# Начальное приближение
initial_guess = np.zeros(3)

# Применение метода наименьших невязок
solution = conjugate_gradient(A, B, initial_guess)
print("Решение методом наименьших невязок:", solution)
