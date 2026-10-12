import numpy as np
from array import *

import array
a = array("i",[2,3,4])
print(type(a))
print(a)

import array
a = array.array("i", [1, 2, 3, 4])
print("Items are: ")
for i in a:
    print(i)


from array import *
a = array("i", [1, 2, 3, 4])
print("Items are: ")
for i in a:
    print(i)


from array import *
a = array('u', ['a', 'b', 'c', 'd']) 
print("Items are: ")
for ch in a:
    print(ch)


from array import*
a = array('i', [1, 2, 3, 4])
b = array(a.typecode, (i for i in a))
print("Items are: ")
for i in b:
    print(i)


c = array(a.typecode, (i * 3 for i in a))
print("Items are: ")
for i in c:
    print(i)


from array import *
a = array('i', [1, 2, 3, 4])
n = len(a)
range(n):
print(a[i], end=' ')


from array import *
a = array('i', [1, 2, 3, 4])
n = len(a)
i = 0
while i < n:
    print(a[i], end=' ') 
    i += 1


from array import *
a = array('i', [1, 2, 3, 4])
for i in a[2: 5]:
    print(i)

from array import *
import numpy as
a = np.array([10,20,30,40,50])
print(a)

print(a[0])
print(a[1])
print(a[2])
print(a[2:4])
print(a[:3])
print(a[:3])

for i in a:
    print(i*10)

b = np.arange(1,10,2)
print(b)

z = np.zeros(5)
print(z)

o = np.ones(5)
print(o)

print(a + o)
print(a - o)
print(a * o)

print(np.sqrt(a))
print(np.square(a))
print(np.sum(a))
print(np.mean(a))

b = a
print(a == b)
print(a != b)
b[0] = 30
print(b)
print(a)

c = a.copy()
c[0] = 10
print(c)
print(a)

a[0] = 10
a = np.array([[1,2,3],[10,20,30],[100,200,300],[1000,2000,3000]])
print(a)
print(a[1,2])
print(a[:,1])
print(a[0:2, 1:3])

print(a.ndim)
print(a.shape)
print(a.size)

a = np.array([10,20,30], dtype = np.int32)
print(a.itemsize)
print(a.nbytes)

c = np.array([10,20,30,40,50,60])
b = c.reshape(2,3)
print(b)

d = np.eye(5)
print(d)

np.matmul()

# write a program to take one array as input having 15 elements 1. print the array without duplicate elemets 2. print 5th largest element 3. reverse the elements wihtout violating the order 4. sort the elemets without using sort fucntion 

# Take an array of 15 elements
n = []

print("Enter 15 elements:")
for i in range(15):
    n.append(int(input()))

# 1. Print array without duplicate elements
unique = []

for element in n:
    if element not in unique:
        unique.append(element)

print("\nArray without duplicates:", unique)


# 2. Print 5th largest element
temp = n.copy()

# Sort in descending order without sort()
for i in range(len(temp)):
    for j in range(i + 1, len(temp)):
        if temp[i] < temp[j]:
            temp[i], temp[j] = temp[j], temp[i]

print("5th largest element:", temp[4])


# 3. Reverse the elements without violating the order
reverse = []

for i in range(len(n) - 1, -1, -1):
    reverse.append(n[i])

print("Reversed array:", reverse)


# 4. Sort the elements without using sort()
sorted_arr = n.copy()

for i in range(len(sorted_arr)):
    for j in range(0, len(sorted_arr) - i - 1):
        if sorted_arr[j] > sorted_arr[j + 1]:
            sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]

print("Sorted array:", sorted_arr)

import numpy as np
a = np.array([1, 2, 3])
b = np.array([3, 2, 3])
c = np.logical_and(a > 0, a < 4) 
print(c)
