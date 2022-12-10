# Python Types
print(type("Hello World"))
print(type(13))
print(type(4.23))
print(type(True))

# Moving over to integers
print(4,72, int(4.72))
print(4.05, int(4.05))

# Python rounds down
# Rounding up
print(4.72, int(round(4.72)))

# Rounding down
print(4.05, int(round(4.05)))

# Moving strings to integers
print("12345", int("12345"))
print(type("12345"))
print(type(int("12345")))
# You can not get ASCII values like above

print(float(18))

# Moving to strings
print(str(19.6))
print(type(str(19.6)))

# Logical Operators
# There are three different logical operators
# AND, OR, NOT
x = 6
print(x > 0)
print(x > 7)
print(0 < x < 10)
print(0 < x < 5)
y = 23
print(y % 2 == 0)   # This gives False
y = 24
print(y % 2 == 0)   # This gives True
print( y % 2 == 0 or y % 3 == 0)    # Both true
print( y % 2 == 0 or y % 5 == 0)    # this will also give True
