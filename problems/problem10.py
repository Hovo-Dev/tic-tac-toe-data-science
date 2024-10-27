import numpy as np

array1 = np.random.uniform(0, 20, (10, 10))
array2 = np.random.uniform(0, 20, (10, 10))

result = array1 / array2
non_nan_non_inf_elements = result[(~np.isnan(result)) & (~np.isinf(result))]

print(result)
print("--------------------------------------")
print(non_nan_non_inf_elements)
