
students = []
marks = []
grades = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("\nEnter student name: ")
    mark = int(input("Enter marks: "))

    students.append(name)
    marks.append(mark)

    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    elif mark >= 40:
        grade = "E"
    else:
        grade = "F"

    grades.append(grade)

print("\n--- Student Grading System ---")

for i in range(n):
    print("Name:", students[i])
    print("Marks:", marks[i])
    print("Grade:", grades[i])
    print("--------------------")
