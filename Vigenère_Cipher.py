
#Vigenère Cipher Program
#This function returns an alphabet where the start of the alphabet is the current letter of the input string
#An example would be the input word flank, the first letter of the alphabet would be 'f,g,h,i,j,k...etc,etc'
def modify_alphabet(shift_num):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    i = 0
    #this will shift letters from the front of the alphabet to the back while the index is less than the shift number
    while i < shift_num:
        i += 1
        cur_letter= alphabet[0]
        #pop and append are used to remove the first letter of the alphabet and add it to the end of the list
        #pop removes the first index(0) from the list, then append adds it to the end of the list
        #this will shift the letters in the alphabet by the shift number
        alphabet.pop(0)
        alphabet.append(cur_letter)
    return alphabet


#this function will return the index of the input letter in the alphabet, which can be used in the alt alphabet to 
#find the cipher letter
def find_key_index(key_char):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    if key_char in alphabet:
        key_char_index = alphabet.index(key_char)
        return int(key_char_index)
    else:
        return 'none'

#this is the function that will decrypt the string using the key
#the function will cycle though the possible alphabet arrangements(since there are only 26 possilities) and find the
#corresponding letter in the alphabet that matches the letter in the string, and return the first letter of the alphabet
#which will be the decrypted letter.
def decrypt(string, key):
    decrypt_text = ""
    key_index = 0

    #These will convert strings to lower case so that the program is not case sensitive
    string = string.lower()
    key = key.lower()

    alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
    #this will loop through the string and find the alphabet that was used to encrypt the string
    for char in string:
        #key_letter is used to keep track of the current key letter we are on
        key_letter = key[key_index]
        #will be used as the index of the key letter in the key word
        key_index+=1
        #if the key index is greater than the length of the key, it will reset to 0
        #this is used to cycle through the key letters
        if key_index >= len(key):
            key_index=0
        #this will find the index of the key letter in the alphabet
        key_char_index=find_key_index(key_letter)
        char_index = find_key_index(char)
        #if the char is 'none,' then the char is a special char and will remain the same
        if char_index != 'none':
            #Will loop though the alphabet and find the index of the letter in the alphabet when the cipher char matches
            #the char position
            for letter in alphabet_list:
                new_alphabet = modify_alphabet(find_key_index(letter))
                if new_alphabet[key_char_index] == char:
                    decrypt_text += new_alphabet[0]
        elif char_index == 'none':
            decrypt_text += " "
    return decrypt_text

def encrypt(string, key):
    #for first section, look at decrypt function for comments
    key = key.lower()
    string = string.lower()
    encrypted_string = ""
    
    key_index = 0
    for char in string:
        char = char.lower()
        key_letter = key[key_index]
        key_index += 1
        if key_index >= len(key):
            key_index = 0
        key_char_index=find_key_index(key_letter)
        char_index = find_key_index(char)
        #this function does not loop through alphabets, instead creates one and uses that to encrypt the string for each letter in the string
        if char_index != 'none':
            new_alphabet = modify_alphabet(char_index)
            encrypted_string += new_alphabet[key_char_index]
        elif char_index == 'none':
            encrypted_string += " "
    return encrypted_string


def main():
    #this is the main loop to ask if a person wants to encrypt/decrypt a string until then quit
    while True:
        user_desire = input("Please input '1' to encrypt or '2' to decrypt, or 'q' to quit: ")
        
        if user_desire == 'q':
            print("Thank you for your patronage!")
            #exit is similar to return 0, it will exit the program if you can believe it
            exit()
        elif user_desire == '1':
            user_string = input("Enter a string to encrypt: ")
            user_key = input("Enter a key: ")

            encrypted_string = encrypt(user_string, user_key)

            print("Encrypted string:", encrypted_string)
        elif user_desire == '2':
            user_string = input("Enter a string to decrypt: ")
            user_key = input("Enter Your Key: ")
            
            decrypted_string = decrypt(user_string,user_key)
            
            print("Decrypted string:", decrypted_string)
        

main()