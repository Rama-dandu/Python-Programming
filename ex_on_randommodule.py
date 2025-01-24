#heads and tales program
import random
# side = random.randint(0,1)
# print(side)
# if side == 0:
#     print("tales")
# else:
#     print("heads")

names = input("Enter Everybody's name separated by comma: ")
names_list = names.split(",")

#method 1
# names_length = len(names_list)
# print(names_list)
# print(names_length)

# person = random.randint(0,names_length-1)
# print(person)
# print(names_list[person] + " will pay the bill")
# print(f"{names_list[person]} will pay the bill")

#method 2
print(f"{random.choice(names_list)} will pay the bill") #random.choice pick the random names


