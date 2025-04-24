
# Caesar Cipher Program
#Caesar cipher works by shifting the letters of the alphabet by a certain number of places.
#For example, if the shift is 3, then 'a' becomes 'd', 'b' becomes 'e', and so on.

#this function will cipher the string using the shift number
def cipher(message, shift):
    result = ("")

    for letter in message:
        #ensures letter is in fact a letter
        if letter.isalpha():
            #enures the shift_amount is under 26, so that it will not go out of bounds of the alphabet
            shift_amount = shift % 26
            if letter.islower():
                start = ord('a')
            else:
                start = ord('A')
            #this line is the main line that will shift the letter by using chr() and ord() to convert letters to numbers
            #the shifted character is equal to the letter (in it's ASCII value) - a (the start of the aphabet), then plus the shift to get the new letter
            #%26 means that the number will get subtracted by 26 if it is over 26 until it is under 26, then the final number is converted back into a letter
            #and added to the variable 'result', which is the encrypted word
            result += chr((ord(letter) - start + shift_amount) % 26 + start)
        else:
            result += letter

    return result
# This function will get the shift value and message from the user
# It will also check if the shift value is valid (1-25) and if the message is not empty and contains only letters.
def get_shift_and_message(decrypt):
    while True:
        message = input("Please enter the message you want to encrypt or decrypt: ")
        shift = input("Please enter the shift value (1-25): ")
        if not shift.isdigit() or not (1 <= int(shift) <= 25) and message.isalpha() and len(message) > 0:
            print("Invalid shift value. Please enter a number between 1 and 25.")
            continue
        else:
            break

    if decrypt:
        #for this program, it will only shift in one direction, so to reverse the shift, we just need to reverse which direction we encrypt in
        return cipher(message, -int(shift))
    else:
        return cipher(message, int(shift))


# This function will run the main loop of the program
# It will ask the user if they want to encrypt or decrypt a message and call the get_shift_and_message function accordingly.
def main():
    while True:
        cipher_result = ""
        while True:
            user_option = input("Please Choose to encrypt or decrypt a message (1 or 2) or enter 'exit' to exit: ")
            if user_option == "1":
                decrypt = False
                cipher_result = get_shift_and_message(decrypt)

                print("Ciphered message: ", cipher_result + "\n\n")
                break
            elif user_option == "2":
                #will keep track of whether the user wants to decrypt or not
                decrypt = True
                cipher_result = get_shift_and_message(decrypt)
                print("Decrypted message: ", cipher_result + "\n\n")
                break
            elif user_option.lower() == "exit":
                print("Thank you for using the Caesar Cipher program!")
                #return 0 means the program ends with no errors in the program
                return 0
            else:
                print("Invalid option. Please enter 1, 2, or exit.")
                continue
    
main()