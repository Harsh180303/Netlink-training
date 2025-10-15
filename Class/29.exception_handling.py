# operator overloading
# types of inheritance
# Polymorphism

# ---------------------- Left before below topic -------------------------
'''
Python Exception handling: It is a process to handle run time exceptions.
using try - except - finally block.

Exceptions: It is a runtime error which dirupts the program execution in between. (Recoverable)

Error: Are not Recoverable condition.
Types of Errors:
--------------------------------
1. Syntactical Error: /, ()
2. Logical Error: i+=1 in looping, = instead of ==
3. Linker Error.
4. Run time error. (Exception): Which occured at runtime.

Reasons to occur run time Exception:
1. Divide by zero, nume/deno
2. ArrayIndex out of bound
3. FileNotFoundException

-------------------------------------------------------------
Reason behind using Exception Handling:
1. To avoid abnormal termination of your program.
2. To provide user friendly error messages.
3. Rest of the code should get executed.
--------------------------------------------------------------
1. try block: Is an error detector.
    Programmer should write the code in which possibilities of occuring Exception.

2. except block: Is an Exception Handler.
    Responsible to handle and exception and provide user friendly error message.

3. finally block: Is always executable block. For cleanup code or release resources.
'''

'''
# Need of exception handling
num = 4
print("hii")
print(num/0)
print('\n bye')
'''

# Using try - except block
'''
print("Welcome to Exception handling!!")
try:
    print(num)
except:
    print("Assign val to num!")

print("End")
'''

# try except finally block
'''
nume = int(input("Enter numerator value: "))
deno = int(input("Enter denominator value: "))
try:
    div = nume/deno
    print("\nDivision: ", div)
except:
    print("\nDenominator can't be zero!")
finally:
    print("\nPlease visit again.")
'''

# Multiple Except block with one try.
'''
try: 
    # x = int(input("Enter a value"))
    print(x)
except ValueError:
    print("Val must be a number.")
except:
    print("Something went wrong.")
finally:
    print("Happy Learning!")

'''

# One except block with multiple exceptions
'''
try:
    x = int(input("Enter a value: "))
    print(x)
except (ValueError, KeyError, NameError, ZeroDivisionError):
    print("Something went wrong!")
finally:
    print("Happy learning")
'''

# Multipy try and except blocks:
# try 1
try:
    nume = int(input("Enter numerator: "))
except ValueError:
    print("Numerator must be a number...")

# try 2
try: 
    deno = int(input("Enter denominator: "))
except ValueError:
    print("Denominator must be a number....")

# try 3
# try:
#     nume = int(input("Enter numertaor: "))
#     deno = int(input("Enter denominator: "))    
#     div = nume/deno

