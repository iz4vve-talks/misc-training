#!/usr/bin/env python
import time
start = time.time()
# START OMIT
import numpy as np

counter = [['yes', 0], ['no', 0]]
big_list = np.random.randint(0, 10000, 10000000)
check_list = np.random.randint(0, 99999, 1000)

for number in check_list:
    if number in big_list:
        counter[0][1] = counter[0][1] + 1
    else:
        counter[1][1] = counter[1][1] + 1
# END OMIT
print(counter)

print(f"Script executed in {time.time() - start:.2f} seconds")