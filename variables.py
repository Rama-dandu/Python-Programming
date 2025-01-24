#variables
#are the containers which are used to store the value
#no need to declare variable it's use and no need of data type we can directly assign whatever we want to assign usng assignment operator
#Ex1
from email.contentmanager import raw_data_manager

name = "rama"
print(name)
#Ex2
number = 1
print(number)
#Ex3
number1 = 1.4
print(number1)
#Ex4
name = input("what is your name? ")
print(name)
#Ex5
#len() function is used to find the length of the string
length = len(name)
print(length)

#Ex5
a = 1
b = "rama"

#adding of integer and string gives type error. TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(a + b)

#we can concatenate only same data types
print(name + b)


