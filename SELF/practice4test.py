# fibonacci 
# armstrong
# WAP to find perfect numbers within a range. Perfect numbers are those whose sum of its factors is same as the number. Eg: 6, 28, 496 etc.
# WAP to find the sum of this sequence where n is a positive integer and input by user x = x^2/2 + x^3/3 + x^4/4....x^n/n
# WAP to print a menu to accept the option from the user.
    # Accept a name and print a message
    # Accept a number less than 10 and print all numbers less than 50 But. "Fizz" for every multiple of the number.
# Reverse a number
# Sum of n natural numbers
# palindrome
# pattern - 
    # pyramid
    # inverted pyramid
    # right angled triangle
    # inverted right angled triangle
    # A BB CCC DDDD
    # Simple intrest


# fibonacci Series
# 0 1 1 2 3 5 8 13
'''
number = int(input("Enter a number: "))

a = -1
b = 1

for i in range(0, number):
    c = a + b
    print(c, end=" ")
    a = b
    b = c
'''

# armstrong number
'''
num = int(input("Enter a number: "))
original_num = num

power = 0
for i in str(num):
    power += 1

total = 0
while (num > 0):
    last_digit = num % 10
    total += last_digit ** power
    num //= 10
    
if (total == original_num):
    print("Armstrong.")
else:
    print("Not armstrong.")
    print(total)
'''

# WAP to find the sum of this sequence where n is a positive integer and input by user x = x^2/2 + x^3/3 + x^4/4....x^n/n
'''
n = int(input("Enter a positive integer: "))
x = int(input("Enter value of x: "))

s = 0

for i in range(2, n+1):
    s += x**i/i

print(s)
'''

# WAP to print a menu to accept the option from the user.
    # Accept a name and print a message
    # Accept a number less than 10 and print all numbers less than 50 But. "Fizz" for every multiple of the number.
'''
name = input("What's your name: ")
num = int(input(f"Hi {name}! can you please enter a number less than 10: "))

for i in range(1, 51):
    if (i % num == 0):
        print("Fizz")
    else:
        print(i)
'''

# Reverse a number
'''
num = 123456
rev = 0

while(num > 0):
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10

print(rev)
'''

# Palindrome
'''
num = 100
og_num = num
rev = 0

while(num > 0):
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10

if (og_num == rev) :
    print("Palindrome.")
else:
    print("Not a Palindrome.")
'''


# pyramid
#     *
#    ***
#   *****
#  *******
# *********

for i in range(0, 5):
    for j in range(0, 3-i+1):
        print(" ", end=' ')
    for k in range(2*i+1):
        print("*", end=" ")
    print()


print("INVERSE")

for i in range(5, 0, -1):
    for j in range(5-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()


# WAP to find perfect numbers within a range. Perfect numbers are those whose sum of its factors is same as the number. Eg: 6, 28, 496 etc.
'''
start = int(input("Enter start no: "))
end = int(input("Enter end no: "))

for num in range(start, end + 1):
    divisor_sum = 0
    for i in range():
        pass
'''

start = int(input("Enter start num: "))
stop = int(input("Enter stop num: "))

for num in range(start, stop + 1):
    divisor_sum = 0
    for i in range(1, num // 2 + 1):
        if (num % i == 0):
            divisor_sum += i
    if divisor_sum == num and divisor_sum != 0:
            print(num, "is a perfect no. ")