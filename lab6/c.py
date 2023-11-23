import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Заданные данные
x = np.array([1, 2, 5, 6, 7, 9, 11, 12, 16])
y = np.array([2, 6, 3, 2, 4, 5, 5, 9, 3])

# Линейная регрессия (y = ax + b)
def linear(x, a, b):
    return a * x + b

# Квадратичная регрессия (y = ax^2 + bx + c)
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

# Кубическая регрессия (y = ax^3 + bx^2 + cx + d)
def cubic(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# Создание новых x для более плавного графика
x_new = np.linspace(min(x), max(x), 100)

# Линейная регрессия
params_linear, _ = curve_fit(linear, x, y)
y_linear = linear(x_new, *params_linear)

# Квадратичная регрессия
params_quadratic, _ = curve_fit(quadratic, x, y)
y_quadratic = quadratic(x_new, *params_quadratic)

# Кубическая регрессия
params_cubic, _ = curve_fit(cubic, x, y)
y_cubic = cubic(x_new, *params_cubic)

# Визуализация результатов
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Исходные данные', color='red')
plt.plot(x_new, y_linear, label='Линейная регрессия', linestyle='-', color='blue')
plt.plot(x_new, y_quadratic, label='Квадратичная регрессия', linestyle=':', color='green')
plt.plot(x_new, y_cubic, label='Кубическая регрессия', linestyle='--', color='purple')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Метод минимальных квадратов')
plt.grid(True)
plt.show()
