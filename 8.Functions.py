# Functions

# Like in mathematics, where a function takes an argument and produces a result,
# it does so in Python as well

# The general form of a Python function is
# def dunction_name(arguments):
#   {lines telling the function what to do to produce the result
#   return the result

# Let's consider producing a function that returns x^2

def squared(x):
    return x**2
print(squared(4))

#Let's consider producing a function that gives x^2+y^2

def squared(x,y):   # This is not OOP, just updating function
    return(x**2+y**2)
print(squared(3,4))

# A new function

def born(country):
    return print("I am from "+ country + ".")
born("Nepal")
