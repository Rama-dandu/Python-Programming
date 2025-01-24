#list is a data structure it is way of organizing and storing the data
#list is heterogeneous means it can store different data types
#list is dynamically sized array
#list is ordered and sequence data type, data stored in sequence
#list is mutable - we can modify list after creating it
#duplicates are allowed in list
from audioop import minmax
from traceback import print_tb

numbers = [1,2,-9,5,4,2,7,3,9]
# print(numbers)
names = ['rama','amika','amma']
# print(names)
mix_list = [1,'rama',True,10.10]
# print(mix_list)
# print(numbers[3])
# print(len(numbers))
# print(names[0])
# print(len(names))
# print(numbers[-4])
# print(numbers[0:4]) #string slicing
# print(numbers[0:9:5])# it is removing the number at each second step (extended slicing)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(max(numbers))
print(min(numbers))

numbers.append(45) #it will append only one element at end of the list
print(numbers)

numbers.insert(2,64)
print(numbers)

numbers.extend([34,87,56,3,23]) #it will extend the list at end of list
print(numbers)

numbers[0] = 1
print(numbers)

numbers[1:5] = [45,87,9,5] #it will add the numbers to the list
print(numbers)

numbers.remove(87) #it will remove the selected number from list
print(numbers)

numbers.pop() #pop will remove the last element without any argument
print(numbers)

numbers.pop(1) #if we specify the index then it will remove the specific number in list
print(numbers)

print(numbers.count(2))#it will print how many times 2 appears in the list

