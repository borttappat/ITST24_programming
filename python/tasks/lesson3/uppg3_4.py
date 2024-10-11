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

# testa göra med functions?
# gör så aktiva ips skrivs i filen direkt efter dom pingats

import os

ips = [*range(1, 256)]
reachable_ips = []

with open("ips.txt", "w") as my_file:
    for ip in ips:
        my_file.write("10.2.10." + str(ip) + "\n")


with open("ips.txt") as my_file:
    for ip in my_file:
        ip = ip.rstrip()
        up = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
        if up == 0:
            reachable_ips.append(ip)
            print(f"{ip.rstrip()} is up")
            continue
        print(f"{ip.rstrip()} is not up")


with open("reachable_ips.txt", "w") as my_file:
    for ip in reachable_ips:
        my_file.write(ip + "\n")
