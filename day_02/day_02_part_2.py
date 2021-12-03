import numpy as np

#input_array = np.loadtxt("example", dtype=str)
input_array = np.loadtxt("input", dtype=str)

x = 0
depth = 0
aim = 0

for a in input_array:
    command, value = a
    value = int(value)
    print(value)
    if command == 'forward':
        x += value
        depth += aim*value
    if command == 'down':
        aim += value
    if command == 'up':
        aim -= value
print(f"depth {depth}")
print(f"x {x}")
print(f"ans {x*depth}")