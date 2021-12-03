import numpy as np

#input_array = np.loadtxt("example", dtype=str)
input_array = np.loadtxt("input", dtype=str)

x = 0
depth = 0

for a in input_array:
    command, value = a
    value = int(value)
    print(value)
    if command == 'forward':
        x += value
    if command == 'down':
        depth += value
    if command == 'up':
        depth -= value
print(f"depth {depth}")
print(f"x {x}")
print(f"ans {x*depth}")