# n = 5

# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")
#     print()


# n = 5

# for i in range(n, 0, -1):
#     for j in range(i):
#         print("$", end="")
#     print()


# n = 5

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(i):
#         print("#", end="")
#     print()



# n = 5

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
    
#     for j in range(2 * i - 1):
#         print("*", end="")
    
#     print()


# n = 5

# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")
    
#     for j in range(2 * i - 1):
#         print("*", end="")
    
#     print()


# n = 5

# # Upper half
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
    
#     for j in range(2 * i - 1):
#         print("*", end="")
    
#     print()

# # Lower half
# for i in range(n - 1, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")
    
#     for j in range(2 * i - 1):
#         print("*", end="")
    
#     print()



# n = 5

# # Upper half
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
    
#     for j in range(2 * i - 1):
#         if j == 0 or j == 2 * i - 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
    
#     print()

# # Lower half
# for i in range(n - 1, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")
    
#     for j in range(2 * i - 1):
#         if j == 0 or j == 2 * i - 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
    
#     print()



# n = 5

# # Upper half
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")
    
#     for j in range(2 * (n - i)):
#         print(" ", end="")
    
#     for j in range(i):
#         print("*", end="")
    
#     print()

# # Lower half
# for i in range(n - 1, 0, -1):
#     for j in range(i):
#         print("*", end="")
    
#     for j in range(2 * (n - i)):
#         print(" ", end="")
    
#     for j in range(i):
#         print("*", end="")
    
#     print()


# n = 7

# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("#", end="")
#         else:
#             print(" ", end="")
    
#     print()



# n = 7

# for i in range(n):
#     for j in range(n):
#         if j == i or j == n - i - 1:
#             print("$", end="")
#         else:
#             print(" ", end="")
    
#     print()



# n = 5

# # Upper half
# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")
    
#     for j in range(2 * i - 1):
#         print("*", end="")
    
#     print()

# # Lower half
# for i in range(2, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
    
#     for j in range(2 * i - 1):
#         print("*", end="")
    
#     print()



# n = 5

# for i in range(n, 0, -1):
#     print(" " * (n - i), end="")
#     print("#" * (2 * i - 1))

# for i in range(2, n + 1):
#     print(" " * (n - i), end="")
#     print("#" * (2 * i - 1))



# n = 5

# for i in range(1, n + 1):
#     print(" " * (n - i), end="")

#     if i == 1:
#         print("$")
#     elif i == n:
#         print("$" * (2 * i - 1))
#     else:
#         print("$" + " " * (2 * i - 3) + "$")




# n = 4

# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     print("#" * (2 * i - 1))

# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), end="")
#     print("#" * (2 * i - 1))

# print()

# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     print("#" * (2 * i - 1))

# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), end="")
#     print("#" * (2 * i - 1))




# n = 5

# for i in range(1, n + 1):
#     print("*" * i)

# for i in range(n - 1, 0, -1):
#     print("*" * i)



# n = 5

# for i in range(1, n + 1):
#     print(" " * (n - i), end="")

#     for j in range(i):
#         if j == 0:
#             print("*", end="")
#         elif j % 2 == 1:
#             print("$", end="")
#         else:
#             print("#", end="")

#     print()



# print(" **   **")
# print("**** ****")
# print("*********")
# print(" ********")
# print("  ******")
# print("   ****")
# print("    **")



# print("*   *   *")
# print("** ** **")
# print("*******")
# print("*******")
# print("*******")



# n = 5

# for i in range(1, n + 1):
#     print(" " * (n - i), end="")

#     for j in range(i):
#         if j % 2 == 0:
#             print("$", end="")
#         else:
#             print("#", end="")

#     print()




n = 5

# Upper part
for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(i):
        if j % 2 == 0:
            print("*", end="")
        else:
            print("$#", end="")

    print()

# Lower part
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")

    for j in range(i):
        if j % 2 == 0:
            print("*", end="")
        else:
            print("$#", end="")

    print()

print()

# Bottom section
print("   $$$")
print("  $###$")
print(" $#####$")
print("$#######$")
print("$$$$$$$$$$$")



