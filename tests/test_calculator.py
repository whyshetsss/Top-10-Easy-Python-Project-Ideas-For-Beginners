import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pytest
from calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    absolute,
    round_value,
    add_list,
    check_number_type,
    safe_divide,
    percentage,
    square_root
)

#  1. Сложение
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

#  2. Вычитание
def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5

#  3. Умножение
def test_multiply():
    assert multiply(3, 3) == 9
    assert multiply(-2, 4) == -8

#  4–5. Деление и деление на ноль
def test_divide():
    assert divide(8, 2) == 4

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

#  6. Возведение в степень
def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

#  7. Абсолютное значение
def test_absolute():
    assert absolute(-10) == 10
    assert absolute(5) == 5

#  8. Округление
def test_round_value():
    assert round_value(3.14159) == 3.14
    assert round_value(3.14159, 3) == 3.142

#  9. Сумма элементов списка
def test_add_list():
    assert add_list([1, 2, 3]) == 6
    assert add_list([]) == 0

#  10. Проверка типа данных
def test_check_number_type():
    assert check_number_type(5)
    assert check_number_type(5.5)
    assert not check_number_type("string")

#  11. Безопасное деление
def test_safe_divide():
    assert safe_divide(10, 2) == 5
    assert safe_divide(10, 0) is None

#  12. Проценты
def test_percentage():
    assert percentage(50, 200) == 25
    assert percentage(1, 4) == 25

#  13. Квадратный корень
def test_square_root():
    assert square_root(9) == 3
    assert round(square_root(2), 3) == 1.414

#  14. Комбинированная операция
def test_combined_operations():
    result = multiply(add(2, 3), power(2, 2))
    assert result == 20

#  15. Проверка округления в сложных выражениях
def test_round_combined():
    result = round_value(divide(10, 3), 2)
    assert result == 3.33
