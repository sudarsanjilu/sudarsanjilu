from numpy import random
import numpy as np
arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)
arr2 = np.array([50,60,70,80])
random.shuffle(arr2)
arr3 = random.permutation(arr2)

print(arr)
print(arr2)
print("permutation")
print(arr3)