# Question
# 1 — Student Marks Analysis


# Consider the following tuple
# containing student records:


# students= (
#     ("S101", "Amit", 78, 85,91),
#     ("S102", "Neha", 92, 88,95),
#     ("S103", "Ravi", 65, 72,68),
#     ("S104", "Priya", 88, 91,84),
#     ("S105", "Karan", 55, 67,61)
# )


# Write a Python program using a function
# to:


# Calculate the total marks of each student.
# Display students whose total marks are greater than 250.
# Store their student IDs in a separate list.
# Display the student having the highest total marks without
# using max().



# students = (
#     ("S101", "Amit", 78, 85, 91),
#     ("S102", "Neha", 92, 88, 95),
#     ("S103", "Ravi", 65, 72, 68),
#     ("S104", "Priya", 88, 91, 84),
#     ("S105", "Karan", 55, 67, 61)
# )

# def calculate(students):
#     ids = []
#     highest = 0
#     highest_name = ""

#     for s in students:
#         total = s[2] + s[3] + s[4]

#         print(s[0], s[1], "Total =", total)

#         if total > 250:
#             ids.append(s[0])

#         if total > highest:
#             highest = total
#             highest_name = s[1]

#     print("Student IDs with total > 250:", ids)
#     print("Highest marks:", highest_name, highest)


# calculate(students)






# Question 2 — Product Inventory Analysis


# Consider the following tuple:

# products = (    ("P101", "Laptop", 55000, 8),    ("P102", "Mouse", 800, 25),    ("P103", "Keyboard", 1500, 12),    ("P104", "Monitor", 12000, 5),    ("P105", "Webcam", 2500, 18))
# #Product ID, Product Name, Price, Quantity



# Write a Python program using a to:
# Calculate the inventory value of each product using: 
# Inventory Value = Price × Quantity 
# Display products whose inventory value exceeds ₹20,000.
# Store their product IDs in a list. 
# Find the product having the min().


# products = (    ("P101", "Laptop", 55000, 8),    ("P102", "Mouse", 800, 25),    ("P103", "Keyboard", 1500, 12),    ("P104", "Monitor", 12000, 5),    ("P105", "Webcam", 2500, 18))

# def calculate (products):
#     inventory_value = 0
#     exceeds_20000 = []
#     min = 10000000000000
#     min_name = ""

#     for p in products:
#         inventory_value = p[2] * p[3]
#         print (p[0], p[1], "inventory value =" ,inventory_value )
#         if inventory_value > 20000:
#             exceeds_20000.append(p[0])
#         if inventory_value < min:
#             min = inventory_value
#             min_name = p[1]

#     print ("Product IDs with inventory value > 20000: ", exceeds_20000)
#     print ("The product having the min: ",min_name, min)

# calculate(products)




# Question 3 — Tuple Frequency and Position
# Consider:
# numbers = (4, 7, 4, 9, 7, 4, 2, 9, 7, 4)

# Write a Python program using a function  to: 
# -Find the frequency of a number entered by the user using the tuple function count().
# -Find its first position using index(). 
# -Determine whether the number is frequent or less
# frequent. 
# -Create a list containing all numbers whose frequency is greater than 2.
# Use loops and control structures.


numbers = (4, 7, 4, 9, 7, 4, 2, 9, 7, 4)
def count(numbers):
    count = 0
    for n in numbers:
        









