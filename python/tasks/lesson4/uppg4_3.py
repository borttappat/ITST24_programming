#!/usr/bin/env python3
'''
Skapa ett program som hanterar en inköpslista. Programmet ska kunna:
● Lägga till, ta bort och visa alla varor till inköpslistan.
● Spara inköpslistan till en textfil (användaren får välja filnamn).
Krav:
● Programmet ska ha en meny där användaren kan välja att lägga till varor, visa
listan, ta bort varor, spara listan eller avsluta programmet.
● Använd funktioner för att strukturera koden och hantera varje menyval.
'''

## Detta program är en shopping-lista
## Ska finnas ett menyval för att lägga till och ta bort saker och
## kunna visa hela listan


## Låta user skapa en lista genom input och sedan concata på
## befintlig list?

## Give user a prompt to save list to file before exit

def add_items(*args):
    shopping_list.update(args)
    for item in args:
      print(f'{item} added to the list')


## making for loop to step through items to bring error when item to
## remove not found
def remove_items(*args):
  for item in args:
    try:
      shopping_list.remove(item)
      print(f'{item} removed from the list')
    except KeyError:  # Sets throw KeyError, not ValueError
      print(f'{item} not found in the list. Skipping...')

def show_items():
  print(shopping_list)

def call_doctor():
  print("Here is the number for the ambulance: 112")

def save_list():
  with open('shopping_list.txt', 'w') as savefile1:
    for item in shopping_list:
      savefile1.write(item + '\n')

  print("Shopping list saved as shopping_list.txt")


shopping_list = set()

while True:
  print("""  Welcome to the Shopping List App!
  *********************************
  1: Add items to the list
  2: Remove items from the list
  3: Show list
  4: Call a Doctor
  5: Save list to a file
  6: Exit""")

  while True:
    user_choice = (input("Enter your choice: "))
    if user_choice.isdigit() and 0 < int(user_choice) < 7:
      break

    print("Invalid choice. Please try again.")

  match user_choice:
    case "1":
      user_input = input("Enter items to add to the list with spaces in between: ")
      items_to_add = user_input.split()
      add_items(*items_to_add)
      input("Press enter to continue... ")

    case "2":
      user_input = input("Enter items to remove from the list with spaces in between: ")
      items_to_remove = user_input.split()
      remove_items(*items_to_remove)
      input("Press enter to continue... ")

    case "3":
      show_items()
      input("Press enter to continue... ")

    case "4":
      call_doctor()
      input("Press enter to continue... ")

    case "5":
      save_list()
      input("Press enter to continue... ")

    case "6":
      user_input = input("Do you wish to save the list to a file before exiting, Y/N? ")
      if user_input.lower() == "Y":
        save_list()
      exit()