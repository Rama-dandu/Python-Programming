#dictionaries are used to store the collection of data in the form of key and value.
#dictionaries are ordered, keys are immutable but values are mutable and no duplicates are allowed in keys.
#method 1 to declare a dictionary
phone_no = {
    'ram':1234,
    'shyam':3456,
    'mohan':8976,
    'ram':5677
}
# print(phone_no)
#values are mutable
phone_no['ram']= 8309030820
# print(phone_no)

phone_no['madav'] = {1111,3333}
# print(phone_no)

phone_no['shyam']={'shyam_home':4533,'shyam_office':7854}
print(phone_no)
# print(phone_no['shyam']['shyam_home'])
#get method to access the dictionary members
# print(phone_no.get('shyam'))

#example
#the data type which are immutable we can use them as keys.
data = {
    1:'jenny',
    2:'ram',
    0:'syam'
}
# print(data[0])
#values can be any data type

#del method used to delete dictionary key
# del phone_no['ram']
# print(phone_no)
#
# print(phone_no.pop('shyam')) #it deletet the selected item
# print(phone_no)
#
# print(phone_no.popitem()) #it delete the last item added
# print(phone_no)

#to clear total dictionary
# phone_no.clear()
# print(phone_no)

#we can access only keys
print(phone_no.keys())
print(phone_no.values())
print(phone_no.items()) #it will print list of all items in the form of tuples

#accessing pair using for loop
#method 1
# for i in phone_no:
#     print(i)
#     print(phone_no[i])

#method 2
# for i in phone_no.items():
#     print(i) #it will print the pair in the form of tuple

#copying the dictionary
phone_no2 = phone_no.copy()
print(phone_no2)

#finding length of dictonary
print(len(phone_no2))



# #method 2 to declare dictionary using dict() function
# phone_no1 = dict({
#     'ram':1234,
#     'shyam':3456,
#     'mohan':8976
# })
# print(phone_no1)
#
# #method3
# phone_no2 = dict([('ram',3453),('shyam',3685),('mohan',6753)])
# print(phone_no2)