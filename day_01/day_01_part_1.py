import numpy as np

input_array = np.loadtxt("input")

count = 0
for i, a in enumerate(input_array):
    if i == 0:
        continue
    if a > input_array[i-1]:
        count += 1
print(count)
print(len(input_array))