#!/usr/bin/env python3
'''
Skapa en enkel miniräknare som kan utföra addition, subtraktion, multiplikation och
division.
Krav:
● Funktioner för varje matematiskt operation.
● Programmet ska ta in två tal från användaren och en operation som input.
● Hantera felaktig inmatning och division med 0.
'''

while True:
    num1 = input("Enter your first number(1 out of 2): ")
    if num1.isdigit():
        num1 = int(num1)
        break
    else:
        print("Error, enter a number")

while True:
    num2 = input("Enter your second number(2 out of 2): ")
    if num2.isdigit():
        num2 = int(num2)
        break
    else:
        print("Error, enter a number")


while True:
    operator = input("What operation do you wish to perform? (+, -, * or /): ")
    if operator == "+":
        print(f"{num1} + {num2} is {num1 + num2}")

    elif operator == "-":
        print(f"{num1} - {num2} is {num1 - num2}")

    elif operator == "*":
        print(f"{num1} * {num2} is {num1 * num2}")

    elif operator == "/":
        if num2 != 0:
            print(f"{num1} / {num2} is {num1 / num2}")
        else:
            print("Error: Division by zero")

    else:
        print("Invalid operator. Please enter +, -, *, or /")

    break  

