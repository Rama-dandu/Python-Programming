#syntax: for var_name in sequence:
#           statements(s)
#        else:
#           print("successfully completed for loop!")
list1 = [3,6,4,6,7,3]
for num in list1:
    print(num)
    if num==4:
        break #break will leads to exit of for loop not to else part
else:
    print('successfully completed for loop!')