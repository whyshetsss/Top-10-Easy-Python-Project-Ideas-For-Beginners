import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from calculator import add, subtract
    
def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6

def test_subtract_negative():
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 3) == 9
