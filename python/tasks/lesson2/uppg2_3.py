#!/usr/bin/env python3
'''
● Lägg till filmen "Memento" till slutet av listan.
● Byt ut filmen "The Matrix" mot "The Lord of the Rings".
● Ta bort filmen "The Prestige" från listan.
● Sätt in filmen "The Dark Knight" på position 2 i listan.
● Skriv ut den slutgiltiga listan.

'''

list = ["Inception", "The Matrix", "Interstellar", "The Prestige"]

print(list)

list.append("Memento")
print(list)

list[1] = "The Lord of the Rings"

print(list)

list.pop(3)
print(list)

list.insert(1, "The Dark Knight")
print(list)

