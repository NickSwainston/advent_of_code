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

winner_order = np.zeros(bingo_boards.shape[0])
winner_count = 1
already_won = []

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
        if (5 in np.sum(bingo_checks[bi], axis=0) or \
            5 in np.sum(bingo_checks[bi], axis=1)) and \
            bi not in already_won:
            print(f"winner {winner_count}!")
            winner_order[bi] = winner_count
            winner_count += 1
            already_won.append(bi)
    if winner_count -1 == bingo_boards.shape[0]:
        final_bingo = int(bnum)
        break

# find last winner
wi = list(winner_order).index(max(winner_order))

print(bingo_boards[wi])
print(bingo_checks[wi])
# perform check math
num_called = 0
num_not_called = 0
for ci in range(5):
    for ri in range(5):
        if int(bingo_checks[wi][ci][ri]) == 0:
            num_not_called += bingo_boards[wi][ci][ri]
print(num_not_called, final_bingo)
print(final_bingo * int(num_not_called))


            