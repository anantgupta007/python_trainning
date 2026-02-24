# student_topper.py

n = int(input())   # number of students
marks = {}

for _ in range(n):
    name = input()
    score = int(input())
    marks[name] = score

topper = max(marks, key=marks.get)

print(topper)