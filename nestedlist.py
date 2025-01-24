#nested lists are the list within list
from traceback import print_tb

numbers = [12,76,4,7,3,-10,0,4.6,85,3,23] #it is list
numbers = [12,76,4,[7,3,-10,0],4.6,85,3,23] #it is nested list
#accessing of nested list
print(len(numbers))#8
print(numbers[3][0])#7
print(numbers[3])#[7, 3, -10, 0]
print(numbers[-5])#[7, 3, -10, 0] negative index
print(numbers[3][0:4])#[7, 3, -10, 0] slicing
print(numbers[3][:])#[7, 3, -10, 0]
print(numbers[3][0:1])#[7]
# print(numbers[3][::])#[startingIndex:length:step] default it will take 0:total length:0
print(numbers[3][::7])

list_names = [24,6,43,["rama","amma","aruna"],5,65,78,0,-10]
print(len(list_names))
print(list_names[3][2])

