import pytest
from main import calculate

def test_addition():
    assert calculate("5", "3", "add") == "The result of 5 add 3 is equal to 8"

def test_subtraction():
    assert calculate("10", "2", "subtract") == "The result of 10 subtract 2 is equal to 8"
