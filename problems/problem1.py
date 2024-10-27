import numpy as np

random_array = np.random.randint(0, 1000, 100)
indices_ending_with_6 = [i for i, num in enumerate(random_array) if str(num).endswith('6')]
indices_array = np.array(indices_ending_with_6)

print("Array:")
print(random_array)
print("Elements's index Ending with 6:")
print(indices_array)
