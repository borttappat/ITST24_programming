#!/usr/bin/env python3
'''
Ladda ner password_spraying.py från ITHSdistans.
Kontrollera om någon utav lösenorden i password_list matchar lösenordet för en
user i user_credentials
Skriv resultatet till fil (och i konsolen) med varje lösenord per user och om det
lyckades eller inte.
Exempel:
user1: 123456 -> failed
user1: Welcome123 -> failed
'''

import os

# Lista över användarnamn och deras korrekta lösenord
user_credentials = {
    "user1": "Password123",
    "admin": "Admin@2023",
    "user2": "Welcome123",
    "guest": "Guest1234"
}

# En lista över vanligt använda lösenord
password_list = ["Password123", "123456", "Welcome123", "Guest1234", "password"]

class MyCache():
  def __init__(self):
      ## Make list to hold the cached data
      self.cache = []

  def add(self, trueuser):
      self.cache.append(user)

  def exists(self, trueuser):
      return trueuser in self.cache

  def clear(self):
      self.cache = []
      del self.cache

cache = MyCache()

with open("password_test_results.txt", 'w') as writefile1:
  for password in password_list:
    for user, userpass in user_credentials.items():
      if cache.exists(user):
        message = f"Password test already succeeded for {user}. Skipping...\n"
        print(message, end='')
        writefile1.write(message)
        continue
      if userpass == password:
        message = f'{user}: {password} -> succeeded\n'
        print(message, end='')
        writefile1.write(message)
        cache.add(user)
      else:
        message = f'{user}: {password} -> failed\n'
        print(message, end='')
        writefile1.write(message)

## Clearing cache and deleting the whole object
cache.clear()
