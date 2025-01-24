#arbitary positional arguments
# def add(*numbers): #(1,2,3,4,56,8)
#     c=0
#     for i in numbers:
#         c+=i
#     print(f"sum is {c}")
#
# add(1,2)
# add(6,5,6)
# add(1,2,3,4,56,8)


#tuple is immutable that's why arguments are converting into tuple, we can't change it's values in tuple
#we can't pass keyword arguments, it will not accept
# def fun(*numbers):
#     print(numbers)
#
# fun(1,2,"jenny")
#it will take jenny into tuple
#if we want to consider jenny as separate from tuple use keyword argument
# def fun(*numbers,name):
#     print(numbers)
#     print(name)
#
# fun(1,2,name = "jenny")

# pass positional argument first and then pass arbitary positional arguments
# def fun(name,*numbers):
#     print(name)
#     print(numbers)
#
# fun("jenny",2,4)

#arbitry keyword arguments
# def info_person(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
#
# info_person(name="rama",age='30',dept='ece')
# info_person(name='aruna',dept='ece')

#arbitry positional argument must be before arbitry keyword arguments
# def info_person(*args,**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#     print(args)
#
#
# info_person(1,2,3,name="rama", age='30', dept='ece')
# info_person(1,2,3,4,name='aruna', dept='ece')

import math
#coding exercise
def paint_fun(h, width, coverage = 7):
    no_of_cans = (h * width)/coverage;
    # print(f"cans required to paint wall: {no_of_cans} {no_of_cans.__ceil__()}")
    #or
    print(no_of_cans)
    no_of_cans = math.ceil(no_of_cans)
    print(no_of_cans)
paint_fun(h = 5,width = 6)