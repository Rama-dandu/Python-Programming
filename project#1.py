'''
rock,paper and scissors game
rules:
rock wins against scissor,
scissor win against paper,
paper wins against rock
0 - rock
1 - paper
2 - scissor
'''

import random
user = input("Enter Rock or Scissor or Paper: ")
if user == 'Rock':
    user = 0
elif user == 'Paper':
    user = 1
elif user == 'Scissor':
    user = 2
elif user != 'Rock' or user != 'Paper' or user != 'Scissor':
    user = 3

# comp_choice = random.randint(0,2)
# if comp_choice == 0:
#     print('Rock')
# elif comp_choice == 1:
#     print('Paper')
# elif comp_choice == 2:
#     print('Scissor')

#method1
# if user == comp_choice:
#     print("draw between you and computer")
# elif user > comp_choice and (user == 0 or user == 1 or user ==2):
#     print("you win")
# elif user < comp_choice:
#     print("you lose")
# elif user == 0 and comp_choice == 2:
#     print("you win")
# elif user == 2 and comp_choice == 0:
#     print("you lose")
# elif user == 3:
#     print("you lost, entered invalid input")

#method2

if user == 3:
    print("you lost, entered invalid input")
else:
    comp_choice = random.randint(0,2)
    if comp_choice == 0:
        print('Rock')
    elif comp_choice == 1:
        print('Paper')
    elif comp_choice == 2:
        print('Scissor')

    if user == comp_choice:
        print("draw between you and computer")
    elif user == 0 and comp_choice == 2:
        print("you win")
    elif user == 2 and comp_choice == 0:
        print("you lose")
    elif user > comp_choice:
        print("you win")
    elif user < comp_choice:
        print("you lose")

