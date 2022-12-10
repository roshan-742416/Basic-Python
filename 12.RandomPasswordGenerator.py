# Random Password Generator
# Import random module
from random import randint
# All uppercase password
password = ""
for i in range(10):
    i = chr(randint(65, 90))
    password = str(password) + i
print(password)

# Upper and lowercase password
password = ""
for i in range(5):
    i = chr(randint(65, 90))
    for j in range(5):
        j = chr(randint(65, 90)).lower()
    password = str(password) + i + j
print(password)

# Upper and lower and number
password = ""
for i in range(3):
    i = chr(randint(65, 90))
    for j in range(3):
        j = chr(randint(65, 90)).lower()
    password = str(password) + i + j + str(randint(1, 10))
print(password)
