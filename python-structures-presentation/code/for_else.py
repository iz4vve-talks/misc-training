#!/usr/bin/env python
# START OMIT
for i in range(4):
    if i == 2:
        print("Skipping: %d" % i)
        # the continue keyword lets you skip an iteration
        continue
    print(i)
else:
    print("Done...")

print("\nBreak loop") 
for i in range(4):
    if i == 2:
        print("break")
        # the break breaks out of the loop
        break
    print(i)
# END OMIT