import numpy as np

input_array = np.loadtxt("input")

summed_array = []
for i, a in enumerate(input_array):
    if i < 2:
        continue
    summed_array.append(np.sum([a, input_array[i-1], input_array[i-2]]))
count = 0
for i, a in enumerate(summed_array):
    if i == 0:
        continue
    if a > summed_array[i-1]:
        count += 1
print(count)