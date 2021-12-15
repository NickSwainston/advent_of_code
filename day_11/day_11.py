import numpy as np

input_array = np.loadtxt("input", dtype=str)
#input_array = np.loadtxt("example", dtype=str)
#input_array = np.loadtxt("test", dtype=str)

split_ints = []
for row in input_array:
    split_ints.append([int(char) for char in row])

input_array = np.array(split_ints, dtype=int)
xsize, ysize = input_array.shape
print(input_array)

def flash(array, x, y, xsize, ysize):
    #array[x][y] = 0
    if x > 0 and y > 0:
        array[x-1][y-1] += 1
    if y > 0:
        array[x][y-1]   += 1
    if x < xsize - 1 and y > 0:
        array[x+1][y-1] += 1
    if x > 0 and y < ysize - 1:
        array[x-1][y+1] += 1
    if y < ysize - 1:
        array[x][y+1]   += 1
    if x < xsize - 1 and y < ysize - 1:
        array[x+1][y+1] += 1
    if x > 0:
        array[x-1][y]   += 1
    if x < xsize - 1:
        array[x+1][y]   += 1
    return array

total_flash = 0
#print(flash(np.zeros((3,3)), 1, 1, 3, 3))
for step in range(1000):
    input_array = input_array + 1
    still_flashing = True
    flashed = []
    while still_flashing:
        still_flashing = False
        for xi in range(xsize):
            for yi in range(ysize):
                if input_array[xi][yi] > 9 and (xi,yi) not in flashed:
                    # FLASH!
                    still_flashing = True
                    total_flash += 1
                    #print(xi, yi)
                    input_array = flash(input_array, xi, yi, xsize, ysize)
                    flashed.append((xi,yi))
        #print(flashed)
    #print(step, len(flashed))
    if len(flashed) == xsize * ysize:
        print("step", step + 1)
    for xi, yi in flashed:
        input_array[xi][yi] = 0
print(input_array)
print(total_flash)
