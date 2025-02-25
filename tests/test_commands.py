import pytest
from calculator.calculator import Calculator

def test_add_command():
    assert Calculator.execute_command('add', 5, 3) == 8

def test_subtract_command():
    assert Calculator.execute_command('subtract', 10, 5) == 5

def test_multiply_command():
    assert Calculator.execute_command('multiply', 4, 2) == 8

def test_divide_command():
    assert Calculator.execute_command('divide', 10, 2) == 5
