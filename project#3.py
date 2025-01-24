#Hangman Game
import random
print("Let's Play Hangman!")
print('you have only 6 lives so try to guess the word within 6 attempts! Good luck!!')

list_words = ['apple','banana','orange','mango','grapes','pineapple','pomegranate','avocado','coconut','papaya',
              'watermelon','dragon fruit','strawberry','blueberry','blackberry','gooseberry','cherry','apricot',
              'jackfruit','kiwifruit','lime','peach','pear','tamarind','custard apple','fig','guava','musk melon','olives','java plum']

pick_word = random.choice(list_words)
len_word = len(pick_word)
# print(len_word)
# print(pick_word)
guess_word = []
for i in range(len_word):
    guess_word.append('_')
else:
    print(f"guess a word: {guess_word}")

no_of_lives = 6
count = 0

#hangman images
hangman_head = ('+-------------+''\n'
                '       ''|''      ''|''\n'
                '       ''O''      ''|''\n'
                '              ''|''\n'
                '              ''|''\n'
                '              ''|''\n'
                '              ''|''\n'
                '              ''|''\n'
                 '--------------------''\n'
                 '--------------------')

hangman_body = ('+-------------+''\n'
                '       ''|''      ''|''\n'
                '       ''O''      ''|''\n'
                '       ''|''      ''|''\n'
                '              ''|''\n'
                '              ''|''\n'
                '              ''|''\n'
                '              ''|''\n'
                 '--------------------''\n'
                 '--------------------')

hangman_hand1 = ('+-------------+''\n'
                '       ''|''      ''|''\n'
                '       ''O''      ''|''\n'
                '      ''/''|''      ''|''\n'
                '              ''|''\n'
                '              ''|''\n'
                '              ''|''\n'
                '              ''|''\n'
                 '--------------------''\n'
                 '--------------------')

hangman_hand2 = ('+-------------+''\n'
                '       ''|''      ''|''\n'
                '       ''O''      ''|''\n'
                '      ''/''|''\\' '     ''|''\n'
                '              ''|''\n'
                '              ''|''\n'
                '              ''|''\n'
                '              ''|''\n'
                 '--------------------''\n'
                 '--------------------')

hangman_leg1 = ('+-------------+''\n'
                '       ''|''      ''|''\n'
                '       ''O''      ''|''\n'
                '      ''/''|''\\' '     ''|''\n'
               '      ''/''       ''|''\n'
                '              ''|''\n'
                '              ''|''\n'
                '              ''|''\n'
                 '--------------------''\n'
                 '--------------------')

hangman_leg2 = ('+-------------+''\n'
                '       ''|''      ''|''\n'
                '       ''O''      ''|''\n'
                '      ''/''|''\\' '     ''|''\n'
               '      ''/'' ''\\''     ''|''\n'
                '              ''|''\n'
                '              ''|''\n'
                '              ''|''\n'
                 '--------------------''\n'
                 '--------------------')

#main logic
i=0
while 1:
    string_letter = input("Guess a letter: ")
    if pick_word[i] == string_letter:
        # guess_word.append(string_letter)
        guess_word[i] = string_letter
        print('you guessed correct letter!\n')
        print(guess_word);
        if i==len_word-1:
            print('you win,congratulations')
            break
        i += 1
    else:
        print('you guessed wrong letter!')
        count+=1
        # print(f"counter: {count}")
        no_of_lives -= 1
        if count == 1:
            print(f"hangman:\n {hangman_head}")
            print(f"you have only {no_of_lives} lives\n")
        elif count == 2:
            print(f"hangman:\n {hangman_body}")
            print(f"you have only {no_of_lives} lives\n")
        elif count == 3:
            print(f"hangman:\n {hangman_hand1}")
            print(f"you have only {no_of_lives} lives\n")
        elif count == 4:
            print(f"hangman:\n {hangman_hand2}")
            print(f"you have only {no_of_lives} lives\n")
        elif count == 5:
            print(f"hangman:\n {hangman_leg1}")
            print(f"you have only {no_of_lives} lives\n")
        elif count == 6:
            print(f"hangman:\n {hangman_leg2}")
            print(f"you lost,better luck next time\n")
            break








