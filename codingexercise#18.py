#finding the given number is prime or not
#the number which is divisible by 1 and itself is called prime number
#2 is also a prime number

#prime function
def prime_fun(num):
    if num == 2:
        print('prime number')
        return
    elif num == 1:
        print('not prime number')
        return
    else:
        for i in range(2,num):
            # print(i)
                if num%i==0:
                    print('not prime number')
                    return

    print('prime number')

#main loop
while 1:
    prime_number = int(input("enter the number: "))
    prime_fun(prime_number)