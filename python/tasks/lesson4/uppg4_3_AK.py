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
#import os to handle files
import os

shopping_list = []

def add_item():
    global shopping_list
    
    item = input("What item would you like to add?: ")
    if not item.strip():
        print("Error: empty input")
    else:
        print(f"{item} has been added")
        shopping_list.append(item)


def del_item():
    global shopping_list

    item = input("What item would you like to add?: ")
    if not item.strip():
        print("Error: empty input")
    
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed")
        
    else:
        print(f"Error, {item} does not exist in list")

def show_items():
    print(shopping_list)


def save_list():
    global shopping_list

    filename = input("What would you like to save the list as?: ")


    # Add .txt extension if not provided
    if not filename.lower().endswith('.txt'):
        filename += '.txt'

    
    try:
        with open(filename, 'w') as file:
           for item in shopping_list: 
                file.write(f"{item}\n")
        print(f"Shopping list save to {filename}")

    except IOError:
        print(f"Error: Unable to save the file {filename}")
    
    except FileExistsError:
        print(f"Error: {filename} already exists")
        save_list()

def load_list():
    global shopping_list

    filename = input("What file do you wish to read from?: ")
    try:
        with open(filename, 'r') as file:
            shopping_list.clear()
            for line in file:
                item = line.strip()
                if item:
                    shopping_list.append(item)
        print(f"Shopping list loaded from {filename}")
    except FileNotFoundError:
        print("Error: file not found")
    except IOError:
        print("Error: There was an issue reading the file")


def term_program():
    print("Exiting program...")
    exit()

def main():
    global shopping_list

    while True:
        print("\nShopping List Menu:")
        print("1 - Add item")
        print("2 - Remove item")
        print("3 - Show list")
        print("4 - Open list")
        print("5 - Save list")
        print("6 - Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_item()

        elif choice == '2':
            del_item()

        elif choice == '3':
            show_items()

        elif choice == '4':
            load_list()

        elif choice == '5':
            save_list()

        elif choice == '6':
            term_program()

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
