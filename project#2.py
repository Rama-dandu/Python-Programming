#password generator
import random
print('Welcome to the Password Generator!')
string_letters = int(input("how many letters would you like in you password? "))
string_symbols = int(input("how many symbols would you like in you password? "))
string_numbers = int(input("how many numbers would you like in you password? "))

list_letters = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m',
                'M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']

list_symbols = [ '!','@','#','$','%','^','&','*','(',')','_','+','-','=','{','}','[',']','|',':','/',';','<','>','?','~']

list_numbers = ['0','1','2','3','4','5','6','7','8','9']

# method 1 - easy method
list_password = []

for i in range(string_letters):
    list_password.append(random.choice(list_letters))
# else:
    # print(list_password)

for i in range(string_symbols):
    list_password.append(random.choice(list_symbols))
# else:
    # print(list_password)

for i in range(string_numbers):
    list_password.append(random.choice(list_numbers))
# else:
#     print(list_password)

random.shuffle(list_password)
# print(list_password)

#one way
#password = ''.join(list_password)

#another way
password = ""
for i in list_password:
    password += i #we can use + for concatenation of letter or word to the string or list instead of append
print(f"your password: {password}")

#method 2



