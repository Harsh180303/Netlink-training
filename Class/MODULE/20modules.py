# Module -------- 
# It is a pyhton file only which contains set of functions .
# To achieve readability
# Modularity
# Global access when dealing with large applications.
# flexibility
# Saperation of consern
# Avoid redundancy

# Types: 1. butil-in            2. User Defined 

# Create a normal python file with .py extension then we will have to inclde it in our main.py file by using import keyword followed with module name.

# module name will be module's file name.


# Method 1
'''
import Calculator
print('Additon of numbers: ', Calculator.add(50, 60))
'''

# Method 2
# if you want only few of your functions from a module 
'''
from Calculator import mul
print("Additon of nums: ", mul(2, 9) )
'''

# Method 3
# import whole and reducing the use of module name everytime
'''
from Calculator import*
print(f"Division of nums : {divide(9, 3)}")
'''

# Method 4 to import a module
import platform as platf