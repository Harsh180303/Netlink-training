# Convert all the capital letters to lower and vice versa in a string
'''
str = input("Enter a string in mixed case: ")
print("The swapped string is ", str.swapcase())
'''


# count the no of consonants, vowels and digits in the string entered by user
'''
str = input("Enter a string: ")

consonants = 0
digits = 0
vowels = 0

for letter in str:
    if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
        vowels +=1
    elif (letter.isdigit() ):
        digits +=1
    else:
        consonants+=1

print(f"no of vowels: {vowels}\nno of consonants: {consonants}\nno of digits: {digits}\n ")
'''

# WAP to count repeated characters in a string:
'''
my_str = input("Enter a string: ")

for letter in my_str:
    count = my_str.count(letter)
    print(f"{letter}: {count}")
'''

# Accept 2 strings from the user. Find out if the string1 is present in string2. if it is, remove all instances of string1 in string2 and create a new string

'''
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if string1 in string2:
    print("String1 is present in string2, now the new string is")
    new_str = string2.replace(string1, '')
    print(new_str)

else :
    print("String1 is not present in string2")
'''

# Replace all the digits in a string by #
'''
my_str = input("Enter a string (you can also enter digits in it): ")

for letter in my_str:
    if (letter.isdigit()):
        new_letter = letter.replace(letter, '#')
        print(new_letter, end='')
    else :
        print(letter, end="")
'''


# predict output:
'''
str1 = "aBC"
str2 = "ABC"
str3 = "abc"
str4 = "abcd"
str5 = "0abc"

print(str1 == str2)         # False
print(str1 > str2)          # True
print(str1 < str3)          # True
print(str3 > str4)          # False
print(str1 > str5)          # True
'''


# Caesar encryption

my_str = input("Enter a string: ")
key = int(input("Enter your encryption key: "))

encrypted_data = ''

for letter in my_str:
    if (letter.isalpha()):
        unicode_val = ord(letter)
        enc_letter = chr(unicode_val + key)
        encrypted_data += enc_letter
    else :
        encrypted_data += letter

print(encrypted_data)