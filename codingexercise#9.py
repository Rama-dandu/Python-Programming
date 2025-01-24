#pizza order program
# size = input("size of pizza? Small/Medium/Large ")
# bill = 0
# if size == 'Small' or size == 'small':
#     bill = 100
#     pepper = input("do you want pepper? Y/N ")
#     if pepper == 'Y' or pepper == 'y':
#         bill = bill + 30
# else:
#     if size == 'Medium' or size == 'medium':
#       bill = 200
#     elif size == 'Large' or size == 'large':
#         bill = 300
#     pepper = input("do you want pepper? Y/N ")
#     if pepper == 'Y' or pepper == 'y':
#         bill = bill + 50
#
# extra_cheese = input("do you want extra cheese? Y/N ")
# if extra_cheese == 'Y' or extra_cheese == 'y':
#     bill = bill+20
# print(f"your total bill is {bill} Rs.")

#another logic
size = input("size of pizza? Small/Medium/Large ")
bill = 0

if size == 'Small' or size == 'small':
    bill += 100
elif size == 'Medium' or size == 'medium':
    bill += 200
elif size == 'Large' or size == 'large':
    bill += 300

pepper = input("do you want pepper? Y/N ")
if pepper == 'Y' or pepper == 'y':
    if size == 'Small' or size == 'small':
        bill += 30
    else:
        bill += 50

extra_cheese = input("do you want extra cheese? Y/N ")
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 20
print(f"your total bill is {bill} Rs.")