# Lists
my_list1 = [1, 2, 3, 4, 5, 6]
my_list2 = list(range(1, 1020, 178))
print(my_list1)
print(my_list2)
print(type(my_list1))
print(type(my_list2))
print(type({1, 2, 3, 4}))


# List operations

# this starts from 0
print(my_list1[0])

# this starts reversing from 1
print(my_list1[-1])

# let us create a slice from 2nd element to the 4th element

print(my_list1[1:3])
# WRONG
# didn't work , it is similar to the range


print(my_list1[1:4])
print(len(my_list1))
print(max(my_list1))
print(min(my_list1))
my_list1 += [1]
print(my_list1)
my_list1.append(120)
print(my_list1)

# Reverse a list
my_list1.reverse()
print(my_list1)

# create another list and add another list to this one
print(my_list1 + my_list2)
print(my_list2 + my_list1)

#you could also change permanently but not recommended
# my_list2 += my_list1
# print(my_list2)