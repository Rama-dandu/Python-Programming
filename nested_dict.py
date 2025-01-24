#nested dictionaries
student_data ={
    'ram':{'roll_no':10,'age':20,'course':'python'},
    'mohan': {'roll_no': 11, 'age': 22, 'course': 'c++'}

}
# print(student_data)
#if we want print particular key
# print(student_data['mohan'])
# print(student_data['mohan']['roll_no'])

#how to add another key and value to the present dictionary
student_data['mohan']['phone_no'] = 8309030820;
# print(student_data['mohan'])

#deleting value and key
#if you don't want to know what it returns use del function
# del student_data['mohan']['phone_no']
# print(student_data['mohan'])

#if you want to know what it returns
# print(student_data['mohan'].pop('phone_no'))

#nesting a list within a dictionary
travel_dat = {
    'gujarat':['dwarakadish','somanath','statue of unity'],
    'rajasthan':['jaipur','udaipur']
}
# print(travel_dat)
student_data1 =[
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
        'course': 'c++',
        'phone_no':[345664,246543]
    }
]

print(student_data1[1]['phone_no'])



