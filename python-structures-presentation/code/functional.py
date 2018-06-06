#!/usr/bin/env python

a_list = [1, 2, 3, 4, 5, 6, 7]

# MAP OMIT
doubled = map(lambda x: 2 * x, a_list)
# END MAP OMIT

# FILTER OMIT
even = filter(lambda x: x % 2 == 0, a_list)
# END FILTER OMIT

print(f"doubled: {list(doubled)}")
print(f"even: {list(even)}")

# EQUIVALENT OMIT
_map = [2 * x for x in a_list]
_filter = [x for x in a_list if x % 2 == 0]
# END EQUIVALENT OMIT