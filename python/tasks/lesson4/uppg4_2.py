#!/usr/bin/env python3
'''
Skapa en enkel miniräknare som kan utföra addition, subtraktion, multiplikation och
division.
Krav:
● Funktioner för varje matematiskt operation.
● Programmet ska ta in två tal från användaren och en operation som input.
● Hantera felaktig inmatning och division med 0.
'''

## Little spaghetti on the error handling but hopefully tasteful
## Mixed between having try|except inside functions and outside to get a feel
## while learning

## This program is a calculator
from decimal import *

def is_float(userinput):
  try:
    float(userinput)
    return True
  except ValueError:
    return False


def add(arglist):
  return sum(arglist)


def subtract(arglist):
  result = arglist[0]
  for num in arglist[1::]:
    result = result - num
  return result

def multiply(arglist):
  result = arglist[0]
  for num in arglist[1:]:
    result = result * num
  return result


def divide(startnumber):
  result = Decimal(startnumber)

  while True:

    divider = input("Enter a divider, type 0 to stop: ")

    if divider == '0':
      break

    try:
      divider_value = Decimal(divider)

      if divider_value == 0:
        print("Cannot divide by zero. Please enter a valid number.")
        continue

      result = result / divider_value
      print(f"Current result: {result}")

    except InvalidOperation:
      print("Invalid input. Please enter a numeric value.")

def mymodulus(arg1, arg2):
  return arg1 % arg2

def mysquared(arg):
  return arg * arg

def mycubed(arg):
  return arg * arg * arg

def exponent(arg1, arg2):
  return arg1 ** arg2


while True:
  print("""  Welcome to the Calculator!
  **************************
  1: Addition
  11: Addition to Infinity
  2: Subtraction
  3: Multiplication
  4: Division
  5: Modulus
  6: Squared
  7: Cubed
  8: Exit""")

  while True:
   user_choice = (input("Enter your choice: "))
   if user_choice.isdigit() and 0 < int(user_choice) < 9:
     break

   if user_choice == '11':
     break

   print("Invalid choice. Please try again.")

  match user_choice:

    case '1':
      while True:
        inputerror = 0
        innumbers = input("Input numbers to add with space in between: ").split()

        for num in innumbers:
          if not is_float(num) and not num.isdigit():
              inputerror = 1

        if not inputerror:
          break

        print("Error in input. Please try again.")

      intinnumbers = list(map(int, innumbers))

      result = add(intinnumbers)
      print(result)

      while not input("Press enter to continue... ") == '\n':
        break

    case '11':
      try:
        result = int(input("Input a starting number: "))
        while True:
          print("Current result: ", result)
          addthis = input("Add, end addition with 'e': ")
          if addthis == 'e':
            break
          result = result + int(addthis)

      except ValueError as e:
        print("Invalid input. Error: ", e)
        while not input("Press enter to continue... ") == '\n':
          break
        continue

    case '2':
        try:
          sublist = (list(map(int, input("Input start value and numbers to substract with space separated: ").split())))
          subresult = subtract(sublist)
          print("Current result: ", subresult)

          while True:
            newsub = input("Subtract more. Stop with 'e': ")
            if newsub == 'e':
              break

            subresult = subresult - int(newsub)
            print("Current result: ", subresult)

        except ValueError as e:
          print("Invalid input. Error: " + str(e))
          while not input("Press enter to continue... ") == '\n':
            break
          continue

        while not input("Press enter to continue... ") == '\n':
          break

    case '3':
      try:
        multilist = (list(map(int, input("Input start value and numbers to multiply with space separated: ").split())))
        multiresult = multiply(multilist)
        print("Current result: ", multiresult)

        while True:
          newmulti = input("Multiply more. Stop with 'e': ")
          if newmulti == 'e':
            break

          multiresult = multiresult * int(newmulti)
          print("Current result: ", multiresult)

      except ValueError as e:
        print("Invalid input. Error: " + str(e))
        while not input("Press enter to continue... ") == '\n':
          break
        continue

      while not input("Press enter to continue... ") == '\n':
        break

    case '4':
      while True:
        innumber = input("Enter number: ")
        if innumber.isdigit() or is_float(innumber):
          break

        print("Invalid input. Please input a number")
      divide(innumber)
      while not input("Press enter to continue... ") == '\n':
        break

    case '5':
      while True:
        innumber1 = input("Enter number: ")
        innumber2 = input("Enter a modulus: ")

        if (innumber1.isdigit() or is_float(innumber1)) and (innumber2.isdigit() or is_float(innumber2)):
          break

        print("Invalid input. Please input a number")

      print("Result: ", mymodulus(int(innumber1), int(innumber2)))

      while not input("Press enter to continue... ") == '\n':
        break

    case '6':
      while True:
        innumber = input("Enter number: ")
        if innumber.isdigit() or is_float(innumber):
          break

        print("Invalid input. Please input a number")

      print("Result: ", mysquared(int(innumber)))

      while not input("Press enter to continue... ") == '\n':
        break

    case '7':
      while True:
        innumber = input("Enter number: ")
        if innumber.isdigit() or is_float(innumber):
          break

        print("Invalid input. Please input a number")
      print("Result: ", mycubed(int(innumber)))
      while not input("Press enter to continue... ") == '\n':
        break

    case '8':
      exit()



