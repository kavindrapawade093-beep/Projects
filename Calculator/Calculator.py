# -----------------------------------
# Simple Calculator App in Python
# -----------------------------------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("===== Calculator App =====")

while True:

    print("\nChoose Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "5":
        print("Calculator Closed")
        break

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if choice == "1":
        print("Result =", add(num1, num2))

    elif choice == "2":
        print("Result =", subtract(num1, num2))

    elif choice == "3":
        print("Result =", multiply(num1, num2))

    elif choice == "4":
        print("Result =", divide(num1, num2))

    else:
        print("Invalid Choice")
