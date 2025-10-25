"""
Calculator module for TDD demo (GREEN phase).
Фаза GREEN — все функции реализованы корректно и проходят тесты.
Цель: все тесты должны завершаться успешно.
"""

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b











