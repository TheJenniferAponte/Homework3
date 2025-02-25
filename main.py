from calculator.calculator import Calculator

def print_menu():
    """Displays available commands."""
    print("\nAvailable Commands:")
    print("  add [a] [b]       - Add two numbers")
    print("  subtract [a] [b]  - Subtract two numbers")
    print("  multiply [a] [b]  - Multiply two numbers")
    print("  divide [a] [b]    - Divide two numbers")
    print("  menu              - Show this menu")
    print("  exit              - Exit the calculator\n")

def repl():
    """Interactive calculator using REPL (Read-Eval-Print Loop)."""
    print("Welcome to the interactive calculator! Type 'menu' for options or 'exit' to quit.")
    print_menu()
    
    while True:
        user_input = input("\nEnter command: ").strip().lower()
        
        if user_input == "exit":
            print("Goodbye!")
            break
        if user_input == "menu":
            print_menu()
            continue

        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid input. Example usage: add 5 3")
            continue

        command, a, b = parts
        result = Calculator.execute_command(command, a, b)
        print(result)

if __name__ == "__main__":
    repl()
