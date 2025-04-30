# build list of character values to exclude from output

import unicodedata

char_value_min = 0
char_value_max = 1114111

unprintable = []

for i in range (char_value_min, char_value_max + 1):
    # unicode decinmal value for regular space, U+0020, which we don't want to exclude
    if i == 32:
        next
    elif str.isspace(chr(i)) or unicodedata.category(chr(i)) == 'Cc':
        unprintable.append(i)
        
print (unprintable)