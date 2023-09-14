import 'dart:math';

// Функция, которую мы интегрируем
double f(double x) {
  return x * x * sqrt(16 - x * x);
}

// Метод прямоугольников: левые прямоугольники
double leftRectangleMethod(double a, double b, int n) {
  // Вычисляем ширину каждого прямоугольника
  double h = (b - a) / n;
  double integral = 0;

  for (int i = 0; i < n; i++) {
    double x = a + i * h;
    integral += f(x) * h;
  }
  return integral;
}

// Метод прямоугольников: правые прямоугольники
double rightRectangleMethod(double a, double b, int n) {
  // Вычисляем ширину каждого прямоугольника
  double h = (b - a) / n;
  double integral = 0;

  for (int i = 1; i <= n; i++) {
    double x = a + i * h;
    integral += f(x) * h;
  }
  return integral;
}

// Метод прямоугольников: центральные прямоугольники
double centralRectangleMethod(double a, double b, int n) {
  // Вычисляем ширину каждого прямоугольника
  double h = (b - a) / n;
  double integral = 0;

  for (int i = 0; i < n; i++) {
    double x = a + (i + 0.5) * h;
    integral += f(x) * h;
  }
  return integral;
}

void main() {
  // Границы интегрирования
  double a = 2;
  double b = 4;

  // Количество прямоугольников (чем больше, тем точнее результат)
  int n = 1000;

  // Вычисляем интегралы с помощью трех разных методов
  double leftIntegral = leftRectangleMethod(a, b, n);
  double rightIntegral = rightRectangleMethod(a, b, n);
  double centralIntegral = centralRectangleMethod(a, b, n);

  // Выводим результаты на экран
  print('Значение интеграла (левые прямоугольники): $leftIntegral');
  print('Значение интеграла (правые прямоугольники): $rightIntegral');
  print('Значение интеграла (центральные прямоугольники): $centralIntegral');

  // Вычисление погрешности
  double h = (b - a) / n;
  double xi = a + Random().nextDouble() * (b - a); // Случайная точка на отрезке
  double secondDerivative = 16.0 * xi * xi / (pow(16 - xi * xi, 1.5)) - 2.0; // Вторая производная функции
  double error = (((b - a) * h * h * secondDerivative) / 24.0).abs();

  print('Погрешност: ${error.toStringAsFixed(6)}');
}
