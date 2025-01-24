#random module is used to generate pseudo random number
import random

a = random.randint(2,5)
print(a)

b = random.randrange(2,5)
print(b)

c = random.random()

d = random.uniform(1,3)
print(d)

l = [43,76,4,3,9,1.0,6,1.67]
e = random.choice(l)
print(e)

random.shuffle(l)
print(l)



