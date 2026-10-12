# Q1. Display the value and data type of different values
a = 25
b = 12.5
c = "Python"
d = True
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# Q2. Store student information in variables
name = "Rahul"
age = 20
marks = 85.5
print("Name:", name)
print("Age:", age)
print("Marks:", marks)

# Q3. Calculate the area of a rectangle
length = 12
breadth = 8
area = length * breadth
print("Area =", area)

# Q4. Calculate simple interest
principal = 10000
rate = 5
time = 2
si = (principal * rate * time) / 100
print("Simple Interest =", si)

# Q5. Convert Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9 / 5) + 32
print("Fahrenheit =", fahrenheit)

# Q6. Calculate the average of three numbers
a = 10
b = 20
c = 30
average = (a + b + c) / 3
print("Average =", average)

# Q7. Swap two variables
a = 10
b = 20
a, b = b, a
print("a =", a)
print("b =", b)

# Q8. Calculate total and percentage of five subjects
m1 = 78
m2 = 85
m3 = 92
m4 = 88
m5 = 80
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5
print("Total =", total)
print("Percentage =", percentage)

# Q9. Calculate the perimeter and area of a circle
radius = 7
pi = 3.14159
area = pi * radius ** 2
perimeter = 2 * pi * radius
print("Area =", area)
print("Perimeter =", perimeter)

# Q10. Convert seconds into hours, minutes and seconds
total_seconds = 7384
hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60
print(hours, "hours", minutes, "minutes", seconds, "seconds")

# 2. STATEMENTS, ARITHMETIC & OPERATOR PRECEDENCE


# Q11. Predict the result using operator precedence
result = 10 + 5 * 2
print(result)

# Q12. Evaluate an expression involving brackets
result = (10 + 5) * 2
print(result)

# Q13. Evaluate a mixed arithmetic expression
result = 20 - 4 * 3 + 10 / 2
print(result)

# Q14. Compare two expressions
a = 10 + 5 * 2
b = (10 + 5) * 2
print(a)
print(b)

# Q15. Calculate a shopping bill
price = 500
quantity = 3
discount = 10
total = price * quantity
discount_amount = total * discount / 100
final_amount = total - discount_amount
print("Final Amount =", final_amount)

# Q16. Calculate salary after deduction
salary = 50000
tax = 10
insurance = 2000
tax_amount = salary * tax / 100
net_salary = salary - tax_amount - insurance
print("Net Salary =", net_salary)

# Q17. Demonstrate floor division and modulus
a = 17
b = 5
print("Division =", a / b)
print("Floor Division =", a // b)
print("Remainder =", a % b)

# Q18. Calculate the last digit of a number
number = 45678
last_digit = number % 10
print("Last digit =", last_digit)

# Q19. Calculate square and cube
number = 6
square = number ** 2
cube = number ** 3
print("Square =", square)
print("Cube =", cube)

# Q20. Evaluate a complex expression
result = 5 + 2 * 3 ** 2 - 8 / 4
print(result)


# 3. LISTS

# Q21. Create and display a list
marks = [78, 85, 92, 67, 88]
print(marks)

# Q22. Find the length of a list
numbers = [10, 20, 30, 40, 50]
print("Number of elements =", len(numbers))

# Q23. Find the sum and average of list elements
marks = [70, 80, 90, 60, 85]
total = sum(marks)
average = total / len(marks)
print("Total =", total)
print("Average =", average)

# Q24. Find the largest and smallest element
numbers = [45, 12, 78, 34, 90, 23]
print("Largest =", max(numbers))
print("Smallest =", min(numbers))

# Q25. Access specific elements from a list
cities = ["Delhi", "Mumbai", "Bhopal", "Indore", "Pune"]
print(cities[0])
print(cities[2])
print(cities[-1])

# Q26. Add elements to a list
numbers = [10, 20, 30]
numbers.append(40)
numbers.insert(1, 15)
print(numbers)

# Q27. Remove an element from a list
numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
print(numbers)

# Q28. Reverse a list
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)

# Q29. Sort a list
marks = [78, 45, 92, 67, 88]
marks.sort()
print(marks)

# Q30. Find the second-largest number
numbers = [45, 12, 78, 34, 90, 23]
numbers.sort()
print("Second largest =", numbers[-2])


# 4. TUPLES

# Q31. Create and access a tuple
student = ("Rahul", 21, 85)
print(student[0])
print(student[1])
print(student[2])

# Q32. Find the length of a tuple
numbers = (10, 20, 30, 40, 50)
print("Length =", len(numbers))

# Q33. Find maximum and minimum in a tuple
numbers = (45, 12, 78, 34, 90)
print("Maximum =", max(numbers))
print("Minimum =", min(numbers))

