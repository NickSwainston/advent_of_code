import numpy as np
from scipy import ndimage, misc

input_array = np.loadtxt("example", dtype=str)
input_array = np.loadtxt("input", dtype=str)
#input_array = np.loadtxt("test", dtype=str)

def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 9)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value

heat_map = []
for ia in input_array:
    heat_map.append([int(char) for char in ia])
heat_map = np.array(heat_map)
#heat_map = np.pad(heat_map, 1, pad_with)
print(heat_map)
#print(ndimage.minimum_filter(heat_map, size=3))
xmax, ymax = heat_map.shape
print(xmax, ymax)
risk_level = 0
for xi in range(xmax):
    for yi in range(ymax):
        lp_check = True
        #left
        if xi != 0:
            if heat_map[xi][yi] >= heat_map[xi-1][yi]:
                lp_check = False
        # right
        if xi != xmax -1:
            if heat_map[xi][yi] >= heat_map[xi+1][yi]:
                lp_check = False
        # top
        if yi != 0:
            if heat_map[xi][yi] >= heat_map[xi][yi-1]:
                lp_check = False
        # bottom
        if yi != ymax - 1:
            if heat_map[xi][yi] >= heat_map[xi][yi+1]:
                lp_check = False

        if lp_check:
            print(heat_map[xi][yi], xi, yi)
            risk_level += 1 + heat_map[xi][yi]
print(risk_level)

