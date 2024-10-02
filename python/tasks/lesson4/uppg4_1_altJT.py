## This program will show the multiplication
## table for a number that the user inputs

while True:
  print("Welcome to the multiplicator")
  innum = input("Enter a number to multiply: ")
  inmax = input("Enter a max value as stop: ")

  if innum.isdigit() and inmax.isdigit():
    break

  print("Incorrect format. Input integer only")

def multiplicator(parnum, parmax):

  for i in range(1, parmax//parnum + 1):
    multiply_result = parnum * i
    print(f'{i}: {multiply_result}')

multiplicator(int(innum), int(inmax))