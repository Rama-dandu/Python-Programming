#silent auction program
import os

def clear_console():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

print("*******welcome to the silent auction program********")
auction_mem = []
temp_dict = {}
high_act_mem= {'name':'dfdfd','bid':0}

while 1:
    name = input('What is your name?: ')
    bid_amount = int(input('What is your bid?: '))

    def add_mem(name,bid):
        if bid > high_act_mem['bid']:
            high_act_mem['name'] = name
            high_act_mem['bid'] = bid

    add_mem(name,bid_amount)
    temp_dict['name'] = name
    temp_dict['bid'] = bid_amount
    auction_mem.append(temp_dict)
    print(auction_mem)
    print(high_act_mem)
    other_mem = input('Are there any other bidders? type "yes" or "no": ')
    if other_mem == 'yes':
        clear_console()
        continue;
    elif other_mem == 'no':
        print(f"The winner is {high_act_mem['name']} with bid of {high_act_mem['bid']}")
        break

