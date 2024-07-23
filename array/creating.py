import array as Array
import numpy as np

my_array = Array.array('i')
print(my_array);

my_array1 = Array.array('i', [1, 2,3 ,4])
print(my_array1)
print("fisrt element: ", my_array1[0])

my_array1.append(5)
print("last element: ", my_array1[len(my_array1) - 1])

# Creating array using numpy lib

np_array = np.array([], dtype=int)
print("\n", np_array)
