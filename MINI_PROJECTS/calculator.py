
print("===== SIMPLE CALCULATOR =====")

while True:

    # First number validation
    while True:
        try:
            num1 = float(input("Enter first number : "))
            break
        except ValueError:
            print("Invalid first number!")

    # Second number validation
    while True:
        try:
            num2 = float(input("Enter second number : "))
            break
        except ValueError:
            print("Invalid second number!")

    # Validate operator
    while True:
        operator = input("Enter your choice (+,-,*,/) : ")

        if operator in ("+", "-", "*", "/"):
            break
        else:
            print("Invalid operator! Try again.")

    # Perform calculation
    if operator == "+":
        print(f"Result is = {num1 + num2}")

    elif operator == "-":
        print(f"Result is = {num1 - num2}")

    elif operator == "*":
        print(f"Result is = {num1 * num2}")

    elif operator == "/":
        if num2 != 0:
            print(f"Result is = {num1 / num2}")
        else:
            print("Cannot divide by zero!")

    # Ask to continue
    choice = input("Do you want to continue? (yes/no): ")

    if choice.lower() == "no":
        print("Thank you for using the calculator!")
        break
