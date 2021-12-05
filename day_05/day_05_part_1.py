import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

input_file = "example"
input_file = "input"
#input_file = "test1"

input_array = co2_array = np.loadtxt(input_file, dtype=str)

if input_file == "example":
    grid = np.zeros((10, 10), dtype=int)
else:
    grid = np.zeros((1000, 1000), dtype=int)

for line in input_array:
    #print(line)
    #c1, c1 = line.split(" -> ")
    c1 = line[0]
    c2 = line[2]
    x1, y1 = c1.split(",")
    x2, y2 = c2.split(",")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    #Loop over movement
    if x1 > x2:
        xd = -1
    else:
        xd = 1
    if y1 > y2:
        yd = -1
    else:
        yd = 1
    if x1 == x2 or y1 == y2:
        #print("line", x1,y1,x2,y2)
        #print("range", x1, x2+xd, xd)
        for xi in range(x1, x2+xd, xd):
            for yi in range(y1, y2+yd, yd):
                #print("    ", xi,yi)
                grid[yi][xi] = grid[yi][xi] + 1
    elif (abs(x1-x2) == abs(y1-y2)):
        #print("line", x1,y1,x2,y2)
        #print("x", xs,xb, "y",ys,yb)
        for xi, yi in zip(range(x1, x2+xd, xd), range(y1, y2+yd, yd)):
                grid[yi][xi] = grid[yi][xi] + 1


#print(grid)
count = 0
for g in grid.flatten():
    if int(g) > 1:
        count += 1
        #print(g)
print("Count",count)