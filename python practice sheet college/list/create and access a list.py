#  Create and Access a List 
numbers = [10, 20, 30, 40, 50]
print("List:", numbers) 
print("First element:", numbers[0]) 
print("Last element:", numbers[-1]) 
print("Third element:", numbers[2]) 
# Program 2: Add Elements — append(), insert(), extend() 
numbers = [10, 20, 30] 
 
# Add one element at the end 
numbers.append(40) 
 
# Add an element at a specific position 
numbers.insert(1, 15) 
 
# Add multiple elements 
numbers.extend([50, 60]) 
 
print(numbers) 
# O/P [10, 15, 20, 30, 40, 50, 60] 
# Program 3: Remove Elements — remove(), pop(), del, clear() 
numbers = [10, 20, 30, 40, 50] 
 
numbers.remove(30)      # Remove by value 
print(numbers) 
 
numbers.pop()           # Remove last element 
print(numbers) 
 
numbers.pop(0)          # Remove element at index 0 
print(numbers) 
 
del numbers[0]          # Delete element 
print(numbers) 
 
numbers.clear()         # Remove all elements 
print(numbers)