# Q34. Count occurrences in a tuple
numbers = (10, 20, 10, 30, 10, 40)
print(numbers.count(10))

# Q35. Unpack a tuple
student = ("Amit", 21, "CSE")
name, age, branch = student
print(name)
print(age)
print(branch)


# 5. SETS

# Q36. Create a set and remove duplicate values
numbers = {10, 20, 10, 30, 20, 40}
print(numbers)

# Q37. Add and remove elements from a set
numbers = {10, 20, 30}
numbers.add(40)
numbers.remove(20)
print(numbers)

# Q38. Find union of two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)

# Q39. Find intersection of two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A & B)

# Q40. Find elements present in one set but not another
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A - B)


# 6. DICTIONARIES

# Q41. Create and access a dictionary
student = {
    "name": "Rahul",
    "age": 21,
    "marks": 85
}
print(student["name"])
print(student["marks"])

# Q42. Add and modify dictionary values
student = {
    "name": "Rahul",
    "age": 21
}
student["marks"] = 85
student["age"] = 22
print(student)

# Q43. Find the number of items in a dictionary
student = {
    "name": "Rahul",
    "age": 21,
    "branch": "CSE",
    "marks": 85
}
print(len(student))

# Q44. Display all keys and values
student = {
    "name": "Rahul",
    "age": 21,
    "marks": 85
}
print(student.keys())
print(student.values())

# Q45. Calculate total marks from a dictionary
marks = {
    "Python": 85,
    "Maths": 78,
    "AI": 90,
    "DBMS": 82
}
total = sum(marks.values())
print("Total =", total)


# 7. SOME MORE PROBLEMS

# Q46. Find common students in two classes
class_a = {"Amit", "Rahul", "Priya", "Neha"}
class_b = {"Priya", "Neha", "Karan", "Ravi"}
common = class_a & class_b
print("Common students:", common)

# Q47. Remove duplicate marks from a list
marks = [85, 90, 85, 78, 90, 88, 78]
unique_marks = list(set(marks))
print(unique_marks)

# Q48. Create a dictionary from two lists
names = ["Amit", "Rahul", "Priya"]
marks = [85, 90, 88]
students = dict(zip(names, marks))
print(students)

# Q49. Find the student with the highest marks
marks = {
    "Amit": 85,
    "Rahul": 92,
    "Priya": 88,
    "Neha": 95
}
topper = max(marks, key=marks.get)
print("Topper:", topper)
print("Marks:", marks[topper])

# Q50. Calculate the final bill using a list and operator precedence
prices = [500, 300, 200]
quantity = [2, 3, 1]
discount = 10
tax = 5
subtotal = prices[0] * quantity[0] + prices[1] * quantity[1] + prices[2] * quantity[2]
discount_amount = subtotal * discount / 100
amount_after_discount = subtotal - discount_amount
tax_amount = amount_after_discount * tax / 100
final_amount = amount_after_discount + tax_amount
print("Subtotal =", subtotal)
print("Discount =", discount_amount)
print("Tax =", tax_amount)
print("Final Amount =", final_amount)

# Program 1: Write a program to print "Hello, World!" on the screen.
print("Hello, World!")


# Program 2: Write a program to read a person's name from the user and greet them.
# Sample input: Riya
name = input("Enter your name: ")
print("Hello,", name)


# Program 3: Write a program to read two integers from the user and print their sum.
# Sample input: 12, 30
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)


# Program 4: Write a program to demonstrate the sep and end parameters of print().
print("Python", "is", "fun", sep="-")
print("Hello", end=" ")
print("World")


# Program 5: Write a program to display a name and age in a sentence using an f-string.
name = "Aman"
age = 20
print(f"My name is {name} and I am {age} years old.")


# Program 6: Write a program to read two integers on a single line, then print them and their product.
# Sample input: 6 7
x, y = map(int, input("Enter two numbers: ").split())
print("x =", x, "y =", y)
print("Product =", x * y)


# Program 7: Write a program to read the radius of a circle and find its area.
# Sample input: 5
r = float(input("Enter radius: "))
area = 3.14159 * r * r
print(f"Area of circle = {area:.2f}")


# Program 8: Write a program to display formatted output using format() and % formatting.
print("{} scored {} marks in {}".format("Amit", 92, "Maths"))
print("%s is %d years old" % ("Neha", 19))


# Program 9: Write a program to convert a temperature from Celsius to Fahrenheit.
# Sample input: 37
c = float(input("Enter temperature in Celsius: "))
f = c * 9 / 5 + 32
print(f"{c}°C = {f:.1f}°F")


# Program 10: Write a program to calculate simple interest from principal, rate and time.
# Sample input: 5000, 8, 2
p = float(input("Principal: "))
r = float(input("Rate (%): "))
t = float(input("Time (years): "))
si = p * r * t / 100
print("Simple Interest =", si)

