
employees = [
    (101, "HR", 30000),
    (102, "IT", 50000),
    (103, "HR", 40000),
    (104, "IT", 60000),
    (105, "Sales", 35000)
]

department_salary = {}
department_count = {}

for emp_id, department, salary in employees:
    if department not in department_salary:
        department_salary[department] = 0
        department_count[department] = 0

    department_salary[department] += salary
    department_count[department] += 1

print("Average salary by department:")
for department in department_salary:
    average = department_salary[department] / department_count[department]
    print(department, ":", average)



# The expected time complexity is O(n), where n is the number of employees, 
# Each employee is processed once, and the final loop visits each distinct department once.
# Dictionary operations take O(1) average time, so the overall expected time complexity is O(n).


# and the auxiliary space complexity is O(d), where d is the number of distinct departments.
# because the two dictionaries store one entry per department.


# Scenario where the code may fail:

# The program assumes that every employee tuple contains exactly three elements and that the salary is numeric.
# For example, if an employee tuple contains a salary such as "forty thousand" instead of a number, the statement department_salary[department] += salary will raise a TypeError, because a number cannot be added to a string.