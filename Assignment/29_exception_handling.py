# 1.	Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

# num = int(input("Enter a number"))
# if not num.is_digit():
#     raise Exception("this is a value error")
# else:
#     print(num)

'''
try:
    num = int(input("Enter a number"))
except:
    print("something went wrong.")
'''

# 2. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
'''
num = int(input("Enter no. of ele u want in a list: "))
lst = []
for i in range(-2, num):
    n = int(input("Enter a number: "))
    lst.append(n)

print(f"Your list is: {lst}")
num = int(input("Enter index number: "))
try:
    lst[num]
    print(lst[num])
except IndexError:
    print("Array limit exceeded....")
'''

# 3. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
# exception AttributeError:
# Raised when an attribute reference (see Attribute references) or assignment fails. (When an object does not support attribute references or attribute assignments at all, TypeError is raised.)
'''
try:
    a = int(input("Enter a number: "))
    a.append()
except AttributeError:
    print(f"{type(a)} does not support append")
except ValueError:
    print(f"Please enter only integer value")
'''


# 4. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
'''
try:
    name = input("Enter file path or name (if it is in current directory): ")
    fob = open(name)
    print(fob)
except FileNotFoundError:
    print(f"no such file named as {name}")
'''

# 5. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
'''
try:
    num1 = input("Enter number 1: ")
    num2 = input("Enter number 2: ")
    if not (num1.isdigit() and num2.isdigit()):
        raise TypeError("Inputs can only be numbers (like 1 or -5 etc.)")

except TypeError as err:
    print(err)
'''