students = (
    ("S101", "Amit", 78, 85, 91),
    ("S102", "Neha", 92, 88, 95),
    ("S103", "Ravi", 65, 72, 68),
    ("S104", "Priya", 88, 91, 84),
    ("S105", "Karan", 55, 67, 61)
)

def studentdetails(students):
    ids = []
    highest_total = 0
    topper = ""
    
    print("Total Marks of Each Student:")
    for s in students:
        total = s[2] + s[3] + s[4]
        print(s[1], ":", total)

    print("\nStudents with Total Marks > 250:")
    for s in students:
        total = s[2] + s[3] + s[4]
        if total > 250:
            print(s[1], ":", total)
            ids.append(s[0])
        if total > highest_total:
            highest_total = total
            topper = s[1]

    print("\nStudent IDs:", ids)
    print("\nHighest Total Marks:", topper, "-", highest_total)

studentdetails(students)

products = (
    ("P101", "Laptop", 55000, 8),
    ("P102", "Mouse", 800, 25),
    ("P103", "Keyboard", 1500, 12),
    ("P104", "Monitor", 12000, 5),
    ("P105", "Webcam", 2500, 18)
)

def inventory_analysis(products):
    ids = []
    lowest_value = 10000000000
    lowest_product = ""

    print("Inventory Value of Each Product:")
    for p in products:
        value = p[2] * p[3]
        print(p[1], ":", value)

    print("\nProducts with Inventory Value > ₹20,000:")
    for p in products:
        value = p[2] * p[3]
        if value > 20000:
            ids.append(p[0])
            print(p[1], ":", value)
        if value < lowest_value:
            lowest_value = value
            lowest_product = p[1]

    print("\nProduct IDs:", ids)
    print("\nProduct with lowest Inventory Value:", lowest_product, "-", lowest_value)

inventory_analysis(products)

#swapping two numbers without using variable
a = 10
b = 20
print(f"Before swapping a = {a}") 
print(f"Before swapping b = {b}") 
a = a + b
b = a - b
a = a - b
print(f"After swapping a = {a}") 
print(f"After swapping b = {b}")

#swapping two number without using arithemetic operator
a = 10
b = 20
print(f"Before swapping a = {a}") 
print(f"Before swapping b = {b}")
a = a ^ b
b = a ^ b
a = a ^ b
print(f"After swapping a = {a}")
print(f"After swapping b = {b}")

#counting digits in a number
def cd(s):
    count = 0
    while s != 0:
        s //= 10 
        count += 1
    return count

a = int(input("Enter the number: "))
print(f"Total digits are: {cd(a)}")

import math
def cdm(s):
    return math.floor(math.log10(s)+1)

a = int(input("Enter the number: "))
print(cdm(a))

def cds(s):
    s = str(s)
    return len(s)

a = int(input("Enter the number: "))
print(cds(a))

# write an program to find sum and average of n numbers inputed by the user
def s():
    n = int(input(("enter the number: ")))
    if n == 0:
        return 0 , 0
    total , count = s()
    return n + total, 1 + count

s , c = s()
print(f" sum is {s} and avg is {s/c}")

#reverse a number
def r(n):
    re = 0
    while n != 0:
        c = n % 10
        re = re * 10 + c
        n//=10
    return re

a = int(input("Enter the number: "))
print(f"The reverse is {r(a)}")