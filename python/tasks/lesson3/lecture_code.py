## IF satser ##

# x = 10
# if x > 5:
#     print("x är större än 5")


# x = 10
# if x > 15:
#      print("x är större än 15")
# elif x > 5:
#      print("x är större än 5 men mindre än eller lika med 15")

# x = 3
# if x > 15:
#     print("x är större än 15")
# elif x > 5:
#     print("x är större än 5 men mindre än eller lika med 15")
# else:
#     print("x är mindre än eller lika med 5")


# x = 20
# if x > 10:
#     print("x är större än 10")
#     if x > 20:
#         print("x är större än 20")
#     else:
#         print("x är mindre än eller lika med 20")

## For loopar ##

# fruits = ("apple", "banana", "cherry")
# for fruit in fruits:
#     print(fruit)

# people = [("Anna", 23), ("Eva", 45), ("Kalle", 34)]
# for name, age in people:
#     print(f"{name} är {age} år gammal")

# person = {"name": "Bobbo", "age": 34, "city": "Uppsala"}
# for key, value in person.items():
#     print(f"{key}: {value}")

# text = "Hello World"
# for letter in text:
#     print(letter)

# person = {"name": "Bobbo", "age": 34, "city": "Uppsala"}
# for key in person.keys():
#     print(key)


# person = {"name": "Bobbo", "age": 34, "city": "Uppsala"}
# for value in person.values():
#     print(value)

# for i in range(1,101):
#     print(i)

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# ports = [22, 80, 443, 8080, 3306]
# open_ports = [22, 80, 443]

# for port in ports:
#     if port in open_ports:
#         print(f"Port {port} is open")
#     else:
#         print(f"Port {port} is closed")

## While loopar ##

# x = 0
# while x < 10:
#     print(x)
#     x += 1

# x = 0
# while x < 10:
#     print(x)
#     if x == 5:
#         break
#     x += 1

# x = 0
# while x < 10:
#     print(x)
#     x += 1
#     if x == 5:
#         break
# else:
#     print("Loop is done")

# password = input("Enter password: ")
# while len(password) < 8:
#     print("Password is too short")
#     password = input("Enter password: ")
# print("Password is ok")

## Logiska operatörer ##

# a = True
# b = False

# print(a and b)
# print(a or b)
# print(not a)

# x = 5
# print(1 < x < 10)
# print(1 < x and x < 10)

# a = 5
# b = 10
# c = 15

# if a < b < c:
#     print("a is less than b and b is less than c")

## Files ##

# file = open("log.txt", 'r')
# content = file.read()
# print(content)
# file.close()

# file = open("log.txt", 'r')
# line = file.readline()
# while line:
#     print(line, end="")
#     line = file.readline()
# file.close()

# file = open("log.txt", 'r')
# line = file.readline()
# print(line)

# file = open("log.txt", 'r')
# lines = file.readlines()
# for line in lines:
#     print(line, end="")
# file.close()

# file = open("log.txt", 'r')
# lines = file.read().splitlines()
# print(lines)

# file = open("example.txt", 'w')
# file.write("Hello World\n")
# file.write("This is a test\n")
# file.close()

# file = open("example.txt", 'a')
# file.write("This is a test\n")
# file.close()

# with open("example.txt", 'r') as file:
#     content = file.read()
#     print(content)

# with open("example.txt", 'w') as file:
#     file.write("Hello World\n")

# try:
#     file = open("log.txt", 'r')
#     content = file.read()
#     print(content)
#     file.close()
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:

# except Exception as e:
#     print(e)

