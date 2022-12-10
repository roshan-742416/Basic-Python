# Tuples in Python

# Conventionally Tuples look like lists
Fruit = ("Apples", 4, "Bananas", 5, "Oranges", 6)
print(type(Fruit))
List_of_fruit = ["Apples", 4, "Bananas", 5, "Oranges", 6]
print(type(List_of_fruit))
List_of_fruit[0] = "Strawberries"
print(List_of_fruit)
# We can modify elements in lists
# We can't modify elements in tuples

# We can perform similar operations on tuples like we can on lists
print(Fruit[3:])

# Concatenation of tuples
Fruit = Fruit[:4] + ("Cherries", 10)
print(Fruit)

x = (5) # This is not a tuple
print(type(x))
y = (5, )   # This is the notation of tuple with one element
print(type(y))

#We can find the length of tuple
print(len(Fruit))

# Creating a tuple
another_tuple = tuple(("Hello", 18, True))  #Needs two brackets
print(type(another_tuple))
print(another_tuple)

#Converting a tuple into a list
Fruit = list(Fruit)
print(type(Fruit))
Fruit.append("Pear")
print(Fruit)
Fruit = tuple(Fruit)
print(type(Fruit))

# Unpacking tuples
Fruit = ("Apples", "Bananas", "Pears", "Oranges", "Strawberries")
(one, *two, three) = Fruit
print(one)
print(two)  # Notice this gives a list not tuple
print(three)

# Incorporate loops within tuples
for i in range(len(Fruit)):
    print(Fruit[i])
