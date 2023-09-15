import 'dart:math';

// Функция, которую мы интегрируем
double f(double x) {
  return x * x * sqrt(16 - x * x);
}

// Метод Симпсона для вычисления интеграла
double simpsonsRule(double a, double b, int n) {
  // Проверка на четность количества подинтервалов n
  if (n % 2 != 0) {
    throw ArgumentError("Количество подинтервалов n должно быть четным.");
  }

  // Вычисляем ширину каждого подинтервала
  double h = (b - a) / n;
  double integral = 0;

  // Вычисляем сумму по формуле Симпсона
  for (int i = 1; i < n; i++) {
    double x = a + i * h;
    integral += (i % 2 == 0) ? 2 * f(x) : 4 * f(x);
  }

  // Умножаем на h/3 по формуле Симпсона, чтобы получить интеграл
  integral *= h / 3;
  return integral;
}

void main() {
  // Границы интегрирования
  double a = 2;
  double b = 4;

  // Количество подинтервалов (чем больше, тем точнее результат)
  int n = 1000;

  // Вычисляем интеграл с помощью метода Симпсона
  double integral = simpsonsRule(a, b, n);

  // Выводим результат на экран
  print('Значение интеграла (метод Симпсона): $integral');

  // Вычисление погрешности
  double h = (b - a) / n;
  double xi = a + Random().nextDouble() * (b - a); // Случайная точка на отрезке
  double fourthDerivative = -16.0 *
      (3 * xi * xi - 8) *
      (3 * xi * xi - 4) /
      pow(16 - xi * xi, 2.5); // Четвертая производная функции
  double error = (((b - a) * h * h * h * h * fourthDerivative) / 2880.0).abs();

  print('Погрешность метода Симпсона: ${error.toStringAsFixed(6)}');
}
