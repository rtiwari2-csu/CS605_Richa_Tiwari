def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def show_menu():
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

while True:
    try:
        a = float(input("\nEnter the first number: "))
        b = float(input("Enter the second number: "))

        show_menu()
        choice = input("Enter your choice (1/2/3/4): ")

        print("\n--- Result ---")

        if choice == '1':
            print(f"{a} + {b} = {add(a, b)}")
        elif choice == '2':
            print(f"{a} - {b} = {subtract(a, b)}")
        elif choice == '3':
            print(f"{a} * {b} = {multiply(a, b)}")
        elif choice == '4':
            print(f"{a} / {b} = {divide(a, b)}")
        else:
            print("Error: Invalid choice. Please enter 1, 2, 3, or 4.")

    except ValueError:
        print("Error: Please enter valid numeric values.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

    again = input("\nWould you like to perform another operation? (yes/no): ").strip().lower()
    if again not in ['yes', 'y']:
        print("see ya bye!")
        break