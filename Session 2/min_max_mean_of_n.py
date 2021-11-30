students = int(input('enter the number of students: '))
grades = []
for i in range(students):
  grades.append(float(input('enter the grade: ')))
print(f'Max: {max(grades)}\nMin: {min(grades)}\nMean: {sum(grades)/students}')