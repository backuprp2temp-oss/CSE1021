# continue skips the current iteration and moves to the next iteration.


# questions: 
# 1. take a list containing few zeroes. print all the numbers of the list except zero.
# 2. print 5-1 except 3
# 3. take a list containing positive and negative numbers, print all the numbers in the list until you're getting a negative number.
# 4. create a list having 6 numbers, search a number in that list, when it is found display "number is found". it should display number is found even though the number is present multiple times in the list (along with the number of occurence of that number in the list)

# answer 1:


# list = [0,1,17,23,68,459,0,67,0]
# for i in list:
#     if i == 0:
#         continue
#     print (i)


# answer 2:

# for i in range (5,0,-1):
#     if i == 3:
#         continue
#     print(i)
    

# answer 3:

# list = [-2,-13,69,67,435]
# for i in list:
#     if i < 0:
#         break
#     print (i)


# asnwer 4:

# list = [1,2,3,2,5,6]
# count = 0
# for i in list:
#     if i == 4:
#         count = count + 1
#         break
# print (f"Number {i} is found {count} times.")

# write a program that repeatedly accepts numbers and calculates their sum. Ignore negative numbers and stop when 0 is entered.
# sum = 0
# while True:
#     n = float(input("Enter your number:"))
#     if n < 0:
#         continue
#     if n == 0:
#         break
#     sum = sum + n
#     print (sum)

# for i in range (1,21):
#     if i % 3 == 0:
#         continue 
#     print (i)



# str = input ("Enter your string:")
# vowel_count= 0
# for i in str:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u"  :
#         vowel_count += 1
# print (vowel_count)



# n = int(input("Enter your number:"))
# for i in range (1,11):
#     if i == 4:
#         continue
#     print (f" {n} * {i} = {n*i}")




# balance = 1000000
# n = int(input("Enter 1 to check balance, 2 to desposit money, 3 to withdraw money, 4 to exit:"))
# if n == 1:
#     print (f"Your account balance is:{balance} rs")
# elif n == 2:
#     deposit = float(input("Enter the amount you want to deposit:"))
#     balance = balance + deposit
#     print (f"You've successfully deposied {deposit} rs ")
#     print (f"Your current balance is:{balance} rs")
# elif n == 3:
#     withdraw = float(input("Enter the amount you want to withdraw:"))
#     if withdraw <= balance:
#         balance = balance - withdraw
#         print (f"You've successfully withdrawn {withdraw} rs ")
#         print (f"The remaining balance is:{balance} rs")
#     else:
#         print ("Insufficient balance")
# elif n == 4:
#     print ("Goodbye! see you again!")
# else:
#     print ("Invalid input")


# Rectangle of stars:
# output: * * * *
#         * * * * 
#         * * * * 

# for i in range (3):
#     for j in range (4):
#         print ("*", end="")
#     print()


# Number pattern:
# output:
# 1 2 3
# 1 2 3 
# 1 2 3

# for i in range (1,4):
#     for j in range (1,4):
#         print ( j , end = "")
#     print()


# Multipication Tables:
# output:
# 1 2 3
# 2 4 6
# 3 6 9


# for i in range (1,4):
#     for j in range (1,4):
#         print ( i * j, end = "")
#     print()


# Triangle pattern
# output:
# *
# * *
# * * *
# * * * *














    
