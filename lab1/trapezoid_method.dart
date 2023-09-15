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

  for (int i = 0; i < n; i++) {
    double x0 = a + i * h;
    double x1 = a + (i + 1) * h;
    integral += (f(x0) + f(x1)) / 2 * h;
  }

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

  // Вычисление погрешности
  double h = (b - a) / n;
  double xi = a + Random().nextDouble() * (b - a); // Случайная точка на отрезке
  double secondDerivative = 16.0 * xi * xi / pow(16 - xi * xi, 1.5) -
      2.0; // Вторая производная функции
  double error = (((b - a) * h * h * secondDerivative) / 12.0).abs();

  print('Погрешность метода трапеций: ${error.toStringAsFixed(6)}');
}
