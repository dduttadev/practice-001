from array import *

arr1 = array('i',[23,56,34,86,2,87,17])

print(type(arr1))
print(arr1)
print(list(arr1))

for n in arr1:
    print(n)

arr1.reverse()
print(arr1)

#arr2 = array('i',arr1.tolist())
arr2 = array(arr1.typecode, (n for n in arr1))
print(arr2)

print(id(arr1))
print(id(arr2))