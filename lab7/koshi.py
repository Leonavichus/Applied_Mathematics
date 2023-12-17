import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Заданная дифференциальная функция


def f(x, y):
    return ((8 + 12 * np.cos(x)) * np.exp(2*x)) / y - 3 * y * np.cos(x)

# Шаг метода Рунге-Кутта для решения дифференциального уравнения


def runge_kutta_step(f, x, y, h):
    k1 = h * f(x, y)
    k2 = h * f(x + h/2, y + k1/2)
    k3 = h * f(x + h/2, y + k2/2)
    k4 = h * f(x + h, y + k3)
    return (k1 + 2*k2 + 2*k3 + k4) / 6

# Адаптивный выбор шага для метода Рунге-Кутта


def find_step_size(f, x, y, h, tolerance):
    k1 = runge_kutta_step(f, x, y, h)
    k2 = runge_kutta_step(f, x + h/2, y + k1/2, h/2)
    y1 = y + k1
    y2 = y + k2
    error = abs(y2 - y1)
    return h * 0.9 * (tolerance / error)**0.2

# Решение дифференциального уравнения методом Рунге-Кутта


def runge_kutta_solver(f, a, b, y0, h):
    x_values = [a]
    y_values = [y0]
    while x_values[-1] < b:
        x = x_values[-1]
        y = y_values[-1]
        y += runge_kutta_step(f, x, y, h)
        x_values.append(x + h)
        y_values.append(y)
    return x_values, y_values

# Решение дифференциального уравнения методом Эйлера


def euler_solver(f, a, b, y0, h):
    x_values = [a]
    y_values = [y0]
    while x_values[-1] < b:
        x = x_values[-1]
        y = y_values[-1]
        y += h * f(x, y)
        x_values.append(x + h)
        y_values.append(y)
    return x_values, y_values


# Задание начальных условий и параметров
a, b = 0, 2
y0 = 2
tolerance = 1e-4

# Определение шага для метода Рунге-Кутта и его применение
h_rk = find_step_size(f, a, y0, 0.1, tolerance)
x_values_rk, y_values_rk = runge_kutta_solver(f, a, b, y0, h_rk)

# Фиксированный шаг для метода Эйлера и его применение
h_euler = 0.05
x_values_euler, y_values_euler = euler_solver(f, a, b, y0, h_euler)

# Вычисление точного решения
solution_exact = solve_ivp(
    f, [a, b], [y0], method='RK45', rtol=tolerance, vectorized=True)
y_values_exact_interp = np.interp(
    x_values_rk, solution_exact.t, solution_exact.y[0])

# Сравнение с приближенным решением
max_deviation = np.max(np.abs(y_values_exact_interp - y_values_rk))
print(f"Максимальное отклонение: {max_deviation}")

# Построение графиков
plt.plot(x_values_rk, y_values_rk, label='Рунге-Кутт IV')
plt.plot(x_values_euler, y_values_euler, label='Эйлер')
plt.plot(solution_exact.t,
         solution_exact.y[0], label='Точное решение', linestyle='dashed')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
