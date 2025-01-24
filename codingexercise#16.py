#WAP to find the sum of even numbers from 1 to 100 (including 1 and 100)

#method 1
# sum = 0
# for i in range(1,101,1):
#     if i%2 == 0:
#         sum+=i
# else:
#     print(f"sum of even numbers from 1 to 100 is: {sum}")

#method 2
sum = 0
for i in range(0,101,2):
    sum+=i
else:
    print(f"sum of even numbers from 1 to 100 is: {sum}")