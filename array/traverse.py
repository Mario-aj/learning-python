from array import *

arr1 = array('i', [1,2,3,4,5,6])

def traverse(arr):
  for i in arr:
    print(i)

traverse(arr1)
# Time and space for the traverse function
# Time complexity: O(n)
# Space complexity: O(1)