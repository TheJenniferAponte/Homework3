# calculator/calculation.py

class Calculation:
    """Represents a single arithmetic calculation."""

    def __init__(self, operation: str, num1: float, num2: float, result: float):
        self.operation = operation
        self.num1 = num1
        self.num2 = num2
        self.result = result

    def __str__(self):
        return f"{self.num1} {self.operation} {self.num2} = {self.result}"








