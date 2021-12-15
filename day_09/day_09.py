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
heat_map = np.pad(heat_map, 1, pad_with)
print(heat_map)
#print(ndimage.minimum_filter(heat_map, size=3))
xmax, ymax = heat_map.shape
print(xmax, ymax)
risk_level = 0
min_spots = []
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
            min_spots.append([xi,yi])
print(risk_level)

all_basins = []
for min_spot in min_spots:
    #print(min_spot)
    basin = [min_spot]
    new_spot = True
    while new_spot:
        new_spot = False
        print(basin)
        new_basin = basin
        for base in basin:
            print(base)
            xi, yi = base
            if heat_map[xi-1][yi] < 9 and [xi-1, yi] not in new_basin:
                new_spot = True
                new_basin.append([xi-1, yi])
            if heat_map[xi+1][yi] < 9 and [xi+1, yi] not in new_basin:
                new_spot = True
                new_basin.append([xi+1, yi])
            if heat_map[xi][yi-1] < 9 and [xi, yi-1] not in new_basin:
                new_spot = True
                basin.append([xi, yi-1])
            if heat_map[xi][yi+1] < 9 and [xi, yi+1] not in new_basin:
                new_spot = True
                new_basin.append([xi, yi+1])
        basin = new_basin
    all_basins.append(basin)
print(basin)

basin_sizes = []
for base in all_basins:
    basin_sizes.append(len(base))
basin_sizes.sort()
print(basin_sizes)
print("3 size multiplications", basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])

"""
# put into dict of groups
dict_groups = {}
for di, spot in enumerate(min_spots):
    dict_groups[di] = [spot]
print(dict_groups)

new_group_found = True
while new_group_found:
    new_group_found = False
    for g1 in dict_groups.keys():
        for g2 in dict_groups.keys():
            if g1 != g2:
                for pos1 in dict_groups[g1]:
                    for pos2 in dict_groups[g2]:
                        print(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]))
                        if abs(pos1[0] - pos2[0]) < 2 and \
                           abs(pos1[1] - pos2[1]) < 2:
                            print(pos)
                            new_group_found = True
                            # Append new group
                            dict_groups[g1] = dict_groups[g1] + dict_groups[g2]
                            dict_groups.pop[g2]
print(dict_groups)
"""
