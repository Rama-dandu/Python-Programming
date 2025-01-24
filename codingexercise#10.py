# #LOVE CALCULATOR
# #consider small true love letters
# person1 = input("enter person 1 name: ")
# person2 = input("enter person 2 name: ")
# person1 = person1.lower()
# person2 = person2.lower()
#
# #true
# a = person1.count('t')
# b = person2.count('t')
# t_count = a + b
#
# a = person1.count('r')
# b = person2.count('r')
# r_count = a + b
#
# a = person1.count('u')
# b = person2.count('u')
# u_count = a + b
#
# a = person1.count('e')
# b = person2.count('e')
# e_count = a + b
#
# total1 = t_count + r_count + u_count + e_count
#
# #love
# a = person1.count('l')
# b = person2.count('l')
# l_count = a + b
#
# a = person1.count('o')
# b = person2.count('o')
# o_count = a + b
#
# a = person1.count('v')
# b = person2.count('v')
# v_count = a + b
#
# a = person1.count('e')
# b = person2.count('e')
# e_count = a + b
#
# total2 = l_count + o_count + v_count + e_count
#
# print("love score: " + str(total1) + str(total2))
#
#code another
name1 = input("Enter your name: ")
name2 = input("Enter his/her name: ")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"your love score is {love_score} and you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
    print(f"your love score is {love_score} and you are always together")
else:
    print(f"your love score is {love_score}")
