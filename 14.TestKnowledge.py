# Q1

# x = 2
# y = 5
# print(x+y)
# print(x/y)
# print(x-y)
# print(x * y)

# Q2

even = []
for i in range(0, 101):
    if i % 2 == 0:
        even.append(i)
print(even)

# Q3

print(even[:11])

# Q4

even.append(True)
print(even)

# Q4

z = 69
if z % 5 == 0:
    print(z, " is divisible by 5.")
else:
    print(z, " is NOT divisible by 5.")

# Q5
for i in range(0, 6):
    print(i)

# Q6

import turtle

turtle.bgcolor("white")
turtle.color("red")
turtle.speed(0)
print(360 / 5)
for i in range(0, 5):
    turtle.forward(100)
    turtle.left(360 / 5)
turtle.done()

# Q7
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))


def pythagorean(a, b, c):
    return a ** 2 + b ** 2 == c ** 2
if pythagorean(a, b, c):
    print("These are pythagorean triples!")
else:
    print("These are NOT pythagorean triples!")

# Q8

n = 5
while n > 0:
    n = n - 1
    print(n)

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()