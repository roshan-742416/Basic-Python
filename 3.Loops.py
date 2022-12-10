my_list1 = [5, 8, 10, 12]
# let's add 5 to each element in the list
# Let's use the for loop
for element in my_list1:
    element = element + 5
    print(element)

# notice that this did not change the my_list1 data values at all
print(my_list1)
for x in range(0, len(my_list1)):
    my_list1[x] += 5
print(my_list1)

# If loop
a = 15
if a % 2 == 0:
    print("a is divisible by 2")
else:
    print("a is not divisible by 2")
