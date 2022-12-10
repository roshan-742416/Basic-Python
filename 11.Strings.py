# Strings
# We have already covered strings, integers, floats, booleans and lists
# Integers, floats, and booleans are al considered to be simple data types
# They can not be broken down

# Lists and strings are different! They are made up of smaller pieces
# Which can be broken down

# We already know what strings are
print("Hello World")
print(type("Hello World"))
print(str("Hello World"))

# Operations in Strings
# addition sign concatenation
Greeting = "Hello "
Name = "Roshan Poudel "
print(Greeting + Name)
print("My shoe size is ", 5, " and my age is", 23)

# Star operator
print(Greeting * 3)
print(Greeting + Name * 3)
print((Greeting + Name) * 3)

# Index operator
Name = "Roshan"
print(Name[2])
print(Name[0]+Name[4])
print(Name[0:4])    # This is smilar to the range operator 0 to N-1
print(Name[:6])
print(Name[2:])
print(Name.lower())
print("Roshan".upper())
print(Name.count("R"))
print(Name.count("r"))
print(Name.replace("R", "A"))
print(Name.replace("o", "i"))
print(len(Name))

# Format strings
your_name = input("Your name:")
hello = "Hello {}".format(your_name)
print(hello)

# Each letter in Python is assigned to a specific number
print("orange"<"strawberry")
print(ord("o"))
print(chr(111))
# We can perform maths in strings

# in and not operators
fruit = "banana"
print("a" in fruit)
print("s" in fruit)

# Incorporate a few things we have learnt
x = "hello"
y = ""
for character in x:
    y=character.upper() +y
print(y)