# Program 1: Write a program to print "Hello, World!" on the screen.
print("Hello, World!")


# Program 2: Write a program to read a person's name from the user and greet them.
# Sample input: Riya
name = input("Enter your name: ")
print("Hello,", name)


# Program 3: Write a program to read two integers from the user and print their sum.
# Sample input: 12, 30
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)


# Program 4: Write a program to demonstrate the sep and end parameters of print().
print("Python", "is", "fun", sep="-")
print("Hello", end=" ")
print("World")


# Program 5: Write a program to display a name and age in a sentence using an f-string.
name = "Aman"
age = 20
print(f"My name is {name} and I am {age} years old.")


# Program 6: Write a program to read two integers on a single line, then print them and their product.
# Sample input: 6 7
x, y = map(int, input("Enter two numbers: ").split())
print("x =", x, "y =", y)
print("Product =", x * y)


# Program 7: Write a program to read the radius of a circle and find its area.
# Sample input: 5
r = float(input("Enter radius: "))
area = 3.14159 * r * r
print(f"Area of circle = {area:.2f}")


# Program 8: Write a program to display formatted output using format() and % formatting.
print("{} scored {} marks in {}".format("Amit", 92, "Maths"))
print("%s is %d years old" % ("Neha", 19))


# Program 9: Write a program to convert a temperature from Celsius to Fahrenheit.
# Sample input: 37
c = float(input("Enter temperature in Celsius: "))
f = c * 9 / 5 + 32
print(f"{c}°C = {f:.1f}°F")


# Program 10: Write a program to calculate simple interest from principal, rate and time.
# Sample input: 5000, 8, 2
p = float(input("Principal: "))
r = float(input("Rate (%): "))
t = float(input("Time (years): "))
si = p * r * t / 100
print("Simple Interest =", si)

# Program 1: Write a program to print the multiplication table of 5 up to 10.
n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# Program 2: Write a program to find the sum of the first n natural numbers using a while loop.
n = 10
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print("Sum =", total)


# Program 3: Write a program to find the factorial of a number using a loop.
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"{n}! = {fact}")


# Program 4: Write a program to check whether a number is prime.
n = 29
if n < 2:
    print("Not prime")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(n, "is not prime")
            break
    else:
        print(n, "is prime")


# Program 5: Write a program to print the first 10 terms of the Fibonacci series.
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


# Program 6: Write a program to reverse a given number.
n = 1234
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Reversed =", rev)


# Program 7: Write a program to check whether a number is a palindrome.
n = 121
temp, rev = n, 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Palindrome" if rev == n else "Not palindrome")


# Program 8: Write a program to check whether a number is an Armstrong number.
n = 153
digits = len(str(n))
total = sum(int(d) ** digits for d in str(n))
print("Armstrong" if total == n else "Not Armstrong")


# Program 9: Write a program to find the sum of the digits of a number.
n = 4582
s = 0
while n > 0:
    s += n % 10
    n //= 10
print("Sum of digits =", s)


# Program 10: Write a program to print numbers from 1 to 15, showing Fizz for multiples of 3, Buzz for multiples of 5 and FizzBuzz for multiples of both.
for i in range(1, 16):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Program 1: Write a function that takes a name as a parameter and prints a greeting.
def greet(name):
    print("Hello,", name)

greet("Riya")
greet("Aman")


# Program 2: Write a function that returns the sum of two numbers.
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum =", result)


# Program 3: Write a function with a default argument that raises a base to a power (default power is 2).
def power(base, exp=2):
    return base ** exp

print(power(5))
print(power(2, 10))


# Program 4: Write a function using *args that returns the sum of any number of values.
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))
print(total(10, 20, 30, 40))


# Program 5: Write a function using **kwargs that prints all the keyword arguments passed to it.
def show(**info):
    for key, value in info.items():
        print(key, "->", value)

show(name="Asha", age=20, city="Indore")


# Program 6: Write programs using lambda functions to square a number, add two numbers and sort words by length.
square = lambda x: x * x
add = lambda a, b: a + b
print(square(6))
print(add(3, 4))
words = ["banana", "kiwi", "apple"]
print(sorted(words, key=lambda w: len(w)))


# Program 7: Write a recursive function to find the factorial of a number.
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

print(fact(6))


# Program 8: Write a function that returns the minimum, maximum and average of a list.
def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)

lo, hi, avg = stats([4, 8, 15, 16, 23])
print("Min:", lo, "Max:", hi, "Avg:", avg)


# Program 9: Write a program using filter() and map() with functions to select even numbers and multiply items by 10.
def is_even(n):
    return n % 2 == 0

nums = [1, 2, 3, 4, 5, 6]
print(list(filter(is_even, nums)))
print(list(map(lambda x: x * 10, nums)))


