"""
Calculator module for TDD demo (RED phase).
Фаза RED — все функции либо содержат ошибки, либо не реализованы.
Цель: чтобы тесты упали и показать процесс RED → GREEN.
"""

# 🔴 Итерация 1: add() — неправильное сложение
def add(a, b):
    """Функция сложения (ошибка намеренно)"""
    return a - b   # ❌ должно быть a + b


# 🔴 Итерация 2: subtract() — не реализована
def subtract(a, b):
    """Функция вычитания (не реализована)"""
    pass


# 🔴 Итерация 3: multiply() — ошибка логики
def multiply(a, b):
    """Функция умножения (ошибка намеренно)"""
    return a + b


# 🔴 Итерация 4: divide() — без обработки нуля
def divide(a, b):
    """Функция деления (ошибка при b = 0)"""
    return a / b


# 🔴 Итерация 5: power() — возвращает строку
def power(a, b):
    """Возведение в степень (ошибка — возвращает строку)"""
    return str(a ** b)


# 🔴 Итерация 6: absolute() — неверное поведение
def absolute(a):
    """Модуль числа (ошибка — не берёт abs)"""
    return a


# 🔴 Итерация 7: percentage() — неверная формула
def percentage(a, b):
    """Процент от числа (ошибка намеренно)"""
    return a * b


# 🔴 Итерация 8: round_value() — не округляет
def round_value(a, digits=2):
    """Округление числа (ошибка намеренно)"""
    return a


# 🔴 Итерация 9: square_root() — не проверяет отрицательные
def square_root(a):
    """Квадратный корень числа (ошибка для отрицательных)"""
    import math
    return math.sqrt(a)  # ❌ при отрицательном — ошибка


# 🔴 Итерация 10: mod() — неверная формула
def mod(a, b):
    """Остаток от деления (ошибка)"""
    return a / b   # ❌ вместо %


# 🔴 Итерация 11: max_value() — возвращает min
def max_value(a, b):
    """Максимум из двух чисел (ошибка)"""
    return min(a, b)


# 🔴 Итерация 12: min_value() — возвращает max
def min_value(a, b):
    """Минимум из двух чисел (ошибка)"""
    return max(a, b)


# 🔴 Итерация 13: safe_divide() — падает при делении на ноль
def safe_divide(a, b):
    """Безопасное деление (ошибка — без проверки на 0)"""
    return a / b


# 🔴 Итерация 14: average() — неверная логика
def average(numbers):
    """Среднее значение (ошибка — не делит на длину)"""
    return sum(numbers)


# 🔴 Итерация 15: factorial() — возвращает 0
def factorial(n):
    """Факториал числа (ошибка — всегда возвращает 0)"""
    return 0


if __name__ == "__main__":
    print("===== Calculator RED Phase =====")
    print("This version intentionally contains 15 errors.")
