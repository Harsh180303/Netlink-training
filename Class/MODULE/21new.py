# import sys






# Built in modules: Already defined in python standard library.
# package > library > module

# platform module: used to get hte platform at which your application is running.
# system(): used to get hte platform at which your application is running.

# Method 4 to import a module and provide an alias or a short name to access that module.
'''
import platform as platf
print("Platfrom module", platf.platform())
print("Platfrom module", platf.system())
'''

# ====================================================

# math module: To perform more mathematical operations.

# some methods are :
# sqrt(): to find squrare root of a given number and return a float value
'''
import math
num = int(input("Enter a number to find sqrt: "))
print(math.sqrt(num))
'''

# ceil(): round up of the given number to it's higher integer value (upward)
'''
import math
num = float(input('Enter a float value: '))
print(math.ceil(num))
'''

# floor(): round up of the given number to it's lower integer value (downward)
'''
import math
num = float(input('Enter a float value: '))
print(math.floor(num))
'''

# random(): return a random outupt according to the given arguments: 
# choice(): 
'''
import random
L = ["Python", "Java", "Ruby", "Cpp"]
print("Your choise is:", random.choice(L))
'''

'''
import math
r = int(input("Enter radius: "))
print(f"area of circle: {math.pi * r * r}")
'''

'''
import math
num = float(input("Enter float number: "))
print(math.trunc(num))
'''

# datetime module
'''
import datetime
print(datetime.datetime.now())
'''

# Functions -> modules -> library -> Packages. 

# funcitons: collection of instructions
# modules: collection of function
# library: collection of modules
# packages: collection of library


# library ------ types 1) standard library    2) other libraries 

            ## Other libraries ----------
# data science (numpy, pandas)
# data visualization ------- (matplotib, plotly)
# Tkinter, turtle (for gui)
# scipy,