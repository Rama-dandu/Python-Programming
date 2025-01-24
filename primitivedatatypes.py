#primitive data types int float string and boolean
#type() function is used to print the type of the variable
#no need to mention the data type while declaring the variable
#ex1
var_1 = 1;
print(type(var_1)) #<class 'int'> var_1 is the object or instance of class int
#ex2
#there is no range limit for data types in python it only depends on the system memory
var_2 = 123445685904936857899098777;
print(var_2) #this value printed
#ex3
#adding of integer and float number
var_3 = 23
var_4 = 40.34
print(var_3 + var_4)
#ex4
#this binary, octal and hexa decimals are objects or instances of class int
#binary number
var_5 = 0b1010
print(var_5)
#octal number
var_6 = 0o123
print(var_6)
#hexa decimal number
var_7 = 0x123
print(var_7)
print(type(var_5),type(var_6),type(var_7))
#ex5
#\ is used to skip the meaning of anything
print("Jenny's Lectures");#correct
# print("Jenny's "Lectures"") #SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("Jenny\'s \"Lectures\"") #solution
print("Jenny\'s \n \"Lectures\"") #new line
#now I want to skip the meaning of this new line
print("Jenny\'s \\n \"Lectures\"") #now as it is printed
#I want to print my name 5 times
print(5 * "rama \n")
#ex6 - boolean
#only capital T for True and F for False, if we write small t or f it will give naming error
var_8 = True
var_9 = False
print(var_8)
print(var_9)
print(type(var_8))#<class 'bool'>

a = 10
b = 20
var_10 = a<b #it returns True boolean
print(var_10)




