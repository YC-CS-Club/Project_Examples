# an alternative implementation using the build in chr() and ord() functions of python; a naive implementation is
# really simple, but doesn't account for control characters and white space winding up being used with the entered
# offset value, so I had to integrate some error checking and that was tricky.

# TODO: error check decryption process for values that yield unprintable results... which we shouldn't have,
# because the encryption process prevents them from being created in the first place, but we should check for
# anyway.

import unicodedata

char_value_min = 0
char_value_max = 1114111

def get_offset_value():
    
    try:
        checked_key = int(input("Enter offset (any whole number greater than 0 and less than 1,114,111): "))
    except ValueError:
        print('Please enter an integer value.')
        return get_offset_value()
    else:
        # if key is equal to char_value_min or char_value_max, we're not shifting anything
        if checked_key <= char_value_min or checked_key >= char_value_max:
            print ('Please enter a whole number greater than 0 and less than 1,114,111.')
            return get_offset_value()
        else:
            return checked_key
        
def check_shifted_value_in_range(value_to_check):
    
    if value_to_check > char_value_max:
        return False
    else:
        return True
    
# check for control characters or white space (other than blank spaces)
def is_not_printable(value_to_check):

    # unicode decinmal value for regular space, U+0020
    if value_to_check == 32:
        return False
    elif unicodedata.category(chr(value_to_check)) == 'Cc' or str.isspace(chr(value_to_check)):
        return True
    else:
        return False

# check to see if the encrypted message winds up using unprintable characters or undesired whitespace
def is_message_encryptable_with_key(message, offset):
    
    is_encryptable = True
    
    for char in message:
    
        shifted_value = ord(char) + offset
     
        if not check_shifted_value_in_range(shifted_value):
            shifted_value = shifted_value - char_value_max
            
        if is_not_printable(shifted_value):
            is_encryptable = False
    
    return is_encryptable

def get_message_to_encrypt():
        
    original_message = input("Enter message to be encrypted using a Caesar cipher: ")
    
    # i can't figure out how to enter a "tab", so I'm not sure this is even needed
    if not is_message_encryptable_with_key(original_message, 0):
        print ("Please only enter printable characters and spaces, no control characters or other whitespace.")
        get_message_to_encrypt()

    key = get_offset_value()
    
    # dynamically adjust the offset value so that it doesn't produce unuseable output
    while not is_message_encryptable_with_key(original_message, key):
        key += 1
    
    print ("Original offset yields unprintable output, new offset is:", key)

    print ("Encrypted message: ", end="")

    for char in original_message:
        
        shifted_value = ord(char) + key
     
        if not check_shifted_value_in_range(shifted_value):
            shifted_value = shifted_value - char_value_max

        print (chr(shifted_value), end="")
    
def get_message_to_decrypt():
        
    original_message = input("Enter message using a Caesar cipher to be decrypted: ")

    key = get_offset_value()

    print ("Decrypted message: ", end="")

    for char in original_message:
        
        shifted_value = ord(char) - key
     
        if not check_shifted_value_in_range(shifted_value):
            shifted_value = shifted_value + char_value_max
            
        print (chr(shifted_value), end="")

def get_choice():
    
    value = input("Enter 'encrypt' or 'decrypt' to process a message: ")
    value = value.lower()

    if value not in ('encrypt', 'decrypt'):
        print ("Please enter only 'encrypt' or 'decrypt'")
        return get_choice()
    else:
        return value

# main

choice = get_choice()

if choice == 'encrypt':
    get_message_to_encrypt()
if choice == 'decrypt':
    get_message_to_decrypt()

    
