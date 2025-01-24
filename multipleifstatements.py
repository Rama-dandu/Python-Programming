height = int(input("what is your height?"))
bill = 0
if height >= 3:
    print("you can ride")
    age = int(input("what is your age?"))
    if age < 12:
        bill = 150
        print("Ticket price is 150 Rs.")
    elif age <= 18:
        bill = 250
        print("Ticket price is 250 Rs.")
    else:
        bill = 500
        print("Ticket price is 500 Rs.")

    want_photo = input("want to take photo?Y/N ")
    if want_photo == 'Y' or want_photo == 'y':
        bill = bill + 50;

    print(f"your total bill is {bill} Rs.")

else:
    print("you can't ride")
print("Thank you... enjoy the ride")