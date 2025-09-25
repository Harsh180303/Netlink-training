# Slicing is must

# Quiz Question
'''
a = ['abc', 'def', 'ghi']
b = a
print(id(a))
print(id(b))
b.pop(1)
print(a)
'''


# Accept a list of integers and segregate them as odd and even list.
'''
my_list = []

n = int(input("How many numbers do you want in your list? "))
i = 1
while(n >= i):
    num = int(input(f"Element no. {i}: "))
    my_list.append(num)
    i+=1

print(f"My list is: {my_list}")

odd_list = []
even_list = []

for item in my_list:
    if (item % 2 == 0):
        even_list.append(item)
    else :
        odd_list.append(item)

print(f"Odd list is : {odd_list}")
print(f"Even list is : {even_list}")
'''

# Accept a list of numbers and strings. Convert the numbers to its square and strings to its upper case.
'''
my_list = input("Enter items: ").split()
print(f"Original list {my_list}")

new_list = []

for list_item in my_list:
    if (list_item.isdigit()):
        list_item = int(list_item) ** 2
        new_list.append(list_item)
    else :
        list_item = list_item.upper()
        new_list.append(list_item)
    
print(new_list)
'''

# Accept 2 lists in ascending order. WAP to merge the 2 list. The resultant list should also be in ascending order.
'''
list1 = []
list2 = []

n = int(input("How many elements do you want in your list1: "))

for i in range(n):
    num = int(input(f"Enter ele {i+1}: "))
    list1.append(num)


n2 = int(input("How many elements do you want in your list2: "))
for i in range(n2):
    num = int(input(f"Enter ele {i+1}: "))
    list2.append(num)

list1.sort(reverse=False)
list2.sort(reverse=False)

print(list1)
print(list2)

list1.extend(list2)
print(f"Resultantant is {list1}")

list1.sort(reverse=False)
print(list1)
'''

# Accept a list of integers and swap the first half of numbers with it's second half.
'''
list_of_int = []
n = int(input("Enter the no of elements in your list: "))
half_n = n // 2
for i in range(n):
    num = int(input(f"Enter ele no. {i+1}: "))
    list_of_int.append(num)

print(f"Before swapping: {list_of_int}")

for i in range(half_n):
    popped = list_of_int.pop()
    list_of_int.insert(0, popped)

print(f"After swapping: {list_of_int}")
''' 


# Accept a list of integers and a number n. Perform the rotation of elements in the list n times.
'''
list1 = []
no_of_ele = int(input("How many elements do you want in your list: "))
n = int(input("Enter a number: "))

for i in range(no_of_ele):
    num = int(input(f"Enter ele no. {i+1}: "))
    list1.append(num)

print(f"Actual list is: {list1}")

for i in range(n):
    popped = list1.pop()
    list1.insert(0, popped)

print(f"Rotated list by {n} is: {list1}")
'''

# Accept a matrix and calc sum row wise.
'''
row = int(input('Enter the number of rows: '))
col = int(input('Enter the number of cols: '))

matrix = []

for i in range(row):
    elements = []
    for j in range(col):
        num = int(input(f"Enter {j+1} element of row {i+1}: "))
        elements.append(num)
    matrix.append(elements)

print(matrix)

# now calculating the sum of each row
for i in range(row):
    s = 0
    for i in matrix[i]:
        s += i
    print(f"Sum of elements of row {i} is: {s}")
'''

# Accept a matrix and calculate the product of the primary diagonal numbers.
'''
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of cols: "))

matrix = []

for i in range(row):
    row_ele = []
    for j in range(col):
        num = int(input(f"Enter element {j+1} of row {i+1}: "))
        row_ele.append(num)
    
    matrix.append(row_ele)

print(matrix)

# now, calc. the product of primary diagonal numbers.
prod = 1
for i in range(row):
    for j in range(col):
        if (i == j):
            prod = prod * matrix[i][j]

print(prod)
'''

'''
a = ['ab', 'cde', ['ghi']]
b = a[:]
print(f"a is: {a}")
print(f"b is: {b}")
a[2][0] = 'jkh'
a[1] = 'mno'
print(f"now, a is {a}")
print(f"now, b is {b}")
'''