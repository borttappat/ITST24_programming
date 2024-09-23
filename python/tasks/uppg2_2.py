#!/usr/bin/env python3
'''
2. Beställning på ICA
En kund har lagt en beställning som innehåller följande varor i angiven
ordning:
"bröd", "mjölk", "ägg", "smör", "ost", "yoghurt"
Skapa en tuple som innehåller kundens beställning. Skriv ut:
● De första tre varorna i beställningen.
● De sista två varorna i beställningen.
● Varannan vara från beställningen.
'''
korg = tuple(('bröd', 'mjölk', 'ägg', 'smör', 'ost', 'yoghurt'))

print(korg[0:3])
print(korg[4:6])

print(korg[::2])