# Program 10: Write a program to demonstrate local and global variable scope using the global keyword.
count = 0

def increment():
    global count
    count += 1

increment()
increment()
print("Count =", count)

# Program 1: Write a program that uses a function to print all prime numbers up to 30.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print([n for n in range(1, 31) if is_prime(n)])


# Program 2: Write a function to find the GCD of two numbers.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("GCD(48, 18) =", gcd(48, 18))


# Program 3: Write a function that returns the first n terms of the Fibonacci series as a list.
def fib(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print(fib(12))


# Program 4: Write a function to count the vowels in a string.
def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

print(count_vowels("Programming in Python"))


# Program 5: Write a function to check whether a string is a palindrome (ignoring spaces and case).
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

for word in ["Madam", "Python", "nurses run"]:
    print(word, "->", is_palindrome(word))


# Program 6: Write a function to assign a grade and use it on a dictionary of student marks.
def grade(m):
    if m >= 90: return "A+"
    elif m >= 75: return "A"
    elif m >= 60: return "B"
    elif m >= 40: return "C"
    return "Fail"

students = {"Amit": 92, "Neha": 78, "Ravi": 55, "Sita": 35}
for name, marks in students.items():
    print(f"{name}: {marks} -> {grade(marks)}")


# Program 7: Write a program to find all perfect numbers up to 500 using a function.
def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

for n in range(1, 501):
    if is_perfect(n):
        print(n, end=" ")
print()


# Program 8: Write a function to generate the Collatz sequence for a number.
def collatz(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

print(collatz(6))


# Program 9: Write a menu-driven calculator using a function that keeps running until the user quits.
# Sample input: +, 10, 5, /, 20, 4, q
def calc(op, a, b):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/": return a / b if b != 0 else "Cannot divide by zero"
    return "Invalid operator"

while True:
    op = input("Operator (+,-,*,/ or q to quit): ")
    if op == "q":
        print("Bye!")
        break
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print("Result =", calc(op, a, b))


# Program 10: Write a program to find all Armstrong numbers between 100 and 999 using a function.
def is_armstrong(n):
    return n == sum(int(d) ** 3 for d in str(n))

print([n for n in range(100, 1000) if is_armstrong(n)])

# Program 1: Write a program to find all the factors of a number.
def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

print("Factors of 36:", factors(36))


# Program 2: Write a program to find the prime factors of a number using trial division.
def prime_factors(n):
    result = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            result.append(d)
            n //= d
        d += 1
    if n > 1:
        result.append(n)
    return result

print("Prime factors of 84:", prime_factors(84))


# Program 3: Write a program to display the prime factorization of a number in exponent form.
def factor_powers(n):
    powers = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            powers[d] = powers.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        powers[n] = powers.get(n, 0) + 1
    return powers

p = factor_powers(360)
print(" x ".join(f"{b}^{e}" for b, e in p.items()))


# Program 4: Write a program to count the number of factors of a number using its prime factorization.
def count_factors(n):
    count = 1
    d = 2
    while d * d <= n:
        e = 0
        while n % d == 0:
            e += 1
            n //= d
        count *= (e + 1)
        d += 1
    if n > 1:
        count *= 2
    return count

print("Number of factors of 360 =", count_factors(360))


# Program 5: Write a program to find the sum of all factors of a number.
def sum_factors(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)

print("Sum of factors of 28 =", sum_factors(28))


# Program 6: Write a program to find the GCD (HCF) of two numbers using Euclid's method.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("GCD of 48 and 18 =", gcd(48, 18))


# Program 7: Write a program to find the LCM of two numbers using their GCD.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print("LCM of 12 and 18 =", lcm(12, 18))


# Program 8: Write a program to find the common factors of two numbers.
a, b = 24, 36
common = [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]
print("Common factors:", common)


# Program 9: Write a program to factorize a number using Fermat's factorization method.
import math

def fermat(n):
    a = math.isqrt(n)
    if a * a < n:
        a += 1
    while True:
        b2 = a * a - n
        b = math.isqrt(b2)
        if b * b == b2:
            return a - b, a + b
        a += 1

print("5959 =", fermat(5959))


# Program 10: Write a program to list the factor pairs of a number efficiently using the square-root limit.
n = 100
pairs = []
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        pairs.append((i, n // i))
print("Factor pairs of 100:", pairs)

# Program 1: Write a program to create an integer array and print it with its first and last elements.
from array import array

arr = array('i', [10, 20, 30, 40, 50])
print(arr)
print("First:", arr[0], "Last:", arr[-1])


# Program 2: Write a program to add elements to an array using append() and extend().
from array import array

arr = array('i', [1, 2, 3])
arr.append(4)
arr.extend([5, 6])
print(arr)


# Program 3: Write a program to insert an element into an array at a given position.
from array import array

arr = array('i', [10, 20, 40, 50])
arr.insert(2, 30)
print(arr)


# Program 4: Write a program to delete an element from an array using remove() and pop().
from array import array

arr = array('i', [5, 10, 15, 20, 25])
arr.remove(15)
print(arr)
print("Popped:", arr.pop())
print(arr)


# Program 5: Write a program to find the index of an element and count its occurrences in an array.
from array import array

arr = array('i', [1, 2, 3, 2, 4, 2])
print("Index of 3:", arr.index(3))
print("Count of 2:", arr.count(2))


# Program 6: Write a program to reverse an array.
from array import array

arr = array('i', [1, 2, 3, 4, 5])
arr.reverse()
print(arr)


# Program 7: Write a program to find the sum, maximum, minimum and length of an array.
from array import array

arr = array('i', [4, 9, 2, 7])
print("Sum:", sum(arr))
print("Max:", max(arr))
print("Min:", min(arr))
print("Length:", len(arr))


# Program 8: Write a program to show the type code and item size of integer and double arrays.
from array import array

a = array('i', [1, 2])
b = array('d', [1.5, 2.5])
print(a.typecode, a.itemsize)
print(b.typecode, b.itemsize)
print(b)


# Program 9: Write a program to slice an array and convert it to a list.
from array import array

arr = array('i', [10, 20, 30, 40, 50, 60])
print(arr[1:4])
print(arr[::2])
print(arr.tolist())


# Program 10: Write a program to traverse an array using indexes and display it in sorted order.
from array import array

arr = array('i', [42, 7, 19, 3, 25])
for i in range(len(arr)):
    print(f"arr[{i}] = {arr[i]}")
print("Sorted:", array('i', sorted(arr)))

# Program 1: Write a program to add elements to a list using append(), insert() and extend().
nums = [1, 2, 3]
nums.append(4)
nums.insert(0, 0)
nums.extend([5, 6])
print(nums)


# Program 2: Write a program to delete list elements using remove(), pop(), del and clear().
items = [10, 20, 30, 40, 50, 60]
items.remove(20)
print(items.pop())
del items[0]
print(items)
items.clear()
print(items)


# Program 3: Write a program to sort and reverse a list.
nums = [5, 2, 9, 1, 7]
print(sorted(nums))
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)


# Program 4: Write a program to demonstrate slicing of a list.
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L[2:6])
print(L[:3])
print(L[-3:])
print(L[::2])
print(L[::-1])


# Program 5: Write a program to create lists using list comprehension.
squares = [x ** 2 for x in range(1, 8)]
evens = [x for x in range(1, 21) if x % 2 == 0]
print(squares)
print(evens)


# Program 6: Write a program to use count(), index() and membership testing on a list.
L = [3, 7, 3, 9, 3, 1]
print("Count of 3:", L.count(3))
print("Index of 9:", L.index(9))
print(7 in L, 100 in L)


# Program 7: Write a program to show the difference between copying a list and aliasing it.
a = [1, 2, 3]
b = a
c = a.copy()
b.append(99)
print("a:", a)
print("b:", b)
print("c:", c)


# Program 8: Write a program to create a 2D list (matrix) and find its transpose.
m = [[1, 2, 3], [4, 5, 6]]
for row in m:
    print(row)
t = [[m[r][c] for r in range(len(m))] for c in range(len(m[0]))]
print("Transpose:", t)


# Program 9: Write a program to find the sum, maximum, minimum and average of a list.
marks = [78, 92, 65, 88, 71]
print("Sum:", sum(marks))
print("Max:", max(marks), "Min:", min(marks))
print("Average:", sum(marks) / len(marks))


# Program 10: Write a program to merge two lists and remove duplicate elements.
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
merged = a + b
print(merged)
print(list(dict.fromkeys(merged)))
print(list(zip(a, b)))

# Program 1: Write a program to create a tuple and access its elements.
t = (10, 20, 30, 40, 50)
print(t)
print(t[0], t[-1])
single = (5,)
print(type(single), len(single))


# Program 2: Write a program to demonstrate slicing of a tuple.
t = (1, 2, 3, 4, 5, 6, 7)
print(t[1:4])
print(t[:3])
print(t[::2])
print(t[::-1])


# Program 3: Write a program to concatenate and repeat tuples.
a = (1, 2, 3)
b = (4, 5)
print(a + b)
print(a * 2)


# Program 4: Write a program to use count() and index() on a tuple.
t = (4, 8, 4, 2, 4, 9)
print("Count of 4:", t.count(4))
print("Index of 2:", t.index(2))


# Program 5: Write a program to demonstrate tuple packing and unpacking.
person = ("Asha", 20, "Indore")
name, age, city = person
print(name, age, city)
first, *rest = (1, 2, 3, 4)
print(first, rest)


# Program 6: Write a program to modify a tuple by converting it to a list and back.
t = (1, 2, 3)
temp = list(t)
temp[1] = 99
t = tuple(temp)
print(t)


# Program 7: Write a program to work with nested tuples.
students = (("Amit", 90), ("Neha", 85), ("Ravi", 72))
for name, marks in students:
    print(name, "->", marks)
print(students[1][0])


# Program 8: Write a program to find len, min, max and sum of a tuple and test membership.
t = (12, 5, 27, 8, 19)
print(len(t), min(t), max(t), sum(t))
print(27 in t, 100 in t)


# Program 9: Write a program to swap two values using tuples.
a, b = 10, 20
print("Before:", a, b)
a, b = b, a
print("After:", a, b)


# Program 10: Write a program to sort a tuple and use tuples as dictionary keys.
t = (5, 2, 8, 1)
print(sorted(t))
print(tuple(sorted(t, reverse=True)))
coords = {(0, 0): "origin", (1, 2): "point A"}
print(coords[(1, 2)])

# Program 1: Write a program to create a set and show that duplicates are removed.
s = {3, 1, 2, 3, 2}
print(s)
print(len(s))
print(set([1, 1, 2, 2, 3]))
empty = set()
print(type(empty), len(empty))


# Program 2: Write a program to add elements to a set using add() and update().
s = {1, 2, 3}
s.add(4)
s.update([5, 6, 2])
print(s)


# Program 3: Write a program to delete elements from a set using remove(), discard() and clear().
s = {1, 2, 3, 4, 5}
s.remove(3)
s.discard(10)
print(s)
s.clear()
print(s)


# Program 4: Write a program to find the union of two sets.
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
print(a.union(b))


# Program 5: Write a program to find the intersection of two sets.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)
print(a.intersection(b))


# Program 6: Write a program to find the difference of two sets.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a - b)
print(b - a)


# Program 7: Write a program to find the symmetric difference of two sets.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a ^ b)
print(a.symmetric_difference(b))


# Program 8: Write a program to check subset, superset and disjoint relations between sets.
a = {1, 2}
b = {1, 2, 3, 4}
c = {7, 8}
print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint(c))


# Program 9: Write a program to use set comprehension, membership testing and looping over a set.
squares = {x * x for x in range(1, 6)}
print(sorted(squares))
print(16 in squares, 10 in squares)
for x in sorted(squares):
    print(x, end=" ")
print()


# Program 10: Write a program to remove duplicates from a list using a set and demonstrate frozenset.
names = ["amit", "neha", "amit", "ravi", "neha"]
unique = sorted(set(names))
print(unique)
fs = frozenset([1, 2, 3])
print(fs)
print(2 in fs)

# Program 1: Write a program to create a dictionary and access its values.
student = {"name": "Asha", "age": 20, "course": "B.Tech"}
print(student)
print(student["name"])
print(len(student))


# Program 2: Write a program to add and update items in a dictionary.
d = {"a": 1, "b": 2}
d["c"] = 3
d["a"] = 100
d.update({"d": 4, "b": 20})
print(d)


# Program 3: Write a program to delete items from a dictionary using pop(), del, popitem() and clear().
d = {"a": 1, "b": 2, "c": 3, "d": 4}
print(d.pop("b"))
del d["a"]
print(d.popitem())
print(d)
d.clear()
print(d)


# Program 4: Write a program to use get(), setdefault() and membership testing on a dictionary.
d = {"x": 10, "y": 20}
print(d.get("x"))
print(d.get("z"))
print(d.get("z", "not found"))
d.setdefault("z", 30)
print(d)
print("y" in d)


# Program 5: Write a program to display the keys, values and items of a dictionary.
d = {"math": 90, "physics": 85, "chem": 78}
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))


