import numpy as np

input_array = np.loadtxt("example", dtype=str)

for line in input_array:
    open_track = {"(":0,
                  "[":0,
                  "{":0,
                  "<":0}
    print(line)
    for letter in line:
        if letter in ["(", "[", "{", "<"]:
            open_track[letter] += 1
        
        if letter == ")" and open_track["("] > 0:
            open_track["("] -= 1
        if letter == "]" and open_track["["] > 0:
            open_track["["] -= 1
        if letter == "}" and open_track["{"] > 0:
            open_track["{"] -= 1
        if letter == ">" and open_track["<"] > 0:
            open_track["<"] -= 1
    if open_track["("] > 0 or \
       open_track["["] > 0 or \
       open_track["{"] > 0 or \
       open_track["<"] > 0 and \
       line[-1] in [")", "]", "}", ">"]:
        print(line[-1])