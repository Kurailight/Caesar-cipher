import sys
alphabet = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'R', 'S', 'Ś', 'T', 'U', 'W', 'Y', 'Z', 'Ż', 'Ź']
marks= [' ','.','?','!']
digits = list(str(a) for a in range(0, 10))
full_list= alphabet+marks+digits
def decipherment(cipher_as_a_list, H):
    code= []
    for x in cipher_as_a_list:
        y= (int(x) + H) % 46
        code.append(y)
    return code  
def solution(full_list, a):
    result= []
    for i in a:
        s= full_list[i]
        result.append(s)
    return ''.join(result)
'''
we have a word and we want to cipher it in Cezar's cryptosystem.
'''
def reverse(full_list, word_to_cipher):
    lst= []
    for i in word_to_cipher:
        indices = [index for index, value in enumerate(full_list) if value == i]
        lst.extend(indices)
    return lst
def get_your_cipher(result_lst, k):
    cipher= []
    for x in result_lst:
        y= (x-k)%46
        cipher.append(y)
    return cipher
intro= input("What do you want to do? If deciphering write: D, if ciphering: C.")
if intro.upper()=="D":
    encrypted_data= input("Provide the cipher: ")
    cipher_as_a_list= encrypted_data.split(',')
    H= int(input("Provide the key: "))
    a= decipherment(cipher_as_a_list, H)
    print(solution(full_list, a))
elif intro.upper()=="C":
    print("Do you need to see a full_list to write the word you wanna cipher? Write Yes or No.")
    answer= input()
    if answer.lower()=="yes":
        print(full_list)
    elif answer.lower()=="no":
        pass
    else:
        print("Is it that hard for you to write one of the two above words? Now you cannot see the list LOL")
    try:
        k= int(input("Provide the key: "))
    except:
        print('Something went wrong')
        sys.exit()
    word_to_cipher1= input("Provide the word to cipher, separate them with a comma, but do not use a space (remember to use signs from full_list): ")
    if all(char in full_list for char in word_to_cipher1.split(',')):
        word_to_cipher = word_to_cipher1.split(',')
        result_lst = reverse(full_list, word_to_cipher)
        print(get_your_cipher(result_lst, k))
    else:
        print("Wtf read again")
else:
    print("You're dumb or what? Write D or C duh.")
