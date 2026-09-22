# Dictionary-Based Student Record System: 
# Create a dictionary containing student names and marks.
# Develop functions to add/update records, calculate grades, search for a student, and identify students requiring academic support based on their marks.


students = {
    "Rajesh": 85,
    "Vaibhav": 72,
    "Prashant": 45,
    "Mayak": 91,
    "Sitanshu": 38
}


def add_or_update_student(name, marks):
    students[name] = marks
    print(f"Record for {name} added/updated successfully.")

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def search_student(name):
    if name in students:
        marks = students[name]
        grade = calculate_grade(marks)
        print(f"Name: {name}")
        print(f"Marks: {marks}")
        print(f"Grade: {grade}")
    else:
        print("Student not found.")


def students_needing_support():
    print("\nStudents requiring academic support:")
    
    found = False
    
    for name, marks in students.items():
        if marks < 50:
            print(f"{name} - {marks} marks (Grade: {calculate_grade(marks)})")
            found = True
    
    if not found:
        print("No students currently require academic support.")


# Display all student records
print("Student Records:")
for name, marks in students.items():
    print(f"{name}: {marks} marks - Grade {calculate_grade(marks)}")


# Add a new student
add_or_update_student("Rohan", 78)

# Update an existing student's marks
add_or_update_student("Vaibhav", 55)

# Search for a student
print("\nSearching for Prashant:")
search_student("Prashant")

# Find students requiring support
students_needing_support()

