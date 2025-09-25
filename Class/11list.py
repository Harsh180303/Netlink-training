# LIst : It is one of the data type use to store collection of elements of similar (Homogenious) or disimilar (Heterogenious) types of data in one variable.

# It is indexed collection.[starts storing from zeroth index]
# It is represented by squeare braces[] subscript operator.
# It is mutable that means it's elements can be changeable.
# It is ordered collection.
# It allows duplicate elements.

Student_marks = [10, 20, 30, 40, 50] 
print(f"Similar list element: ", Student_marks)

print("First element: ", Student_marks[0])

# Dissimilar list

Student_data = ["Harsh", 18, {"age": 22}, True]
print(f"Dissimilar elements list: ", Student_data)

# Mutable list

L = [88, 22, 35, 46, 65]
L[3] = 87

print(f"updated list", L)

# Buit in methods
# append(): used to add an element at the end of the list

L.append(33)
print("An element append in the list:", L)

# How to delete elements in a list
# 2 ways: index and built in method 

# del L[3]

# L.pop(3)

# del L


print(L)

# clear, pop, popindex, list comprehension, 

# EmptyList
'''
empty_list = []
print(empty_list)

for i in range(1, 6):
    ele = input("Enter element: ")
    empty_list.append(ele)

print("Created list: ", empty_list)
'''

# Nesting of list:

nested_list = [1, 2, 3, [100, 200, 300]]

print("nested list: ", nested_list)

print(nested_list[0])
print(nested_list[1])
print(nested_list[2])
print(nested_list[3])
print(nested_list[3][0])
print(nested_list[3][1])
print(nested_list[3][2])

nested_list2 = [1, 2, 3, ['ABC']]

print(nested_list2[3][0])
print(nested_list2[3][0][0])
print(nested_list2[3][0][1])


# slicing and negative indexing

