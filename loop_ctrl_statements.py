#break, continue and pass are called the loop control statements, which are used to control the loop
# list1 = ['hi','hello','welcome']
# names = ['rama','aruna','hemanshu']
#
# for item in list1:
#     for name in names:
#         print(item,name)
#         if item == 'hello' and name == 'rama':
#             break #it will exit from only nearest loop not from two loops
#     print('out of inner loop')
# print('out of outer loop')

#continue
# count = 0
# while count<=10:
#     count+=1
#     if count==7:
#         continue
#     print(count)
# print('out of loop')

#pass
# for i in range(10):
#     pass

count = 0
while count<=10:
    count+=1
    if count==7:
        pass
    print(count)
print('out of loop')