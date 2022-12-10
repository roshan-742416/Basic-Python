# Booleans
print(True)
print(False)
print("True")
# But these are different

print(type(True))  # This type is a bool
print(type("True"))  # This type is a string
print(5 == 5)

# Incorporating the if statement with a boolean
x = 11
y = 5
if x % y == 0:
    print(x % y == 0)
else:
    print(x % y == 0)

# While loop
number = 1
while number < 4:
    print(number)
    if number == 2:
        break
    number += 1

# Incorporating the else statement within the while loop
number = 2
while number< 4:
    print(number)
    number += 1
else:
    print("number is no longer less than 4")
