# Palindrome
'''
num = int(input("Enter a number: "))
original_num = num

rev = 0
while (num > 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

if rev == original_num :
    print("It is a palindrome number.")
else :
    print("It is not a palindrome number.")
'''

# Sum of first n natural nums
'''
n = int(input("Enter the nth number: "))
i = 1
sum_of_nums = 0
while (n >= i):
    sum_of_nums += i
    i+=1

print(f"Sum of first {n} natural number is {sum_of_nums}")
'''


# Reverse a number
'''
num = int(input("Enter a number: "))
original_num = num

rev = 0
while (num > 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

print(f"Reverse of {num} is {rev}")
'''

# WAP to print a menu to accept the option from the user.
    # Accept a name and print a message
    # Accept a number less than 10 and print all numbers less than 50 But. "Fizz" for every multiple of the number.
'''
name = input("What is your name? ")
num = int(input(f"Hello {name}! Please choose a number between 1 to 10: "))
i = 1
while (i <= 50 ):
    if (i % num == 0) :
        print("Fizz", end=" ")
    else :
        print(i, end=" ")
    i+=1
'''

# WAP to find the sum of this sequence where n is a positive integer and input by user x = x^2/2 + x^3/3 + x^4/4....x^n/n
'''
n = int(input("Enter a number: "))
x = int(input("Enter the val of x: "))

s = 0
for i in range(2, n+1):
    s+= x**i/i

print(s)
'''


# WAP to find perfect numbers within a range. Perfect numbers are those whose sum of its factors is same as the number. Eg: 6, 28, 496 etc.
'''
start = int(input("Enter the starting number of the range: "))
stop = int(input("Enter the end number of the range: "))

num = 1
for i in range(start, stop+1):
    divisor_sum = 0
    for j in range(1, i):
        if (i % j == 0):
            divisor_sum += j

    if (divisor_sum == i):
        print(i, end=" ")
'''


# Armstrong
'''
num = int(input("Enter a number: "))
original_num = num
power_of_num = 0
for i in str(num):
    power_of_num +=1

# print(power_of_num)

sum_of_dig = 0
for i in range(0, power_of_num):
    rem = num % 10
    sum_of_dig += rem**power_of_num
    num //= 10

if (sum_of_dig == original_num):
    print(original_num, "is a armstrong number")
else :
    print(original_num, "is not a armstrong number")

'''