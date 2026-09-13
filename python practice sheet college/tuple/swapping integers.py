# Accept two integer values from the user 
a = int(input("Enter the first integer: ")) 
b = int(input("Enter the second integer: ")) 
print("Before swapping:") 
print("a =", a) 
print("b =", b) 
# Tuple assignment using a third variable 
temp = a 
a, b = b, temp 
print("After swapping:") 
print("a =", a) 
print("b =", b) 