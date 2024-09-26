#!/usr/bin/env python3
'''
1. Skapa ett username från ett namn
Vi har variabeln:
namn = " aNnA kaRlSsOn "
● Ta bort eventuella extra mellanslag i början och slutet av strängen.
● Se till att första bokstaven i varje ord är en versal och resten är
gemener.
● Ersätt mellanslag inuti namnet med bindestreck (-).
● Skriv ut det bearbetade namnet.
'''

name = " aNnA kaRlSsOn "
# print(name)

# trimname = name.strip()
# print(trimname)

# lowercasename = trimname.casefold()
# print(lowercasename)

# titlename = lowercasename.title()
# print(titlename)

# dashname = titlename.replace(" ", "-")

# Shorten the above to a one-line solution that strips, "titelefies" and insert dashes at once.
# No need for the lowercasing as title() changes that.
dashname = name.strip().title().replace(" ","-")


print(dashname)
