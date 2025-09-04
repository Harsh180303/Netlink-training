# Checking if a character is an alphabet or number or a special character based on unicode value

character = input("Enter any character: ")

if (( ord(character) <= 90 and ord(character) >= 65) or (ord(character) <= 122 and ord(character) >= 97)):
    print("It is an alphabet")
elif (ord(character) >= 48 and ord(character) <= 57) :
    print("It is a number")
else :
    print("It is a special charactor")