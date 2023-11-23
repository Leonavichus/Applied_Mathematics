import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Заданные данные
x = np.array([1, 2, 5, 6, 7, 9, 11, 12, 16])
y = np.array([2, 6, 3, 2, 4, 5, 5, 9, 3])

# Интерполяционный кубический сплайн
cubic_spline = CubicSpline(x, y)

# Создание новых x для более плавного графика
x_new = np.linspace(min(x), max(x), 100)

# Оценка значений функции
y_cubic_spline = cubic_spline(x_new)

# Визуализация результатов
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Исходные данные', color='red')
plt.plot(x_new, y_cubic_spline, label='Интерполяционный кубический сплайн', linestyle='-', color='blue')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяция: Кубический сплайн')
plt.grid(True)
plt.show()
