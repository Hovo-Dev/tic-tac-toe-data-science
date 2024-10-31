import numpy as np

# Create 3 arrays fill 0 in first one, fill 1 in second one and fill 9 in third one.

array_zeros = np.zeros(10, dtype=int)
array_ones = np.ones(10, dtype=int)
array_nines = np.full(10, 9, dtype=int)

array_2d = np.vstack((array_zeros, array_ones, array_nines))

print('2D Array:: ', array_2d)
