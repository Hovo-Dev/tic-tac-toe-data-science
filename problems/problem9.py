import numpy as np

original_array = np.arange(1, 101).reshape(10, 10)

resized_1 = np.resize(original_array, (2, 5, 10, 1))
# resized_2 = np.resize(original_array, (50, 2))
# resized_3 = np.resize(original_array, (4, 25))
# resized_4 = np.resize(original_array, (25, 4))
# resized_5 = np.resize(original_array, (100, 1))
# resized_6 = np.resize(original_array, (1, 100))
# resized_7 = np.resize(original_array, (5, 20))
# resized_8 = np.resize(original_array, (20, 5))


print("Original 10x10 Array:")
print(original_array)
print("1")
print(resized_1)
# print("2")
# print(resized_2)
# print("3")
# print(resized_3)
# print("4")
# print(resized_4)
# print("5")
# print(resized_5)
# print("6")
# print(resized_6)
# print("7")
# print(resized_7)
# print("8")
# print(resized_8)