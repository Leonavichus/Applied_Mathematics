import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Заданные данные
y = np.array([3, 4, 4, 7, -4, 3, -3, 3])
x = np.arange(len(y))  # Используем индексы в качестве значений x

# Создаем интерполяционную функцию
interp_func = interp1d(x, y, kind='cubic', fill_value='cubic')

# Генерируем новые значения x для более гладкой кривой
x_interp = np.linspace(0, len(y) - 1, 100)

# Вычисляем значения y для новых x
y_interp = interp_func(x_interp)

# Выводим результаты
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Исходные данные', color='red')
plt.plot(x_interp, y_interp, label='Интерполяционный тригонометрический полином', color='blue')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяция тригонометрическим полиномом')
plt.grid(True)
plt.show()
