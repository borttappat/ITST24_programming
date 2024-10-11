#!/usr/bin/env python3

'''
Skriv en funktion som tar emot ett godtyckligt antal args och kwargs, och sedan skriver ut
dessa på ett strukturerat sätt.
'''
'''
def order_pizza(, **kwargs):
    print(f"you have ordered {args} pizzas with {kwargs} as toppings")
'''
def order_pizza(size, *toppings):
    print(f"\nOrdering a {size} pizza with the following toppings: ")
    for topping in toppings:
        print(f"{topping}")

def user_input():
    size = input("What pizza size would you like to order? (small, medium or large): ")
    
    toppings = []
    while True:
        topping = input("What topping would you like? (enter an item and press Return, end with an empty input): ")
        if topping == "":
            break
        toppings.append(topping)

    return size, toppings

def main():
    print("PizzaPy - the pizza ordering app written in python")
    size, toppings = user_input()
    order_pizza(size, *toppings)

if __name__ == "__main__":
    main()
