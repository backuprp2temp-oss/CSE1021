# x = 10
# y = 5

# x = x ^ y;
# y = x ^ y;
# x = x ^ y

# print ("After Swapping: x = ", x, "y = ", y )




# program to count digits in an integer:


# Method 1:

# Iterative python program to count
# number of digits in a number

# def countDigit(n):
#     count = 0
#     while n != 0:
#         n //= 10
#         count += 1

#     # Driver Code
#     n = 345289467
#     print ("Number of digits: % d" % (countDigit(n)))




# Method 2:

# Recursive python program to count
# number of digits in a number

# def countDigit(n):
#     if n == 0:
#         return 0
#     return 1 + countDigit (n // 10)

# # Driver Code

# n = 345289467
# print ("Number of digits: % d" % (countDigit(n)))





# Method 3:

# Log based Python program to count number of
# digits in a number

# function to import ceil and log
# import math

# def countDigit(n):
#     return math.floor(math.log10(n) + 1)

# # Driver Code
# n = 345289467
# print("Number of digits : %d" % (countDigit(n)))





# Method 4:

# Python3 implementation of the approach
# def count_digits(n):
#     n = str(n)
#     return len(n)

#  Driver code
# n = 456533457776
# print(count_digits(n))




# Calculate the sum and average of first n natural numbers:


# n = 10
# sum = 0
# for num in range (0, n+1, 1):
#     sum += num
# print ("SUM of first ",n,"numbers is: ", sum)




# Write a python program to find sum and average of n numbers inputed by the user.

# sum = 0
# count = 0
# print ("Do you want to enter the game? Enter start to start and quit to quit: ")
# choice = input("Please enter your choice: ").lower()

# if choice == "start":
#     while True:
#         n = int(input ("Enter a number: "))
#         sum += n
#         count += 1
#         average = sum / count
#         print ("The sum is: ", sum)
#         print ("The average is: ", average)

# elif choice == "quit":
#     print ("Thanks for playing, see you soon!")

# else:
#     print ("Invalid Input")




# Reverse a number:

num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)










    


