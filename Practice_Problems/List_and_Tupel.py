# Exercise 3: Nested Lists – Grade Calculator
#
# You have a list of students, where each student is represented as a list:
# [name, grade1, grade2, grade3]

students = [
     ["Alice", 85, 90, 88],
     ["Bob", 78, 82, 80],
     ["Charlie", 92, 88, 91]
 ]

# Task:
# 1. For each student, calculate the average grade (mean of the three grades)
# 2. Create a new list of tuples: (name, average_grade)
students_average=[]

for i in range(len(students)): 
    avg=(students[i][1]+students[i][2]+students[i][3])/3
    tuple=(students[i][0],avg)
    students_average.append(tuple)

# 3. Print each student's name and their average, rounded to 1 decimal place
print(students_average)
# Expected output:

# Alice: 87.7
# Bob: 80.0
# Charlie: 90.3
