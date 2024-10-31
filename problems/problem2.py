# Create 2 2dimensional array and compute

# 1) Elementwise product
import numpy as np

array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

elementwise_product = array1 * array2

print('Element_Wise:: ', elementwise_product)

# 2) Matrix Product
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

matrix_product = array1 @ array2

print('Matrix:: ', matrix_product)
