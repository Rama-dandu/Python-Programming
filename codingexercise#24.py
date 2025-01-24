
student_data =[
    {
        'name':'ram',
        'roll_no':10,
        'age':20,
        'course':'python'
    },
    {
        'name':'mohan',
        'roll_no': 11,
        'age': 22,
        'course': 'c++'
    }
]

def add_new_student(name,roll_no,age,course):
    test = {'name':name,'roll_no':roll_no,'age':age,'course':course}
    student_data.append(test)


add_new_student("shyam",30,28,'java');
print(student_data)