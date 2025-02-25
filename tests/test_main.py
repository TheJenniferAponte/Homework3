import pytest
from calculator.calculator import Calculator

def test_add():
    assert Calculator.execute_command('add', 5, 3) == 8

def test_subtract():
    assert Calculator.execute_command('subtract', 5, 3) == 2

def test_multiply():
    assert Calculator.execute_command('multiply', 4, 2) == 8

def test_divide():
    assert Calculator.execute_command('divide', 10, 2) == 5

def test_divide_by_zero():
    assert Calculator.execute_command('divide', 1, 0) == "Error: Cannot divide by zero"
