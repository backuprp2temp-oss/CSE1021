marks = { 
"Amit": 85, 
"Rahul": 92, 
"Priya": 88, 
"Neha": 95 
}  
topper = max(marks, key=marks.get) 
print("Topper:", topper) 
print("Marks:", marks[topper])