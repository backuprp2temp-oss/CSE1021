# import numpy as np
# a = np.array([4, 6, 2, 9])

# Write a program to take one array as input having 15 elements 
# print the array withour duplicate element
# print fifth largest element
# Reverse the element without violating the order
# Sort the elements without using the sort function. 


# Take an array of 15 elements
# Take an array of 15 elements
arr = []

print("Enter 15 elements:")
for i in range(15):
    element = int(input("Enter element: "))
    arr.append(element)

# 1. Print array without duplicate elements
unique = []

for element in arr:
    if element not in unique:
        unique.append(element)

print("\nArray without duplicate elements:", unique)

# 2. Find the fifth largest element
temp = unique.copy()

# Sort in descending order without using sort()
for i in range(len(temp)):
    for j in range(i + 1, len(temp)):
        if temp[i] < temp[j]:
            temp[i], temp[j] = temp[j], temp[i]

if len(temp) >= 5:
    print("Fifth largest element:", temp[4])
else:
    print("There are less than 5 unique elements.")

# 3. Reverse the elements without changing their order
reverse = []

for i in range(len(arr) - 1, -1, -1):
    reverse.append(arr[i])

print("Reversed array:", reverse)

# 4. Sort the elements without using sort()
sorted_arr = arr.copy()

for i in range(len(sorted_arr)):
    for j in range(i + 1, len(sorted_arr)):
        if sorted_arr[i] > sorted_arr[j]:
            sorted_arr[i], sorted_arr[j] = sorted_arr[j], sorted_arr[i]

print("Sorted array:", sorted_arr)








