# Python Exercises on Tuple

# 1. Repeat the below tuple three times.
# Given:
# original_tuple = ('a', 'b')
# Expected Output:
# ('a', 'b', 'a', 'b', 'a', 'b')
'''
original_tuple = ('a', 'b')
new_tuple = original_tuple * 3
print(new_tuple)
'''


# 2.Slice below tuple to get elements from the 4th to the 7th position.
# Given:
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Expected Output:
# (4, 5, 6, 7)
'''
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sliced_nums = numbers[3:7]
print(sliced_nums)
'''

# 3.Reverse the tuple
# Given:
# tuple1 = (10, 20, 30, 40, 50)
# Expected output:
# (50, 40, 30, 20, 10)
# Solution: 
# tuple1 = (10, 20, 30, 40, 50)
# tuple1 = tuple1[::-1]
# print(tuple1)
'''
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)
'''


# 4.Write a code to access and print value 20 from given nested tuple.
# Given:
# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# Expected output:
# 20
'''
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])
'''


# 5. Write a code to unpack the following tuple into four variables and display each variable.
# Given:
# tuple1 = (10, 20, 30, 40)
# Expected output:

# # Your code
# print(a) # should print 10
# print(b) # should print 20
# print(c) # should print [30,40]
'''
tuple1 = (10, 20, 30, 40)
a,b,*c = tuple1
print(a) # should print 10
print(b) # should print 20
print(c) # should print [30,40]
'''


# 6. Swap two tuples in Python
# Given:
# tuple1 = (11, 22)
# tuple2 = (99, 88)
# Expected output:
# tuple1: (99, 88)
# tuple2: (11, 22)
'''
tuple1 = (11, 22)
tuple2 = (99, 88)
list1 = list(tuple1)
list2 = list(tuple2)
tuple1 = tuple(list2)
tuple2 = tuple(list1)

print(tuple1)
print(tuple2)
'''

            # Method 2 -------------- tuple unpacking
'''
tuple1 = (11, 22)
tuple2 = (99, 88)
# tuple1, tuple2 = tuple2, tuple1
# or
tuple1, tuple2 = (99, 88), (11, 22)

print(tuple1)
print(tuple2)
'''


# 7. Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
# Given:
# tuple1 = (11, 22, 33, 44, 55, 66)
# Expected output:
# tuple2: (44, 55)
'''
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3], tuple1[4]
print(tuple2)
'''
                # Method 2
'''
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:5]
print(tuple2)
'''


# 8. Write a function get_min_max(numbers) that takes a list of numbers and returns a tuple containing the minimum and maximum number.
# Given:
# def get_min_max(numbers):
#     # Write your code here

# # Test the function
# my_numbers = [10, 5, 20, 2, 15]
# min_max_values = get_min_max(my_numbers)
# print(f"Original numbers: {my_numbers}")
# print(f"Minimum and maximum values: {min_max_values}")
# Expected Output:
# Original numbers: [10, 5, 20, 2, 15]
# Minimum and maximum values: (2, 20)
'''
def get_min_max(numbers):
    my_tuple = ()
    my_tuple = my_tuple + (min(numbers),)
    my_tuple = my_tuple + (max(numbers),)
    return my_tuple

my_numbers = [10, 5, 20, 2, 15]
print(f"Original numbers: {my_numbers}")

min_max_values = get_min_max(my_numbers)
print(f"Minimum and maximum values: {min_max_values}")
'''


# 9. Compare two tuples and find out which one is “greater” and why?
# Given:
# t1 = (1, 2, 3)
# t2 = (1, 2, 4)
# Expected Output:
# Tuple 1: (1, 2, 3)
# Tuple 2: (1, 2, 4)
# (1, 2, 3) is less than (1, 2, 4)
'''
t1 = (1, 2, 3)
t2 = (1, 2, 4)

if (t1 > t2):
    print(f"{t1} is grater than {t2}")
else:
    print(f"{t1} is less than {t2}")
'''

# Exercise 10: Function Returning Tuple
# Write a function get_min_max(numbers) that takes a list of numbers and returns a tuple containing the minimum and maximum number.
# Given:
# def get_min_max(numbers):
#     # Write your code here

# # Test the function
# my_numbers = [10, 5, 20, 2, 15]
# min_max_values = get_min_max(my_numbers)
# print(f"Original numbers: {my_numbers}")
# print(f"Minimum and maximum values: {min_max_values}")
# Expected Output:
# Original numbers: [10, 5, 20, 2, 15]
# Minimum and maximum values: (2, 20)

'''
SAME QUESTION AS 8 SO, IT'S ALREADY SOLVED...
'''