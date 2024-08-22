import random
password=[]

letter_lists=['a','b','c','d','e','f','g','i','j','h','l','m','n','o','p']
num_list=['1','2','3','4','5','6','7','8','9']
char_list=['@','#','%','^','&','*']
letter_input=int(input("how many letters do you need?"))
num_input=int(input("how many numbers do you need?"))
num_char=int(input("how many characters do you need ?"))
for i in range(letter_input):
    choose_lett=random.choice(letter_lists)
   
    password.append(choose_lett)
for j in range(num_input):
    choose_num=random.choice(num_list)
    password.append(choose_num)
for k in range(num_char):
    choose_char=random.choice(char_list)
    password.append(choose_char)
random.shuffle(password)
final_password=''.join(password)
print(final_password)
