import numpy as np

input_array = np.loadtxt("input", dtype=str)
#input_array = np.loadtxt("example", dtype=str)
#input_array = np.loadtxt("test", dtype=str)

"""
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
    print(open_track)
    if open_track["("] > 0 or \
       open_track["["] > 0 or \
       open_track["{"] > 0 or \
       open_track["<"] > 0 and \
       line[-1] in [")", "]", "}", ">"]:
        print(line[-1])
"""
total_points = 0
all_close_points = []
for line in input_array:
    open_track = ""
    print("\n")
    print(line)
    corrupted = False
    for letter in line:
        # new opening
        if letter in ["(", "[", "{", "<"]:
            open_track += letter
        # close
        if letter == ")":
            if open_track[-1] == "(":
                # closed correctly
                open_track = open_track[:-1]
            else:
                print("corrupted", line)
                total_points += 3
                corrupted =True
                break
        if letter == "]":
            if open_track[-1] == "[":
                open_track = open_track[:-1]
            else:
                print("corrupted", line)
                total_points += 57
                corrupted =True
                break
        if letter == "}":
            if open_track[-1] == "{":
                open_track = open_track[:-1]
            else:
                print("corrupted", line)
                total_points += 1197
                corrupted =True
                break
        if letter == ">":
            if open_track[-1] == "<":
                open_track = open_track[:-1]
            else:
                print("corrupted", line)
                total_points += 25137
                corrupted =True
                break
    if not corrupted:
        print(open_track[::-1])
        # convert backwards
        backwards = ""
        for letter in open_track[::-1]:
            if letter == "(":
                backwards += ")"
            if letter == "[":
                backwards += "]"
            if letter == "{":
                backwards += "}"
            if letter == "<":
                backwards += ">"
        print(backwards)
        close_points = 0
        for letter in backwards:
            if letter == ")":
                close_points = close_points * 5 + 1
            if letter == "]":
                close_points = close_points * 5 + 2
            if letter == "}":
                close_points = close_points * 5 + 3
            if letter == ">":
                close_points = close_points * 5 + 4
        all_close_points.append(close_points)
    """
    # Check final letter
    final_letter = line[-1]
    #print("final_letter", final_letter)
    if final_letter in [")", "]", "}", ">"]:
        # closed so check if corrupted
        if final_letter == ")" and open_track[-1] != "(":
            print("corrupted", open_track)
        if final_letter == "]" and open_track[-1] != "[":
            print("corrupted", open_track)
        if final_letter == "}" and open_track[-1] != "{":
            print("corrupted", open_track)
        if final_letter == ">" and open_track[-1] != "<":
            print("corrupted", open_track)
    """
all_close_points.sort()
print(all_close_points)
print(all_close_points[int(len(all_close_points)/2 - .5)])
print(total_points)
        
