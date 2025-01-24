#union methods make the common things union
#there are two ways for using union one is union as method and another one is '|' this symbol also do the same as union method
#we can perform the union operation even on more than 2 sets alos
# set1 = {'rama','hemanshu','aruna'}
# set2 = {'aruna','nanna','amma'}
# set3 = {'kernel','masters'}
# print(set1.union(set2))
# print(set1 | set2)
# print(set1.union(set2,set3))
# print(set1 | set2 | set3)

#we can pass the list or tuple as argument in union method, but we can't pass list or tuple as operand for '|' as operator for union
# print(set3.union((1,4,5,64))) #fist it will convert tuple as set then it will make union of two sets
# print(set1 | (1,4,5,64)) #TypeError: unsupported operand type(s) for |: 'set' and 'tuple'

#we can use update method to update the set with some more variables. update method works similar to union method.
# set1.update(set2)
# print(set1)
# set2.update(['kernel','masters'])
# print(set2)

#intersection method is used to extract the common variable in sets
#we can apply the intersection on multiple sets also, if there is common variable in three sets then it results otherwise it will give empty set()
#& operator is used to perform the intersection operation other than direct intersection method
# print(set1.intersection(set2))
# print(set1.intersection(set2,set3))
# print(set1 & set2)

#intersction update is used to update the common variables
# set1.intersection_update(['rama','amika'])
# print(set1)

#symmetric difference is used to find the things which are not present in the second set
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
# print(set1.difference(set2)) #it will the variables which are not present in set2 {1,2,3}
# print(set1-set2) #results the same as above

#instead of set we can pass list or tuple as argument to difference. first it will convert list or tuple as list then it will do operation
# print(set1.difference((7,6,75,4)))

#symmetric differece is used to extract the uncommon variables from multiple sets
# print(set1.symmetric_difference(set2))
# print(set1 ^ set2) #this operator will do the same thing. this operator we can apply on multiple sets
# set1.symmetric_difference_update(set2) #only one argument is allowed
# print(set1)
# print(set2)

#disjoint() method is used to check weather two sets are united with each other or not. it returns either true or false.
# print(set1.isdisjoint(set2)) #False
#there is no operator

#issubset() method - set1 is subset of set2 if every element of set1 is present in set2
# print(set1.issubset(set2)) #False
# print(set1 <= set2) #will do the same work

#issupersubset() method - set1 is super subset of set2 if every element of set2 is present in set1
# print(set1.issuperset(set2)) #False
# print(set1 >= set2) #will do the same work

#we can pass the list or tuple as argument to method

#set.clear() method is used to clear all the entries in set
# set1.clear() #it returns the empty set
# print(set1)

# del keyword is used to delete the set
del set1
print(set1) #NameError: name 'set1' is not defined. Did you mean: 'set2'?. because set1 is deleted in previous line itself


