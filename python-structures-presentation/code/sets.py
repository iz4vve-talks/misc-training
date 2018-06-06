#!/usr/bin/env python

# DEFINE OMIT
# DEFINE A SET:

# using `set` keyword
s = set([1, 2, 3, 1, 1])  # {1, 2, 3}  order might be different 
#using braces
s1 = {1, 2, 2, 3, 3, 1}   # {1, 2, 3}  order might be different 
# DEFINE END OMIT

# OPERATIONS OMIT
set1 = set([1, 2, 3])
set2 = set([3, 4, 5])

union = set1 | set2
intersection = set1 & set2
difference = set1 - set2
symm_difference = set1 ^ set2
# OPERATIONS END OMIT

print(f"Set1: {set1}")
print(f"Set2: {set2}")
print()
print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Difference: {difference}")
print(f"Symmetric difference: {symm_difference}")