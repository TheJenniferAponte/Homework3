# calculator/calculator.py

from calculator.calculation import Calculation

class Calculations:
    """Manages calculation history."""
    history = []  # Class-level attribute to track calculations

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls):
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls):
        cls.history.clear()

class Calculator:
    """Performs basic arithmetic operations."""

    @staticmethod
    def add(num1: float, num2: float) -> float:
        result = num1 + num2
        Calculations.add_calculation(Calculation("+", num1, num2, result))
        return result

    @staticmethod
    def subtract(num1: float, num2: float) -> float:
        result = num1 - num2
        Calculations.add_calculation(Calculation("-", num1, num2, result))
        return result

    @staticmethod
    def multiply(num1: float, num2: float) -> float:
        result = num1 * num2
        Calculations.add_calculation(Calculation("*", num1, num2, result))
        return result

    @staticmethod
    def divide(num1: float, num2: float) -> float:
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        result = num1 / num2
        Calculations.add_calculation(Calculation("/", num1, num2, result))
        return result

