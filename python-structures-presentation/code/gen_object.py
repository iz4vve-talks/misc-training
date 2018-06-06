#!/usr/bin/env python

# START OMIT
# same syntax as comprehensions, but with parentheses
gen_obj = (i for i in range(10) if i % 2)

# generators are usually used in loops:
for item in gen_obj:
    print(item)
# END OMIT