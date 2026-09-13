words = ["python", "java", "python", "c", "java", "python"] 
frequency = {} 
for word in words: 
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)