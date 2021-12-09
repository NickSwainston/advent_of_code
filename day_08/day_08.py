import numpy as np

input_array = np.loadtxt("example", dtype=str)
input_array = np.loadtxt("input", dtype=str)
#input_array = np.loadtxt("test", dtype=str)

 
"""
 0 
1 2
 3
4 5
 6
"""

def sort_string(string):
    order = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    sorted_string = ''
    for o in order:
        if o in string:
            sorted_string += o
    return sorted_string


total = 0
easy_dig_count = 0
one = four = seven = eight = None
#print(input_array)
for row in input_array:
    ten_digits = row[:10]
    answer_digits = row[11:]
    #print(ten_digits)
    #print(answer_digits)
    sorted_strings = []
    for dig in ten_digits:
        sorted_strings.append(sort_string(dig))
    sorted_answer = []
    for dig in answer_digits:
        sorted_answer.append(sort_string(dig))
    # Find digits
    #print("ten_digits", ten_digits)
    two_three_five = []
    zero_six_nine = []
    for dig in sorted_strings:
        #print(dig, len(dig))
        if len(dig) == 2:
            one = dig
        elif len(dig) == 3:
            seven = dig
        elif len(dig) == 4:
            four = dig
        elif len(dig) == 5:
            two_three_five.append(dig)
        elif len(dig) == 6:
            zero_six_nine.append(dig)
        elif len(dig) == 7:
            eight = dig
    print("\none", one, "four", four, "seven", seven, "eight", eight)

    #print("answerdigits", answer_digits)
    for ans in sorted_answer:
        if one == ans:
            #print("one", one)
            easy_dig_count += 1
        if four == ans:
            #print("four", four)
            easy_dig_count += 1
        if seven == ans:
            #print("seven", seven)
            easy_dig_count += 1
        if eight == ans:
            #print("eight", eight)
            easy_dig_count += 1
    
    # segment 0
    seg_0 = seven
    for letter in one:
        seg_0 = seg_0.replace(letter, '')

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # sefment 2 3 4 
    seg_2_3_4 = []
    for dig in zero_six_nine:
        for klet in alphabet:
            if klet not in [char for char in dig]:
                seg_2_3_4.append(klet)
    #print(seg_2_3_4)

    seg_2_5 = [char for char in one]
    for seg in seg_2_5:
        if seg in seg_2_3_4:
            seg_2 = seg
        else:
            seg_5 = seg
    seg_2_3_4.remove(seg_2)
    seg_3_4 = seg_2_3_4
    #print(seg_0, seg_2, seg_5)
    #print(seg_3_4)

    # segment 
    #print(two_three_five)
    for dig in two_three_five:
        if seg_2 not in [char for char in dig]:
            five = dig
        if seg_5 not in [char for char in dig]:
            two = dig
    #print(two_three_five)
    two_three_five.remove(five)
    two_three_five.remove(two)
    three = two_three_five[0]
    print("two", two, "three", three, "five", five)

    for seg in seg_3_4:
        if seg in [char for char in three]:
            seg_3 = seg
        else:
            seg_4 = seg

    for dig in zero_six_nine:
        if seg_3 in [char for char in dig] and \
           seg_4 in [char for char in dig]:
            six = dig
        elif seg_3 not in [char for char in dig] and \
             seg_4 in [char for char in dig]:
            zero = dig
        else:
            nine = dig
    print("zero", zero, "six", six, "nine", nine)

    final_str = ''
    for astr in sorted_answer:
        for dig, num in [(zero, 0), (one, 1), (two, 2),
                         (three, 3), (four, 4), (five, 5),
                         (six, 6), (seven, 7), (eight, 8), (nine, 9)]:
            if dig == astr:
                final_str += str(num)
    print(final_str)
    total += int(final_str)

print(easy_dig_count)
print(total)
