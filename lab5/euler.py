import numpy as np
import matplotlib.pyplot as plt

# Определение функции, представляющей правую часть дифференциального уравнения


def f(t, y):
    return -y / 3 + 2 + np.sin(t)

# Метод Эйлера


def euler(f, t_0, y_0, h, n):
    t_values, y_values = [t_0], [y_0]
    t, y = t_0, y_0
    for _ in range(n):
        y += h * f(t, y)
        t += h
        t_values.append(t)
        y_values.append(y)
    return t_values, y_values

# Метод Рунге – Кутта второго порядка


# Заданные параметры
y_0 = 2  # начальное значение y
h = 0.1  # шаг
n = 100  # количество шагов
t_0 = 0  # начальное значение t

# Вычисление значений с помощью всех трех методов
t_euler, y_euler = euler(f, t_0, y_0, h, n)

# Вычисление точного решения
t_exact = np.linspace(t_0, t_0 + n * h, 1000)
y_exact = 6 - np.cos(t_exact) - 3 * np.exp(-t_exact/3)

# Построение графиков
plt.figure(figsize=(12, 6))
plt.plot(t_euler, y_euler, label='Приближенное решение')
plt.plot(t_exact, y_exact, label='Точное решение', linestyle='dashed')
plt.title('Метод Эйлера')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()

# Интерполяция точного решения на значения t, используемые в методе Эйлера
y_exact_interpolated = np.interp(t_euler, t_exact, y_exact)
# Вычисление погрешности
error = np.abs(y_exact_interpolated - y_euler)
# Максимальная погрешность
max_error = np.max(error)
print(f"Погрешность: {max_error}")
