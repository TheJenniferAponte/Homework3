# calculator/calculator.py

from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class Calculator:
    """Calculator that executes commands."""
    commands = {
        "add": AddCommand(),
        "subtract": SubtractCommand(),
        "multiply": MultiplyCommand(),
        "divide": DivideCommand(),
    }

    @staticmethod
    def execute_command(command, a, b):
        try:
            a, b = float(a), float(b)
            if command in Calculator.commands:
                return Calculator.commands[command].execute(a, b)
            return f"Error: Unknown command '{command}'"
        except ValueError:
            return "Error: Invalid number input"
