import random
def user():
    user_list=[]
    numbers_list=[1,2,3,4,5,6,7,8,9,10,10,10,10]
    rand1_user=random.choice(numbers_list)
    # print(f"First user card:{rand1_user}")
    user_list.append(rand1_user)
    rand2_user=random.choice(numbers_list)  
    
    # print(f"Second user card:{rand2_user}")
    
    user_list.append(rand2_user)
    
    add=rand1_user+rand2_user
    # print(add)
    while add<17 and add>9:
        rand3_user=random.choice(numbers_list)
        new_sum=add+rand3_user
        user_list.append(rand3_user)
    
    print(f"user play:{user_list}")
    return add
user()
def computer():
    com_list=[]
    numbers_list=[1,2,3,4,5,6,7,8,9,10,10,10,10]
    rand1_user=random.choice(numbers_list)
    rand2_user=random.choice(numbers_list)
    
   
    com_list.append(rand1_user)
    com_list.append(rand2_user)
    
    add=rand1_user+rand2_user
    while add<17 and add>11:
    
            rand3_user=random.choice(numbers_list)
            add+=rand3_user
            com_list.append(rand3_user)
    print(f"Compurer_guess:{com_list}")
       
    # print(f"Final sum: {add}, Final list: {com_list}")
    return add
computer()
# user_score=user()
# computer_score=computer()
# if computer_score>user_score:
#     print("Computer is winner")
# elif computer_score<user_score:
#     print("user is winner")