#!/usr/bin/env python3
'''
Lägg till IP-adresser från tailscale-miljön i en text fil (en ip-adress per rad).
Öppna filen och pinga varje ip-adress. Skriv ut resultatet till terminalen och till en fil.
Använd följande i toppen av ditt skript:
import os
Os-funktion för att pinga en adress (en funktion för win och en för linux):
os.system(f"ping -c 1 {ip_address} > /dev/null 2>&1") # Linux
os.system(f"ping -n 1 {ip_address} > NUL 2>&1") # Windows
'''


