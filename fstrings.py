#fstrings are introduced in python 3.6.
#fstrings are used to print the strings and variables of int or float are anything we can print using f function and curly braces of varibles
name = "rama"
age = 31
height = 1.5

#general way of printing
print("my name is " + name,"I am " + str(age) + " years old","my height is " + str(height) +" meters")
#or
print("my name is",name,"I am",age,"years old","my height is",height,"meters")
#here in above two statements comma provides the space between two words
#now using fstrings
print(f"my name is {name} I am {age} years old my height is {height} meters")
#use of fstrings is no need of typecasting of variables, commas, plus. we can dircetly print using f function and curly braces to variables of any data type.\
#we can use the expressions also in fstings
print(f"krishna's fathers age is {age * 2} years")

#coding Exercise #5:
#write a program to find the how many days, weeks and months we have left if we live until 90 years old.
#1 year - 365 days
#1 year - 52 weeks
#1 year - 12 moths
#lets consider above details
#code
current_age = input("enter your age: ")
current_age = int(current_age)
print(current_age)
remaining_years = 90 - current_age;
print(remaining_years)
days = remaining_years * 365
weeks = remaining_years * 52
months = remaining_years * 12

print(f"you have {days} days, {weeks} weeks and {months} months left")