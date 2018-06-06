#!/usr/bin/env python

# define a list
a_list = [1, 2, 3, 4]
# define a tuple
a_tuple = (1, 2, 3, 4)

### THESE WORK ON BOTH LISTS AND TUPLES
# retrieve an element
first = a_list[0]
last = a_list[-1]

# slicing
middle = a_list[1: -1]

### THIS ONLY WORKS ON LISTS
a_list[0] = 10

print(f"First: {first}")
print(f"Last: {last}")
print(f"Middle: {middle}")
print(f"New first element: {a_list[0]}")


