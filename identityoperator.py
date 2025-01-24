""" identity operator is used to compare the addresses of objects.
   equity operator (==) is different from identity operator.
   equity operator is used to compare the values of variables.
   is, is not are the identity operators.
   In python memory manager doesn't alloca"""

a = 5
b = 5

#same address for the two objects because it's data types and values are same
print(id(a)) # 140733469755960
print(id(b)) # 140733469755960
print(a is b) # True
print(a is not b) # False

a = 4
b = 4.5

#different addresses for the two objects because it's data types are different.
print(id(a)) # 140733469755928
print(id(b)) # 2022117125232
print(a is b) # False
print(a is not b) # True


a = 6
b = 9

#different addresses for the two objects because it's values are different.
print(id(a)) # 140733469755992
print(id(b)) # 140733469756088
print(a is b) # False
print(a is not b) # True

#mutebel and immutable objects - mutabul means allocate seperate memory if we different values for same variable
#immutalbel objects
#here different memory locations
c = 5
print(id(c)) # 140735078402616

c = 6
print(id(c)) # 140735078402648
print(c is c)

#Even though the memory addresses of 5 and 6 are different,
# the statement c is c is still True because c is always the same object as itself, regardless of its value.
d = 5
print(id(d))
d = 6
print(id(d))
print(d is d)