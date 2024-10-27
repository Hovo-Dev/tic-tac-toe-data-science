import numpy as np

input_str1 = input("Enter the first array: ")
array1 = np.array([int(x) for x in input_str1.split()])

input_str2 = input("Enter the second array: ")
array2 = np.array([int(x) for x in input_str2.split()])

resulting_array = np.vstack((array1, array2))

print(resulting_array)