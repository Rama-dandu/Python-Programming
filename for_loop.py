#syntax: for var_name in sequence:
#           statements(s)
from operator import index

list1 = ['rama','aruna','amika','hemanshu', 'amma']
tuple1 = ('rama','aruna','amika','hemanshu', 'amma')
set1 = {'rama','aruna','amika','hemanshu', 'amma'}
# for name in set1:
#     print(name)

#we can directly use list or tuple or set in the place of sequence
# for name in {'kernal','masters'}:
#     print(name)

#we can use the strings also in the place of sequence
# string1 = 'rama'
# for name in string1:
#     print(name)

#access each element from list and make square of it
list1 = [2,5,3,-6,2.5]
list2 = []
for num in list1:
    square = num ** 2; #** power operator
    # print(square)
    list2.append(square)
print(list2)