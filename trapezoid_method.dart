import 'dart:math';

// Функция, которую мы интегрируем
double f(double x) {
  return x * x * sqrt(16 - x * x);
}

// Метод трапеций для вычисления интеграла
double trapezoidalMethod(double a, double b, int n) {
  // Вычисляем ширину каждой трапеции
  double h = (b - a) / n;
  double integral = 0;

  // Добавляем значения функции в углах трапеций и усредняем их
  for (int i = 0; i <= n; i++) {
    double x = a + i * h;
    if (i == 0 || i == n) {
      integral += f(x) / 2; // Половина значения на краях
    } else {
      integral += f(x);
    }
  }

  // Умножаем на ширину трапеций, чтобы получить интеграл
  integral *= h;
  return integral;
}

void main() {
  // Границы интегрирования
  double a = 2;
  double b = 4;

  // Количество трапеций (чем больше, тем точнее результат)
  int n = 1000;

  // Вычисляем интеграл с помощью метода трапеций
  double integral = trapezoidalMethod(a, b, n);

  // Выводим результат на экран
  print('Значение интеграла (метод трапеций): $integral');
}
