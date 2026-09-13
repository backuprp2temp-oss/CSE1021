numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
squares = [x ** 2 for x in numbers] 
even_numbers = [x for x in numbers if x % 2 == 0] 
print("Squares:", squares) 
print("Even numbers:", even_numbers) 