#!/usr/bin/env python3
'''
Skapa en klass Person med attributen name och age.
Använd en while-loop för att ta emot användarens namn och ålder.
Validera att åldern är ett heltal
Skapa och skriv ut ett Person-objekt om inputen är giltig.
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def output_name(self):
        return f"Your name is {self.name}"

    def output_age(self):
        return f"You are {self.age} years old"

while True:
    input_age = input("\nHow old are you? ")

    if not input_age.isdigit():
        print(f"{input_age} is not a valid age") 
        continue
    

    input_name = input("What is your name? ")
    
    me = Person(input_name, input_age)
    
    print(me.output_name())
    print(me.output_age())

    break


