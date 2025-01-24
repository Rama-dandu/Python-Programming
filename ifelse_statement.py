#if-else statements are used to check the condition
height = int(input("enter the age in feet: "))
if height > 3:
#print("buy token") #IndentationError: expected an indented block after 'if' statement on line 3
#we must provide the indentation or white space block after if statement
    print("buy token")
    print("now you can board the metro")
else:
    print("no token required")

#simple if
height1 = int(input("enter the age in feet: "))
if height1 > 3:
    print("buy token")
    print("now you can board the metro")
print("out of if block")

#coding exercise #6
#find whether the given number is even or odd
number = int(input("enter the number: "))
if number % 2 == 0:
    print("even number")
else:
    print("odd number")