import numpy as np

input_array = np.loadtxt("input", dtype=str)
print(input_array)

gamma = ""
epsilon = ""
for index in range(12):
    zero_count = 0
    one_count = 0
    for binary in input_array:
        if int(binary[index]) == 0:
            zero_count += 1
        else:
            one_count += 1
    if zero_count > one_count:
        # zero more popular
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
# Convert to decimal
print(gamma, epsilon)
gamma_decimal = int(gamma, 2)
epsilon_decimal = int(epsilon, 2)
print("power: {}".format(gamma_decimal*epsilon_decimal))
