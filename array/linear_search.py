from array import *

my_array = array('i', [1,2,3,4,5,6,])

def linear_search(arr, targe):
  for i in range(len(arr)):
    if arr[i] == targe:
      return i
    
  return -1


print(linear_search(my_array, 9)) # -1
print(linear_search(my_array, 5)) # 4