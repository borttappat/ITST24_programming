#!/usr/bin/env python3
'''
2. Logganalys
Ladda ner log.txt från ITHSdistans. Lägg denna fil i samma katalog som ditt
python-skript.
Öppna filen och läs in den
Skriv ut varje rad i filen som innehåller "Failed login attempt" (utan tomrader)
'''

def search_attempt(filename, word = "Failed login attempt"):
    with open("log.txt", 'r') as file:
        attempt = file.readlines() # Read the file line by line
        for i, line in enumerate(attempt, start=1):
            if word in line:
                print("**************")               
                print(f"The log {word} was found in line {i}.\nHere's how it looks like: \n{line.strip()}")
                print("**************")
search_attempt("log.txt")  # This will search for "Failed login attempt"
