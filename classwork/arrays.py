# from numpy import *
# a = array(['a', 'b', 'c', 'd']) 
# print(a)



# from numpy import *
# a = array(['abc', 'bcd', 'cde', 'def'], dtype=str)
# print(a)



# from numpy import *
# a = array([1, 2, 3, 4, 5]) 
# print(a)
# #Create another array using array() method b = array(a)
# print(a)
# #Create another array by just copy c = a
# print(a)



# from numpy import *
# a = arange(2, 11, 2)
# print(a)


# from numpy import *
# a = zeros(5, int)
# print(a)
# b = ones(5) #Default datatype is float print(b)




# a = array([10, 20 30.5, -40])

# a = a + 5 #Adds 5 to each item of an array


# a1 = array([10, 20 30.5, -40])
# a2 = array([1, 2, 3, 4])
# a3 = a1 + a2 #Adds each item of a1 and a2



# from numpy import *
# a = array([1, 2, 3])
# b = array([3, 2, 3])
# c = a == b
# print(c)
# c = a > b
# print(c)
# c = a <= b
# print(c)




# from numpy import *
# a = array([1, 2, 3])
# b = array([3, 2, 3])
# c = a > b
# print(c)
# print("any(): ", any(c))
# print("all(): ", all(c))
# if (any(a > b)):
#     print("a contains one item greater than those of b")



# from numpy import *
# a = array([1, 2, 3])
# b = array([3, 2, 3])
# c = logical_and(a > 0, a < 4)
# print(c)





# from numpy import *
# a = array([1, 2, 3], int)
# c = where(a % 2 == 0, a, 0)
# print(c)




# from numpy import *
# a = array([1, 2, 0, -1, 0, 6], int) 
# c = nonzero(a)
# #Display the indices
# for i in c:
#     print(i)

# #Display the items
# print(a[c])





# from numpy import *
# a = arange(1, 6)
# b = a
# print(a)
# print(b)

# #Modify 0th Item
# b[0] = 99
# print(a)
# print(b)


# from numpy import *

# a = arange(1, 6)
# b = a.view() #Creates new array print(a)
# print(b)
# #Modify 0th Item 
# b[0]= 99
# print(a)
# print(b)




# a = array([[1, 2, 3],
# [4, 5, 6]])


# a = array([[[1, 2, 3],[4, 5, 6]]
# [[1, 1, 1], [1, 0, 1]]])



# a = array([1, 2, 3])
# print(a.ndim)


# a = array([[[1, 2, 3],[4, 5, 6]]
# [[1, 1, 1], [1, 0, 1]]]

# print(a.ndim)












