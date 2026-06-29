#!/usr/bin/python3
num1 = int(input("Enter the first number: "))
operator = input("Choose an operator; + - * / or **: ")
num2 = int(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print("The result is: ", result)
elif operator == "-":
    result = num1 + num2
    print("The result is: ", result)
elif operator == "*":
    result = num1 * num2
    print("The result is: ", result)
elif operator == "/":
    result = num1 / num2
    print("The result is: ", result)
elif operator == "**":
    result = num1 ** num2
    print("The result is: ", result)
else:
    print("Error")
