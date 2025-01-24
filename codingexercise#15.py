#WAP to find the maximum number from list
string1 = input('Enter series of numbers: ')
list_numbers = string1.split(',')

big_num = 0;
for i in range(len(list_numbers)):
    list_numbers[i] = int(list_numbers[i])
    if i==0:
        big_num = list_numbers[i]
    else:
        if big_num < list_numbers[i]:
            big_num = list_numbers[i]
else:
    print(f"list of numbers: {list_numbers}")
    print(f"biggest number in list is: {big_num}")