# Program 6: Write a program to loop through a dictionary, including a nested dictionary.
students = {
    "Amit": {"age": 19, "marks": 90},
    "Neha": {"age": 20, "marks": 85},
}
for name, info in students.items():
    print(name, "->", info["age"], info["marks"])


# Program 7: Write a program to merge two dictionaries.
a = {"x": 1, "y": 2}
b = {"y": 20, "z": 30}
merged = a | b
print(merged)
a.update(b)
print(a)


# Program 8: Write a program to create dictionaries using dictionary comprehension.
squares = {n: n ** 2 for n in range(1, 6)}
print(squares)
evens = {k: v for k, v in squares.items() if v % 2 == 0}
print(evens)


# Program 9: Write a program to count the frequency of each word in a sentence.
text = "the cat and the dog and the bird"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)


# Program 10: Write a program to sort a dictionary by value and find the key with the maximum value.
scores = {"Amit": 82, "Neha": 95, "Ravi": 67, "Sita": 90}
by_value = dict(sorted(scores.items(), key=lambda kv: kv[1], reverse=True))
print(by_value)
top = max(scores, key=scores.get)
print("Topper:", top, scores[top])




# Class work to update lab manual starts here

# Updating list

a = [1,2,3,4,5]
b = a
b[0] = 10 
print(a)
print(b)

