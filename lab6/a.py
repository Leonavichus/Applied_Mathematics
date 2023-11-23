import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

# Заданные данные
x = np.array([1, 2, 5, 6, 7, 9, 11, 12, 16])
y = np.array([2, 6, 3, 2, 4, 5, 5, 9, 3])

def divided_diff(x, y):
    """Calculate divided differences."""
    n = len(y)
    coef = np.zeros([n, n])

    # Initialize the first column of the divided differences table
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x[i + j] - x[i])

    return coef[0, :]

def newton(x, y, x_interpolate):
    """Perform Newton interpolation."""
    coef = divided_diff(x, y)
    result = coef[0]

    for i in range(1, len(coef)):
        term = coef[i]
        for j in range(i):
            term *= (x_interpolate - x[j])
        result += term

    return result

# Интерполяционный полином Лагранжа
lagrange_poly = lagrange(x, y)

# Интерполяционный полином Ньютона
newton_coef = divided_diff(x, y)  # Rename the variable
y_newton = [newton(x, y, xi) for xi in x]

# Создание новых x для более плавного графика
x_new = np.linspace(min(x), max(x), 100)

# Оценка значений функции
y_lagrange = lagrange_poly(x_new)
y_newton_interpolated = [newton(x, y, xi) for xi in x_new]

# Визуализация результатов
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Исходные данные', color='red')
# plt.plot(x_new, y_lagrange, label='Интерполяционный полином Лагранжа', linestyle='--', color='blue')
plt.plot(x_new, y_newton_interpolated, label='Интерполяционный полином Ньютона', linestyle=':', color='green')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяция: Лагранж и Ньютон')
plt.grid(True)
plt.show()
