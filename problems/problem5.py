import numpy as np

original_array = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])

reversed_array = original_array[::-1, :]

print("Original Array:")
print(original_array)
print("\nReversed Array:")
print(reversed_array)