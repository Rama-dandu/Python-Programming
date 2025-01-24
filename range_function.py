#range(start,stop,step_size) function is used to generate the sequence of numbers depending on step size.
#by defualt start point is 0 and step_size is 1.
#all arguments for ragne function must be integers
#this range function is used in for loop to iterate a loop upto some particular range.
# a = range(0,15,2)
# for i in a:
#     print(i)

# 0 and negative number is not allowed in step size as argument
# a = range(0,15,-3)
# for i in a:
#     print(i) #it results nothing

# a = range(0,15,0)
# for i in a:
#     print(i) #ValueError: range() arg 3 must not be zero

#in negative order we can give it is decreasing order
# a = range(10,0,-1)
# for i in a:
#     print(i)

# a = range(-1,-10,-1)
# for i in a:
#     print(i)

#adding numbers from 1 to 100 and printing it's sum
sum = 0
for i in range(1,101,1):
    sum+=i
else:
    print(f"sum of 1 to 100 number is : {sum}")