#!/usr/bin/env python3
'''
Klassisk uppgift. Loopa genom 1-100 med följande regler:
● Om talet är delbart med 3, skriv ut "Fizz".
● Om talet är delbart med 5, skriv ut "Buzz".
● Om talet är delbart med både 3 och 5, skriv ut "FizzBuzz".
● Annars, skriv ut talet självt.
'''

a = 1
b = 100

# when a is smaller than b
while a <= b:
    # if a is divisble by 3 and 5, print "FizzBuzz" and then increment a by 1
    if a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
        a += 1 
    # if not, check if a is divisible by 3 and if so, print Fizz, then increment a by 1
    elif a % 3 == 0:    
        print("Fizz")
        a += 1
    # if not, check if a is divisible by 5 and if so, print Buzz, then increment a by 1
    elif a % 5 == 0:
        print("Buzz")
        a += 1
    # if not, print the number and increment a by 1
    else:
        print(a)
        a += 1
