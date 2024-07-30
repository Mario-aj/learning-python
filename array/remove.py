from array import *

arr1 = array('i', [1,2,3,4,5,6])

print(arr1)

arr1.remove(3)
print(arr1)

# Removing the element

def remove(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      arr[i] = arr[i+1]
      i = i + 1
    else:
      arr[i] = arr[i]

remove(arr1, 2)
print(arr1)