import numpy as np

#input_file = "example"
input_file = "input"

import csv
with open(input_file) as csvfile:
     spamreader = csv.reader(csvfile)
     for i, row in enumerate(spamreader):
        if i == 0:
            bingos = row
print(bingos)

input_array = co2_array = np.loadtxt(input_file, skiprows=2, dtype=int)
print(input_array.shape)
bingo_boards = input_array.reshape((len(input_array)//5,5,5))
print(bingo_boards)
print(bingo_boards[0][0][1])
bingo_checks = np.zeros_like(bingo_boards)

for bnum in bingos:
    for bi, board in enumerate(bingo_boards):
        for ci in range(5):
            for ri in range(5):
                print(bingo_boards[bi][ci][ri], bnum)
                if int(bingo_boards[bi][ci][ri]) == int(bnum):
                    # bingo so update check
                    print("hit")
                    bingo_checks[bi][ci][ri] = 1
    #print(bingo_checks)
    # check for a winner
    for bi, board in enumerate(bingo_boards):
        # check columns and rows
        if 5 in np.sum(bingo_checks[bi], axis=0) or \
           5 in np.sum(bingo_checks[bi], axis=1):
            print("winner!")
            print(board)
            print(bingo_checks[bi])
            # perform check math
            num_called = 0
            num_not_called = 0
            for ci in range(5):
                for ri in range(5):
                    if int(bingo_checks[bi][ci][ri]) == 0:
                        num_not_called += bingo_boards[bi][ci][ri]
            print(num_not_called, int(bnum))
            print(int(bnum) * int(num_not_called))
            exit()


            