a.append(6)
print(a)
del a[5]
print(a)

# printing list using while loop
l = [10,20,30,[40,50,60],70,80,90]
i = 0
while i < len(l):
    print(f"List[{i}] = {l[i]}")
    i += 1

# basic functions
l.append(100)
print(l)
print(l.count(30))
print(l.index(100))
l.insert(3,30)
print(l)
l.pop(7)
print(l)
l.remove(100)
print(l)
lr = l.reverse()
print(lr)
ls = l.sort()
print(ls)
le = [110,120,130]
l.extend(le)
print(l)

# Find sum and average
s = [10,20,30,40,50,60,70,80,90,100]
print(s)
print(sum(s))
print(sum(s)/len(s))
sumoflist = 0
for i in range(len(s)):
    sumoflist = s[i] + sumoflist
    i += 1
avg = sumoflist/len(s)
print (f"sum is {sumoflist}")
print (f"average is {avg}")

# using range and enumerate
for index,i in enumerate(s):
    print(f"{i} is at index: {index}")
for i in range(len(s)):
    print(f"index: {i}")

# iterator in list
it = iter(s)
for i in range(len(s)):
    print(f"Obj at index {i} is: {next(it)}")

# Filter in list
def checkoffilter(x):
    if (x % 3 == 0):
        return 1

