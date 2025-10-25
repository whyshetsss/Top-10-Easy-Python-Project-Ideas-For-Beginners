import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from calculator import add


def test_addition():
    """Проверяем базовую работу функции сложения"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_multiply():
    """Проверяем умножение (ожидаем ошибку, функции пока нет)"""
    from calculator import multiply
    assert multiply(2, 3) == 6
