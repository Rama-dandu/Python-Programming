#len() function is used to find only the length of the string not int or float or anything. if we try to find the length of int or float it will giv the type error
print(len("rama")) #correct
# print(len(123)) #TypeError: object of type 'int' has no len()
# print(len(12.5)) #TypeError: object of type 'float' has no len()
#type casting
length = len("rama");
print(length);
#now I want to print like my name has 4 characters
# print("my name has" + length + "characters") #TypeError: can only concatenate str (not "int") to str
#we need type casting to convert length from integer to string
print("my name has " + str(length) + " characters") #type casting length from integer to string

""" 
#this are multi line comments
#remaining type casting functions
int()
float()
str()
"""
print(int("10") + int("20")) #30 integer type casting
print(10 + float("12.2")) #22.2 float type casting

name = "rama"
# print(10+int(name)) #ValueError: invalid literal for int() with base 10: 'rama'
name = "12"
print(10+int(name)) #22 correct

#assignment
number_1 = input("enter first number: ")
number_2 = input("enter second number: ")
sum = int(number_1) + int(number_2)
print(sum)

#Excercise
#program to add the digits of a given number
number = input("enter the two digit number: ")
print(number)
print(int(number[0])+int(number[1]))