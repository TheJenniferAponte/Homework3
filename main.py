from calculator.calculator import Calculator

def repl():
    print("Welcome to the interactive calculator!")
    print("Commands: add, subtract, multiply, divide, or 'exit' to quit.")
    
    while True:
        command = input("Enter command: ")
        if command == "exit":
            print("Exiting...")
            break

        try:
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            result = Calculator.execute_command(command, a, b)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()
