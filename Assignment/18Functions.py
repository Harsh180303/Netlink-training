# WAP to define a method named student with 3 parameters name, id, course to display all details 
'''
def student(name, id, course):
    print(f"I'm {name}, my id is {id}, and my course is {course}")

name = input("Enter your name: ")
id = int(input("Enter your id: "))
course = input("Please enter your course name: ")

student(name, id, course)
'''

# add(n1, n2, n3, n4, n5)
'''
def add(n1, n2, n3, n4, n5):
    return n1+n2+n3+n4+n5

n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
n3 = int(input("Enter n3: "))
n4 = int(input("Enter n4: "))
n5 = int(input("Enter n5: "))

print(add(n1, n2, n3, n4, n5))
'''

# Swap (n1, n2) for swapping 2 numbers.
'''
def swap(n1, n2):
    temp = n1
    n1 = n2
    n2 = temp
    print(f"Val of first no. is {n1} and second no. is {n2}")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

swap(num1, num2)
'''

# factorial function(num)
'''
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    print(fact)

num = int(input("Enter a number to check it's factorial. "))
factorial(num)
'''

# fibonacci(no_of_terms)
'''
def fibonacci(num):
    a = -1
    b = 1
    for i in range(num):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

num = int(input("Enter number of terms of fibonacci series: "))
fibonacci(num)
'''

# prime(num)
'''
def prime(num):
    for i in range(2, num):
        if (num % i == 0):
            print("It is not a prime number ")
            break
    else:
        print(f"{num} is a prime number")

num = int(input("Enter a number to check if it is prime or not: "))
prime(num)
'''

# armstrong(num)
'''
def armstrong(num):
    og_num = num
    power = 0
    for i in str(num):
        power += 1

    s = 0
    while(num > 0):
        last_digit = num % 10
        s = s + last_digit**power
        num = num // 10

    if (og_num == s):
        print(f"{og_num} is an armstrong number.")
    else :
        print(f"{og_num} is not an armstrong number.")


num = int(input("Enter a number to check if it is armstrong number or not: "))
armstrong(num)
'''