# WAP to create a tuple by using user input using a while/for loop.
'''
num = int(input("How many elements do you want in your tuple? "))
my_list = [input("Enter the element: ") for i in range(num)]
print(f"List is {my_list}")
my_tuple = tuple(my_list)
print(f"Tuple is {my_tuple}")
'''

# Create two tuples of numbers. Pick only even numbers from both tuples to form a third one.
'''
tuple1 = (1, 2, 4, 5, 3)
tuple2 = (11, 54, 23,56, 3)
print(f"First tuple: {tuple1}")
print(f"Second tuple: {tuple2}")

list1 = list(tuple1)
list2 = list(tuple2)
# print(f"First list: {list1}")
# print(f"Second list: {list2}")

list1.extend(list2)
even_list = [val for val in list1 if val % 2 == 0]
print(even_list)
'''

# Accept a matrix tuple and find the sum column wise.

row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))

matrix = [[int(input(f"Enter element {j+1} for row {i+1}: ")) for j in range(col)]
          for i in range(row)
          ]

print(matrix)

for j in range(col):
    s = 0
    for i in range(row):
        s += matrix[i][j]
    print(f"Sum of col {j+1} is {s}")


# It is according to the sum of row wise...

for i in range(row):
    sum_of_row = sum(matrix[i])
    print(f"sum of row {i+1} is {sum_of_row}")


# Accept a nested tuple and find the sum of all the numbers in it.
'''
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
s = 0
matrix = [[int(input(f"Eneter ele {i+1} of row {j+1}: ")) for i in range(col)]
          for j in range(row)
          ]

print(matrix)

nested_tuple = tuple(tuple(row) for row in matrix)
print(nested_tuple)

total_sum = sum(sum(r) for r in nested_tuple)
print(total_sum)
'''

# Create a nested tuple to store roll number, name and marks of n students. Find the student name with max marks.
'''
students = int(input("Enter the number of students: "))
students_list = []

for i in range(students):
    each_student = []
    name = input(f"Enter name of student {i+1}: ")
    roll_no = int(input(f"Roll no. of {name}: "))
    marks = int(input(f"Enter the marks of {name}: "))
    each_student.append(roll_no)
    each_student.append(name)
    each_student.append(marks)

    students_list.append(each_student)

print(students_list)

students_tuple = tuple(tuple(r) for r in students_list)
print(students_tuple)

max_marks = -1
topper_name = ""
for student in students_tuple:
    if (student[2] > max_marks):
        topper_name = student[1]
        max_marks = student[2]

print(f"{topper_name} got highest marsk {max_marks}")
'''

    
# Accept two tuples of numbers and create a new one with unique elements from both.
'''
ele_of_list1 = int(input("Enter number of ele. in first tuple: "))
list1 = [int(input(f"Enter ele {i+1} of tuple 1: ")) for i in range(ele_of_list1)]

ele_of_list2 = int(input("Enter number of ele. in second tuple: "))
list2 = [int(input(f"Enter ele {i+1} of tuple 2: ")) for i in range(ele_of_list2)]

tuple1 = tuple(list1)
tuple2 = tuple(list2)

print(tuple1)
print(tuple2)

full_tuple = tuple1 + tuple2
print(full_tuple)

unique_tuple = tuple(val for val in full_tuple if (full_tuple.count(val) == 1))
print(unique_tuple)
'''


# slicing, with both pos and neg indexing + built in methods
# how can we manage to mutate tuple this is important!!!!!!!!!!!


# list comprihension ka use karke ek matrix ke primary diagonals ka product aur each row ka sum print karwana hai.