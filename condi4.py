# Simple Calculator using match-case
def calculator():
    print("=== Simple Calculator ===")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    match choice:
        case "1":
            print("Result:", a + b)
        case "2":
            print("Result:", a - b)
        case "3":
            print("Result:", a * b)
        case "4":
            if b != 0:
                print("Result:", a / b)
            else:
                print("Error: Cannot divide by zero!")
        case _:
            print("Invalid choice. Please try again.")

# Run the calculator
calculator()
