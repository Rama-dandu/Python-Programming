# def greet(name,dept):
#     print(f"Hi {name}")
#     print(f"are you from {dept} department")

# greet("jenny","CS") #positional arguments

#if we don't know about definition just we now that there is some def we prefer keyword arguments
# greet(name="jenny",dept="cs") #keyword argument
#or
# greet(dept='cs',name='jenny') #no need of argument order

#mixer of keyword and positional arguments
# greet('jenny',dept='cs')
#keyword arguments should follow positional arguments

#default arguments
# def greet(name,subject, dept = "cs"):
#     print(f"Hi {name}")
#     print(f"do you teach {subject}")
#     print(f"are you from {dept} department")

# greet("jenny",'python')#not providing department by default it it taking cs
# greet("jenny","python","ECE")
#default arguments should follow non-default arguments

#arbitary arguments
#no of arguments will vary every time when we call the function
def add(*numbers):  #variable length arguments it will accept all numbers and convert it into tuple
    sum = 0         # it will accept only arbitrary positional arguments
    for i in numbers:
        sum = sum + i
    print(f"sum is {sum}")

add(5,7,9,5,4)
