#Assignment and relational operators
# '=' - assignment operator, short-hand operators - +=,-=,*=,/=,//=,%=,**=
a = 5
print(a)

# 5 = a
# print(5) #SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
# 5 = 6
# print(5) #same error like above

a,b,c = 10,20,30 #valid this way in python
print(a,b,c)

a,b = 4,3
c = a+b
a+=2
c+=a #short-hand operator
print(c) #13
c/=a #2.1666
print(c)

#comparision or relational operators
#<,>,<=,>=,==,!=
a = 20
print(a==20) #True
print(a<=20)
print(a<20)
print(a!=20)
print(a>20)
print(a>=5)

