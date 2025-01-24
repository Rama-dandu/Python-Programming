#FizzBuzz program. this quesion asked many times in interview
#take 1 to 100 numbers
#if number is divisible by 3 then print Fizz, by 5 print Buzz and by 3 and 5 then print FizzBuzz
#here order is important
for i in range(1,31,1):
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)
