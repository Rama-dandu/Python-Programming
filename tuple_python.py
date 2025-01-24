#tuples also similar to list which is also used to store the number of values in single variable.
#like lists , similar rules applied to tuples also like positive index, negative index, slicing and methods etc.,
#list are mutable - we can change
#but tuples are immutable - we can't change once created
#in both duplicates are allowed
#nesting of tuples also possible

# tuple1 = (12,6,-8,"rama",True,10.3)
# print(tuple1)

#accessing
# print(tuple1[0])
# print(tuple1[-6])

#type
# print(type(tuple1))
# tuple2 = (45,)
# print(type(tuple2))

# tuple1[0] = 7 #TypeError: 'tuple' object does not support item assignment - tuples are immutable
# print(tuple1)

# tuple1 = (12,6,-8,"rama",True,10.3)
# tuple2 = (45,7,39)
# tuple3 = (tuple1,tuple2) #nested tuple
# print(tuple3) #((12, 6, -8, 'rama', True, 10.3), (45, 7, 39))
# print(len(tuple3)) #2
#
# tuple3 = tuple1+tuple2 #tuple concatenation
# print(tuple3) #(12, 6, -8, 'rama', True, 10.3, 45, 7, 39)
# print(len(tuple3)) #9

#we can convert the list to tuple using tuple keyword
# list1 = [3,7,3,35,75]
# print(tuple(list1)) #(3, 7, 3, 35, 75)

#we can print one number multiple times
tuple5 = (19,) * 5
print(tuple5) #(19, 19, 19, 19, 19)

