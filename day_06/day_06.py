import sys
import numpy as np
import csv
import numpy.ma as ma

input_file = "example"
input_file = "input"
#input_file = "test1"

with open(input_file) as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        input_array = row
input_array = np.array(input_array, dtype=int)
#print("Initial state:", input_array)

# Make neat data type
fish_counts = {
               "0":np.count_nonzero(input_array == 0),
               "1":np.count_nonzero(input_array == 1),
               "2":np.count_nonzero(input_array == 2),
               "3":np.count_nonzero(input_array == 3),
               "4":np.count_nonzero(input_array == 4),
               "5":np.count_nonzero(input_array == 5),
               "6":np.count_nonzero(input_array == 6),
               "7":np.count_nonzero(input_array == 7),
               "8":np.count_nonzero(input_array == 8),
              }

for day in range(1, 256+1):

    #Loop over current fish
    """
    new_list = []
    new_fish_n = 0
    for fish in input_array:
        if fish == 0:
            # new fish
            new_fish_n += 1
            new_list.append(6)
        else:
            new_list.append(fish - 1)
    # add new fish
    input_array = new_list + [8] * new_fish_n
    """

    # do matrix stuff
    """
    # count new fish
    new_fish_n = np.count_nonzero(input_array == 0)
    # age non zero fish
    not_new_fish = input_array[input_array != 0] - 1
    # put them together
    new_array = np.concatenate((not_new_fish, np.array([6]*new_fish_n), np.array([8]*new_fish_n)))
    #[~np.array(mask)]
    """
    new_fish_n = fish_counts["0"]
    new_fish_counts = {
               "0":fish_counts["1"],
               "1":fish_counts["2"],
               "2":fish_counts["3"],
               "3":fish_counts["4"],
               "4":fish_counts["5"],
               "5":fish_counts["6"],
               "6":fish_counts["7"] + new_fish_n,
               "7":fish_counts["8"],
               "8":new_fish_n,
              }


    #print("After {:3d} days: {}".format(day, new_array))
    fish_counts = new_fish_counts
print("Total of {} fish".format(fish_counts["0"] +\
                                fish_counts["1"] +\
                                fish_counts["2"] +\
                                fish_counts["3"] +\
                                fish_counts["4"] +\
                                fish_counts["5"] +\
                                fish_counts["6"] +\
                                fish_counts["7"] +\
                                fish_counts["8"]))