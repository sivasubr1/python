import math
import numpy as np

MAX_RANGE = 100

a = np.ones(MAX_RANGE)

for i in range(2, int(math.sqrt(MAX_RANGE))):
    for j in range(i * i, MAX_RANGE, i):
        a[j] = 0

for i in range(2, MAX_RANGE):
    if a[i] == 1:
        print(i)

