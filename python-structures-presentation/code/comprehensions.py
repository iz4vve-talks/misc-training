#!/usr/bin/env python

# START OMIT
a_list = list()
for i in range(10):
    if i % 2:
        a_list.append(i)

# this is equivalent
another_list = [i for i in range(10) if i % 2]

# this has an extra guard
yet_another_list = [i if i % 2 else 10 for i in range(10)]
# END OMIT
print(f"a_list: {a_list}")
print(f"another_list: {another_list}")
print(f"yet_another_list: {yet_another_list}")
