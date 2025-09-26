# 1) Lambda Function
# 2) Recursion
# 3) Modules

# lamdba: A lambda function in python is a small. anonymous function defined wiht lambda keyword.

# unlike regular function defined using def, lamba functions are nameless and typicall used for short, single - expression operations.

# 1. Anonymous
# 2. single expression
# 3. Multiple Arguments
# 4. syntax: lambda args: Expression
# where lamda is a keyword
'''
s = lambda a,b : a + b # defining logic using lamda function
print(s(100, 200))
'''

# ====================================

# def cu(n):
#     cu = n**3
'''
cu = lambda n : n**3
print(cu(3))
print(type(cu))
'''

# max of 2 nums
'''
maximum = lambda a,b : max(a,b)
print(maximum(2,6))
'''

# square of nums
'''
'''

# pos neg
'''
sq = lambda num : print(f"{num} is positive") if num > 0 else print(f"{num} is negative")
print(sq(-1))
'''

# issue license
'''
issue = lambda age : print("Issue license") if age >= 18 else print("Not elegible")
issue(23)
'''

# odd even
'''
odd_even = lambda num : print(f'{num} is an even number') if num % 2 == 0 else print(f"{num} is an odd number")
odd_even(20)
'''
