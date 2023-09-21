import 'dart:math';

double f(double x) {
  return atan(x) + 2 * x - 3;
}

double solveEquation(double a, double b, double epsilon) {
  if (f(a) * f(b) >= 0) {
    print(
        "Условие теоремы Больцано-Коши не выполнено. Выберите другой интервал.");
    return -1.0;
  }

  double x = 0;

  while ((b - a).abs() > epsilon) {
    x = (f(b) * a - f(a) * b) / (f(b) - f(a));

    if (f(a) * f(x) >= 0) {
      // Корень находится в левой половине интервала
      a = x;
    } else if (f(b) * f(x) >= 0) {
      // Корень находится в правой половине интервала
      b = x;
    } else {
      // Мы нашли корень с заданной точностью
      return x;
    }
  }

  return x;
}

void main() {
  final double a = 0; // Начальное приближение для корня
  final double b = 10; // Другое начальное приближение для корня
  final double epsilon = 0.00001; // Точность решения

  double result = solveEquation(a, b, epsilon);

  if (result != -1.0) {
    print("Приближенное значение корня: $result");
  } else {
    print("Не удалось найти корень на заданном интервале.");
  }
}
