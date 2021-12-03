import numpy as np


def remove_data(arr, index, check):
    new_arr = []
    for a in arr:
        if int(a[index]) == check:
            new_arr.append(a)
    return np.array(new_arr)


oxegen_array = co2_array = np.loadtxt("input", dtype=str)
#oxegen_array = co2_array = np.loadtxt("example", dtype=str)

for index in range(12):
    zero_count = 0
    one_count = 0

    # oxegen
    if len(oxegen_array) != 1:
        for binary in oxegen_array:
            if int(binary[index]) == 0:
                zero_count += 1
            else:
                one_count += 1

        if zero_count > one_count:
            # zero more popular
            oxegen_array  =  remove_data(oxegen_array, index, 0)
        elif zero_count == one_count:
            oxegen_array  =  remove_data(oxegen_array, index, 1)
        else:
            oxegen_array  =  remove_data(oxegen_array, index, 1)

    
    # co2
    zero_count = 0
    one_count = 0
    if len(co2_array) != 1:
        for binary in co2_array:
            if int(binary[index]) == 0:
                zero_count += 1
            else:
                one_count += 1
        print(f"index {index:2d}     #0 {zero_count:3d}     #1 {one_count:3d}")
        for a in co2_array:
            print(f"   {a[:index]} {a[index]} {a[index+1:]}")
        if zero_count > one_count:
            # zero more popular
            co2_array  =  remove_data(co2_array, index, 1)
        elif zero_count == one_count:
            co2_array  =  remove_data(co2_array, index, 0)
        else:
            co2_array  =  remove_data(co2_array, index, 0)
    #elif len(co2_array) == 2:
    #print(index, co2_array)
# Convert to decimal
print(len(oxegen_array), len(co2_array))
oxegen = oxegen_array[0]
co2 = co2_array[0]
print(oxegen, co2)
oxegen_decimal = int(oxegen, 2)
co2_decimal = int(co2, 2)
print("power: {}".format(oxegen_decimal*co2_decimal))
