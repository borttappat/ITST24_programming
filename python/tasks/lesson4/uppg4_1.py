#!/usr/bin/env python3
'''
1. Multiplikationstabellen
Skapa ett program som genererar och skriver ut en multiplikationstabell för ett tal
som användaren matar in.
Krav:
● En funktion för att skapa en multiplikationstabell.
● Programmet ska fråga användaren vilket tal som ska multipliceras och till
vilket maxvärde.
● En funktion för att kontrollera om den inmatade strängen bara innehåller
siffror. Använd funktionen isdigit()
● Skriv ut tabellen
'''
#input av siffra
while True:
    multiplier = input("Enter number to multiply: ")
    if multiplier.isdigit():
        multiplier = int(multiplier)
        break
    else:
        print("Error, enter a number")

#hur långt ska talet multipliceras
while True:
    multiplicand = input("Enter number to multiply with: ")
    if multiplicand.isdigit():
        multiplicand = int(multiplicand)
        break
    else:
        print("Error, enter a number")


#skapa en tabell med varje steg
result_list = [ multiplier * i for i in range(1, multiplicand + 1)]

#skriv ut tabellen
print("\n")
print("Here is your math table")
print(result_list)

