#sets are similar to lists and tuples, which are used to store multiple values in single variable.
#sets are not defined in order
#sets are immutable
#indexing is not allowed or not possible in sets.
#we can add or remove a set
#slicing is not allowed in set
set1 = {10,56,34,"rama",True}
# print(set1) #sets are not in defined order

#creaing of empty set
set2 = set() #empty set <class 'set'>
# set2 = {} #it is wrong of creating an empty set
# print(type(set1)) #<class 'set'>
# print(type(set2)) #<class 'dict'>

#adding of new variable to set
# set1[0] = 12
# print(set1) #TypeError: 'set' object does not support item assignment

# set1.add(20) #we can add only one item at a time
# print(set1) #{'rama', True, 34, 20, 56, 10}

#we can add immutable this to set
#tuple is immutable we can add tuple to set
set1.add((45,67,23))
print(set1)
set1.add([34,86,23])
print(set1)