e = list(filter(checkoffilter, range(10,100,10)))
print(e)

# Map in list
def checkofmap(x):
    if (x % 3 == 0):
            return x
    else :
            return 0

m = list(map(checkofmap, range(10,100,10)))
print(m)

# reduce funtion
import functools
def add (x,y):
    return x + y
print(functools.reduce(add, s))




l=10
w=4
area=l*w
print("Area of rectangle is:", area)

# comment

# temperature in celsius
t = 25
#temperature in fahrenheit
f = (t * 9/5) + 32
print("Temperature in Fahrenheit is:", f)

# calcualte simple interest
p = 1000 
rate = 5
time = 2
si = (p * rate * time) / 100
print("Simple Interest is:", si)

# swap two varibale using one temperary variable
a = 15
b = 30
temp = a
a = b
b = temp
print("After swapping: a =", a, "b =", b)

# calculate average of three numbers
num1 = 12
num2 = 18
num3 = 24
avg = (num1 + num2 + num3) / 3
print("Average of three numbers is:", avg)

# combining strings
f = 'Sam'
l = 'Altman'
name = f + ' ' + l
print("Combined string is:", name)

# convert hours into minutes and seconds
h = 3
m = h*60
s = h*3600
print("Hours in minutes:", m)
print("Hours in seconds:", s)

# compute sqaure and cube of a number
a = 4
s = a*a
c = a**3
print("The square of number is:", s)
print("The cube of number is:", c)

# finding quotient and remainder of two numbers
a = 23
b = 5
q = a // b
r = a % b  
print("Quotient is:", q)
print("Remainder is:", r)

# calculate perimeter of triangle
s1 = 7
s2 = 10
s3 = 5
p = s1 + s2 + s3
print("The perimeter is:", p)

# Calculate the area of a circle
r = 7
pi = 3.14
a = pi * r**2
print("The area of the circle is:", a)

# Convert kilometer to miles
k = 15
m = k * 0.621371
print("Kilometers in miles:", m)

# calculate total and percentage of marks
s1 = 85
s2 = 90
s3 = 78
s4 = 88
t = s1 + s2 + s3 + s4
p = (t / 400) * 100
print("Total marks:", t)
print("Percentage:", p)

# swapping two variables without using the third one 
x = 25
y = 10
x = x + y
y = x - y
x = x - y
print("After swapping: x =", x, "y =", y)

n = [1, 2, 3, 4, 5]
print(n)
print(n[2:4])
n.append(6)
print(n)
n.insert(2, 7)
print(n)
n.extend([8, 9])
print(n)
n.pop()
n.remove(7)
n.clear()
del n[0]
print(n)

n.sort()
print(n)

print(sum(n))
print(min(n))
print(max(n))
print(len(n))
m = n.copy()
print(m)

o = [{"Sam" : 25}, {"Bill": 30}, {"Cap": 28}]
print(o)
print(o[1]["Bill"])
o.append({"Cap": 28})

