# While loop

# Simple Intrest program for 5 customers
'''
i = 1
while (i <= 5):
    print(f"Simple Intrest for user {i}")
    principle = int(input("Enter the principle amount: "))
    rate = int(input("Enter the rate of intrest: "))
    time = int(input("Enter the time in months: "))

    SI = (principle * rate * time) / 100
    print(f"Simple intrest of customer {i} is: {SI}")
    print(f"Simple intrest of customer {i} is: {SI + principle}")
    i += 1
'''


# Sum of first 10 natural numbers:
'''
sum_of_num = 0
i = 1
while (i <= 10):
    sum_of_num += i
    i+=1

print(sum_of_num)
'''

# Reverse a number
'''
num = int(input("Enter a number: "))
rev = 0

while (num > 0):
    rem = num % 10
    rev = rev * 10 + rem 
    num //= 10

print(rev)
'''

# Enter a number to print it's table
'''
num = int(input("Enter a number to print it's table: "))
i = 1
while (i <= 10) :
    print(f"{num} * {i} = {num * i}")
    i+=1
'''