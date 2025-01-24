#WAP to find weather the given number is leap year or not
year = int(input("Which your you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year!")
        else:
            print("not leap year!")
    else:
            print("leap year!")
else:
    print("not leap year!")

#1900 - not leap year
#2024 - leap year
#2023 - not leap year
#2025 - not leap year
#1993 - not leap year