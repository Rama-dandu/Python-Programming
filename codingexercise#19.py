#converting marks to grades
students_marks = {
    'jenny':92,
    'harry':78,
    'dimpy':56,
    'rahul':42,
    'aniket':99,
    'prem':34
}

students_grades={}
students_grades = students_marks.copy()
print(students_grades)

for i in students_marks.keys():
    # print(i)
    # print(students_marks[i])
    marks = students_marks[i]
    if marks>90:
        students_grades[i] = 'A+'
    elif marks>80:
        students_grades[i] = 'A'
    elif marks>70:
        students_grades[i] = 'B+'
    elif marks>60:
        students_grades[i] = 'B'
    elif marks>50:
        students_grades[i] = 'C'
    elif marks>40:
        students_grades[i] = 'D'
    else:
        students_grades[i] = 'F'

print(students_grades)