n = [1 ,1 , 1, 2, 2, 2, 3, 4, 5]
nl = list(set(n))
print(nl)

n = ("Sam", 20, "CSE")
name, age, dept = n
m = ("Sam", 20, "CSE")
name, age, dept = m
print("Name:", name)
print("Age:", age)
print("Department:", dept)

nl = [1, 2, 3, 4, 5]
nt = tuple(nl)
print("List:", nl)
print("Tuple:", nt)

nt = (1, 2, 3, 4, 5)
nt.append(6)  # This will raise an AttributeError since tuples are immutable

def sum(n,m):
    s = n+m
    print("Sum of the numbers is:", s)
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
sum(a,b)

def printn(n):
    if n == 0:
        return
    print(n)
    printn(n-1)
a = int(input("Enter a number: "))
printn(a)

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
a = int(input("Enter a number: "))
print("Factorial of the input is:", fact(a))

# for cat 1 no set $ dict... control statement (while, for, nested loop, break, continue) is coming

# take a list containing few zeros print all the number of the list except 0

l = [0,1,2,3,0,4,0,5,6,0,7,8,0,9]
for i in range(0,len(l)):
    if l[i] == 0:
        continue
    print (l[i])

#print 5 to 1 except 3

for i in range(1,6):
    if i == 3:
        continue
    print(i)

#take a list containing positive and negative numbers print all the numbers in the lost until you are getting a negative number

l = [1,2,3,-3,5]
for i in range(0,len(l)):
    if l[i] < 0:
        break
    print(l[i])

#create a list having 6 numbers. search a number in that list, whne it is found display it within "Number is found". it should display number is found even though the number is present multiple times.

l = [1,2,3,4,3,5,6]
s = int(input("Enter a number to search: "))
c = 0
for i in range(0,len(l)):
    if l[i] == s:
        c = c + 1
    continue
print(f"Number {s} is found: {c} times")


c = 0
while True:
    s = int(input("Enter number: "))
    if s < 0:
        continue
    elif s == 0:
        break
    else:
        c = c + s
    x = input("Do you want to enter another number:(y/n) ")
    if x == "n":
        break
    else:
        continue
print(c)

#write a program to print numbers from 1 to 20 but skip the numbers that are divisible by 3

for i  in range(1,21):
    if i%3 == 0:
        continue
    print(i)

#Write a program to count the numbers of vowels in a given string. ignore spaces and consonents

v = ["a","e","i","o","u"]
s = input("Enter the string: ")
c = 0
for i in range(0,len(s)):
    for j in range(0,len(v)):
        if s[i] == v[j]:
            c += 1
            continue
print(f"The numbers of vowels are: {c}")

#Write a program to print the multiplication table of a number from 1 to 10 but skip the multiples of 4

for i in range(1,11):
    for j in range(1,11):
        if j == 4:
            continue
        print(f"{i} x {j} = {i*j}")

#Write a simple ATM program that alows the user to check balance, deposit money, withdraw money, or exit

while True:
    s = int(input("""Enter a command: 
    Enter 1 for chekcing balance
    Enter 2 for deposit money
    Enter 3 to withdraw money
    Enter 4 to exit
    """))
    b = 10000
    if s == 1:
        print(f"Balance: {b}")
        continue
    elif s == 2:
        d = int(input("Amount you want to deposit: "))
        b = b + d
        print(f"Available balance is {b}")
        continue
    elif s == 3:
        w = int(input("Enter the amout you want to withdraw: "))
        b = b - w
        print(f"Available balance is {b}")
    elif s == 4:
        break
    else:
        break

# Write a program, that repeately accepts number and provides options to check whether a number is even/odd, calculate its factor, or ignore a negative number

while True:
    s = int(input("Enter the number: "))
    o = int(input("""Enter a command: 
    Enter 1 for chekcing even/odd
    Enter 2 for calulating factor
    Enter 3 to exit"""))
    if o == 1:
        if s%2 == 0:
            print("Number is even")
        else:
            print("Number is odd")
    elif o == 2:
        c = 0
        for i in range(1,s+1):
            if s%i == 0:
                print(f"factors of {s} are:")
                print(i)
        continue
    elif o == 3:
        break
    else:
        continue

# Print a rectange of *
r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))
for i in range(0,r):
    for j in range(0,c):
        print("*",end=" ")
    print()

# Print a rectange of numbers
r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))
for i in range(0,r):
    for j in range(0,c):
        print(j+1,end=" ")
    print()

#Multiplication table
r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))
for i in range(0,r):
    for j in range(0,c):
        print((j+1)*(i+1),end=" ")
    print()

#triangle pattern
r = int(input("Enter the number of rows: "))
for i in range(1,r+1):
    print("* "*i)
i =0

for i in range(0,31,3):
    print(i)

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