#caesar cipher encryption and decryption project with shift key.
from operator import index

#encryption function
def encryption_fun(msg, shift_key):
    msg_list = msg.split()
    # print(msg_list)

    # main logic
    for i in range(len(msg_list)):
        for j in range(len(msg_list[i])):
            for k in range(len(alpha_list)):
                if msg_list[i][j] == alpha_list[k]:
                    enc_num = k
                    # print(enc_num)
            enc_char = (enc_num + shift_key) % 26
            # print(enc_char)

            for k in range(len(alpha_list)):
                if enc_char == k:
                    character = alpha_list[k]
                    # print(character)
                    encrypted_list.append(character)
                    # print(encrypted_list)
                    word = ''.join(encrypted_list)
                    # print(word)
        encrypted_list.clear()
        encrypted_text.append(word)
        word = '';
        # print(encrypted_text)
    encrypted_msg = ' '.join(encrypted_text)
    decrypted_text.clear()
    print(f"Here's the encrypted result: {encrypted_msg}")
    encrypted_msg = ""


#decryption function
def decryption_fun(msg, shift_key):
    msg_list = msg.split()
    # print(msg_list)

    # main logic
    for i in range(len(msg_list)):
        for j in range(len(msg_list[i])):
            for k in range(len(alpha_list)):
                if msg_list[i][j] == alpha_list[k]:
                    enc_num = k
                    # print(enc_num)
            enc_char = (enc_num - shift_key)
            if enc_char < 0:
                enc_char+=26
                enc_char%=26
            else:
                enc_char%=26
            # print(enc_char)
            for k in range(len(alpha_list)):
                if enc_char == k:
                    character = alpha_list[k]
                    # print(character)
                    decrypted_list.append(character)
                    # print(encrypted_list)
                    word = ''.join(decrypted_list)
                    # print(word)
        decrypted_list.clear()
        decrypted_text.append(word)
        # print(encrypted_text)
    decrypted_msg = ' '.join(decrypted_text)
    decrypted_text.clear()
    print(f"Here's the decrypted result: {decrypted_msg}")
    decrypted_msg = ""


#main function
alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
encrypted_list = []
encrypted_text = []
decrypted_list = []
decrypted_text = []

#encryption and decryption logic
while 1:
    enc_dec = input('Type "encrypt" for encryption and type "decrypt" for decryption:\n')
    msg = input('Type your message:\n')
    shift_key = int(input('Type the shift key:\n'))
    #calling the encryption function or decryption function
    if enc_dec == 'encrypt':
        encryption_fun(msg, shift_key)
    elif enc_dec == 'decrypt':
        decryption_fun(msg, shift_key)

    yes_no_msg = input('Type "yes" if you want to go again. otherwise type "no":\n')
    if yes_no_msg == 'yes':
        continue
    else:
        print('good bye')
        break








