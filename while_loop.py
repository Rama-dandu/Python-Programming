#syntax: while condition/expression:
#            statements(s)
#        else:
#            print("in else block")
#-1 is called sentinel value it is used to terminate the loop

# number = int(input("enter a number(-1 to quit): "))
#
# while number !=-1:
#     print(number)
#     number = int(input("enter a number(-1 to quit): "))
# else:
#     print('Condition failed')
# print('out of while loop')

#example
number = int(input('enter a number: '))
sum = 0
while number !=0:
    sum += number
    number = int(input('enter a number: '))
else:
    print(f"sum of numbers: {sum}")