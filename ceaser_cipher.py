

alphabet_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z']
word_input=input("Eneter the word:")
number_encrypt=int(input("enter the number for encoding:"))
encode_decode=input("encode or decode?")
    #hello
def encrypt(x,y,encode_decode):
    txt=""
    cipher=""
        
    for i in word_input:
        # if number_encrypt !=int:
        #     print("invalid character")
        if i not in alphabet_list :
            cipher+=i
            
        elif encode_decode=="encode":
            shifted_position= alphabet_list.index(i)+number_encrypt
            shifted_position %= len(alphabet_list)
            cipher+=alphabet_list[shifted_position]
        
        
        elif encode_decode=="decode":
            shifted_position= alphabet_list.index(i)-number_encrypt
            shifted_position%= len(alphabet_list)
            cipher+=alphabet_list[shifted_position]
        
            
            
    
    print(cipher)
    # if word_input not in alphabet_list:
    #         cipher=cipher+word_input
    #         print(cipher)
    
encrypt(x=word_input,y=number_encrypt,encode_decode=encode_decode)
x=True

while x:
        re_run=input("do you want to run the program again?")
        if re_run=="yes":
            alphabet_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z']
            word_input=input("Eneter the word:")
            number_encrypt=int(input("enter the number for encoding:"))
            encode_decode=input("encode or decode?")
            encrypt(x=word_input,y=number_encrypt,encode_decode=encode_decode)
            
        elif re_run=="no":
                x==False
                print("the game is over")
                break    