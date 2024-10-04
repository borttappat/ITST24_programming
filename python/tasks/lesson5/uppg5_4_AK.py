#!/usr/bin/env python3
'''
Skapa en klass Rectangle med attributen length och width.
Implementera metoder för att beräkna arean och omkretsen.
Ta emot och validera input för length och width.
Skriv ut arean och omkretsen
'''

class Rectangle:
    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def area(self):
        area_math = self.length * self.width
        return f"the area of the rectangle is {area_math:.2f}"
        
    def circumference(self):
        circumference_math = 2 * (self.length + self.width)
        return f"the circumference of the rectangle is {circumference_math:.2f}"


while True:
    length = input("\nEnter rectangle length: ")
    if not length.isdigit():
        print(f"{input} is not a valid input")
        continue

    width= input("\nEnter rectangle width: ")
    if not width.isdigit():
        print(f"{width} is not a valid input")
        continue
    
    rect = Rectangle(length, width)

    print(rect.area())
    print(rect.circumference())

    break
