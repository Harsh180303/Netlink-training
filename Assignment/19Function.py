# 1) Write a menu based program which accepts a string and does the followeing:
# Return the number of capital letters, vowels, numbers and special characters.
'''
def segrigate(str):
    no_cap = 0
    vowels = 0
    num = 0
    special = 0
    for letter in str:
        if letter.isdigit():
            num +=1
        elif (ord(letter) >= 65 and ord(letter) <= 90):
            no_cap +=1
        elif letter.isalpha():
            if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
                vowels +=1
        else:
            special +=1
    return no_cap, vowels, num, special


str = input("Enter a string: ")
data = segrigate(str)
capital, vowels, numbers, special_chars = data
print(f"Capital letters = {capital}\nVowels = {vowels}\nNumbers = {numbers}\nSpecial Characters = {special_chars}")
'''

# 2) Check whether the given string is palindrome or not.
'''
def checkPalindrome(str1):
    rev = []
    for char in str1:
        rev.insert(0,char)
    return rev

str1 = input("Enter string: ")
reverseList = checkPalindrome(str1)
# print(reverseList)
my_str = ''

for val in reverseList:
    my_str += val

if (my_str == str1):
    print(f"{str1} is palindrome")
else :
    print(f"{str1} is not a palindrome")
'''


# 3) Write a function using the positional args that converts the temperature in celesius to that fahreneit.
'''
def Convert_fahreneit(cele):
    fahreneit = cele * 1.8 + 32
    return fahreneit
    
celesius = int(input("Enter temperature in celecius: "))
print(f"{celesius} degree celesius = {Convert_fahreneit(celesius)} degree fahreneit")
'''

# 4) Write a program to print the following menu: 
# 1. Prime  2.  Perfect 3. Twin Prime   4. Exit
# For options a and b, accept a number and check if the given number is prime or perfect. For option c, accept a number and generate a list of twin primes (less than the given number) where each pair is a tuple. You can use the function written for option a. Write separate function for each.

def checkPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if (num % i == 0):
            return False
    else :
        return True

def checkPerfect(num):
    mul = 0
    for i in range(1, num // 2 + 1):
        if (num % i == 0):
            mul += i
    if mul == num:
        return True
    return False

def TwinPrime(num):
    twim_prime_list = []
    for i in range(2, num):
        if (checkPrime(i) and checkPrime(i + 2)):
            tpl = (i, i+2)
            twim_prime_list.append(tpl)
    return twim_prime_list


should_continue = True
while (should_continue):
    print(f"\n1. Prime\n2. Perfect\n3. Twin Prime\n4. Exit")
    menu = int(input("Enter your choice (Type integer value): "))
    if menu == 1:
        num = int(input("Enter a number to check: "))
        if (checkPrime(num)):
            print(f"{num} is a Prime number.")
        else :
            print(f"{num} is not a Prime number.")

    elif menu == 2:
        num = int(input("Enter a number to check: "))
        if (checkPerfect(num)):
            print(f"{num} is a Perfect number")
        else:
            print(f"{num} is not a Perfect number")

    elif menu == 3:
        num = int(input("Enter number upto which you want to check: "))
        twin = TwinPrime(num)
        if (twin):
            print(f"Twin = {twin}")
        else :
            print(f"No Twim prime found until {num}")

    elif menu == 4:
        print("Gracefully exiting the program...")
        should_continue = False

    else :
        print("Please enter valid input.")