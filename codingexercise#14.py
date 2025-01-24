#WAP to calculate the average height from a list of heights.
string1 = input('enter the heights separated with comma: ')
list_heights = string1.split(',')
# print(list_heights)

#method 1
# sum = 0
#
# for i in list_heights:
#     # print(i)
#     sum+=int(i)
# else:
#     average = sum/len(list_heights)
#     print(average)

#method2
#finding count
count = 0
for height in list_heights:
    count+=1
# print(count)

#converting strings in list to intergers using round function
sum = 0
for i in range(0,count):
    list_heights[i] = int(list_heights[i])
    sum+=list_heights[i]
else:
    average = sum/count
    print(round(average))

# print(list_heights)

