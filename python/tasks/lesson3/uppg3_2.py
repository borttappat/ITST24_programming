#!/usr/bin/env python3
'''
2. Logganalys
Ladda ner log.txt från ITHSdistans. Lägg denna fil i samma katalog som ditt
python-skript.
Öppna filen och läs in den
Skriv ut varje rad i filen som innehåller "Failed login attempt" (utan tomrader)
'''
with open('log.txt', 'r') as file:
    for line in file: 
        if 'Failed login attempt' in line:
            print(line)
