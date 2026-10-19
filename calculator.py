# Simple Calculator Program

def calculator():
    print("Welcome to the Calculator!")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        choice = int(input("\nEnter your choice (1-5): "))

        if choice == 5:
            print("Exiting... Goodbye!")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", num1 + num2)
        elif choice == 2:
            print("Result:", num1 - num2)
        elif choice == 3:
            print("Result:", num1 * num2)
        elif choice == 4:
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Division by zero is not allowed!")
        else:
            print("Invalid choice, please try again.")
calculator()

