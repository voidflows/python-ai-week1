num1 = float(input("Enter a number : "))
num2 = float(input("Enter a number : "))

operator = input(f"Enter your choice (+,-,*,/) : ")

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
        print(f"Cannot divide by zero")
else:
    print(f"Invalid operator")
