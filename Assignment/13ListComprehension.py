# List comprehension

# Q1 Creating a list of n natural numbers.
'''
n = int(input("Enter a number: "))

natural_list = [i for i in range(1, n+1)]
print(natural_list)
'''

# Q2 Creating a list of squares.
'''
numbers = [1, 2, 3, 4, 5, 6, 7]
sqList = [num**2 for num in numbers]
print(sqList)
'''

# Q3 Creating even list and odd list
'''
numbers = [10, 11, 12, 13, 14, 15]
print(f"Original list: ", numbers)
even = [val for val in numbers if val % 2 == 0]
odd = [val for val in numbers if val % 2 != 0]
print(f"Odd number's list is {odd}")
print(f"Even number's list is {even}")
'''


# WAP to create a list displaying positive and negative.
# input: numbers = [10, -11, 12, 14, -15]
'''
numbers = [10, -11, 12, 14, -15]
pos_neg = ['positive' if i >= 0 else 'negative' for i in numbers ]
print(numbers)
print(pos_neg)
'''

# Flattening the list
'''
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten_list = [col for row in matrix for col in row]
print(matrix)
print(flatten_list)
'''

# Nested for loop
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
'''
quadrent = [(x,y) for x in range(3) for y in range(3)]
print(quadrent)
'''
