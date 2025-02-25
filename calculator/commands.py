class Command:
    """Base Command class."""
    def execute(self, a, b):
        raise NotImplementedError("Subclasses must implement `execute` method")

class AddCommand(Command):
    """Command for addition."""
    def execute(self, a, b):
        return a + b

class SubtractCommand(Command):
    """Command for subtraction."""
    def execute(self, a, b):
        return a - b

class MultiplyCommand(Command):
    """Command for multiplication."""
    def execute(self, a, b):
        return a * b

class DivideCommand(Command):
    """Command for division."""
    def execute(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
