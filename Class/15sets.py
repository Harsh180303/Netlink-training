# SETS

'''
set1 = {"apple", 1, 2, "mango"}
print(set1)
'''

'''
set1 = {"apple", 1, 2, "mango", "mango"}
print(set1)
# print(set1[0])   # 'set' object is not subscriptable
'''

# with mixed elements
'''
s = {12.5, 1255, 5+6, True, 5+6j}
print("Set with mixed types of ele ", s)
'''

# It is immutable
'''
s = {11, 22, 33, 44,55}
s[1] = 30
# print(s)   # TypeError: 'set' object does not support item assignment
'''

# We can add or remove elements of set using built in methods
# NOTE : append and insert method not allowed
# add(): to add element in set.
'''
s = {1, 2, 4, "mango", 4-3+5 }
s.add(45)
print(s)

s.add(200, 300) # not allowed bcoz only one argument can be passed
'''

# Adding Multiple elements:
'''
set1 = {2,3,4}
set1.update([3, 5, 8, 4, 10, "mango"])
print(set1)

set1.update(("apple"))
print(set1)
'''

# An empty set
'''
s = {}
print(type(s))  # dict
'''

# set constructor method
'''
Empty_s = set()
print(type(Empty_s))
print(Empty_s)
'''

# How to delete an element from set:
'''
s = {1,2,3, 4,5 , 7}
# del s[2]   # 'set' object doesn't support item deletion
print(s)

s = {1,2,3, 4,5 , 7}
del s
print(s)
'''

# Using built in methods
'''
s = {2,3,5, "harsh"}
s.remove(3)
print(s)

s.clear()
print(s)
'''

# discard Mehtod
'''
s = {2,3,5,7,4, "harsh"}
s.discard(3)
s.discard(8)
print(s)
'''

# assign1 : WAP to create  a set named Emp_Details with elements: 101, "shivani", 20000, "web developer" accept an input element from user to remove the specific element. ans to be removed
'''
Emp_Details = {101, "shivani", 20000, "web developer"}
remove_item = input("Enter element you want to remove: ")
print(Emp_Details)
Emp_Details.remove(remove_item)
print(Emp_Details)
'''

# Set Operations: (union() eg: A|B, intersection() eg: A&B , difference() eg: A-B, symmetric_difference() eg: A^B)
'''
A = {1, 2, 3, 4, 5}
B = {5, 6, 7, 8, 9}
print("Union: ", A|B)
print("Union using method: ", A.union(B))
print("Intersection: ", A&B)
print("Intersection using method: ", A.intersection(B))
print("Difference: ", A-B)
print("Difference using method: ", A.difference(B))
print("Symmetric Difference: ", A^B)
print("Symmetric Difference using method: ", A.symmetric_difference(B))
'''


# Question: WAP to find the unplaced student list among the given student list and placed list
'''
student_list = ["Harsh", "Adarsh", "Vedant", "Ayush", "Kapil", "Shiva"]
print(f"{student_list} are total students.")
placed_list = ["Shiva", "Harsh", "Vedant", "Kapil"]
print(f"{placed_list} are placed students.")

print(f"Unplaced students are: {set(student_list) - set(placed_list)}")
# ------------ using method --------------
print(f"Unplaced students are: {set(student_list).difference(set(placed_list))}")
'''