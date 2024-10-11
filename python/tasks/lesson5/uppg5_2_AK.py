#!/usr/bin/env python3
'''
Skriv ett program som använder lambda-uttryck tillsammans med map och filter för att
bearbeta en lista av tal.
Programmet ska först kvadrera alla tal i listan och sedan filtrera ut de tal som är större än ett
angivet värde.
Krav:
Använd map för att kvadrera alla tal i listan.
Använd filter för att behålla endast de tal som är större än ett specificerat värde.
Använd lambda-uttryck för både map och
filter.
'''

filter_number = int(input("Whats the smallest number you want to keep in the list: "))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared)

filtered = list(filter(lambda x: x >= filter_number, squared))
print(f"Numbers larger than {filter_number}: ", filtered)


