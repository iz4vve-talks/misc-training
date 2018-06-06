#!/usr/bin/env python
# DEFINE OMIT
# DEFINE A DICT
# using curly braces (preferred way)
vowels = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u'}
# using the keyword `dict`
vowels = dict([(1, 'a'), (2, 'e'), (3, 'i'), (4, 'o'), (5, 'u')])
# DEFINE END OMIT

# OPERATIONS OMIT
value_at_1 = vowels[1]
# OPERATIONS END OMIT
print(f"vowels: {vowels}")
print(f"Value at key 1: {value_at_1}")