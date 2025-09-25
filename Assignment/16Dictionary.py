# Create a dictionary of 5 students with their marks and print the marks of a particular student.
'''
dcy = {"Harsh": 100, "Shiva": 95, "Vedant": 90, "Shanvi": 85, "Priyanka": 98, "Sheetal": 92, "Akhilesh": 32, "Ashish": 49, "Yogesh": 20}

name = input("Enter the name whose marks you want to know? ").title()

print(f"Marks of {name} is {dcy[name]}")
'''

# Write a program to add a new key-value pair to an existing dictionary.

'''
existing_dict = {
    "name": "Harsh",
    "is_student": False,
    "age": 22
}

key = input("Enter key: ")
value = input("Enter value: ")

existing_dict[key] = value
existing_dict["is_programmer"] = True
print(existing_dict)
'''


# Given a dictionary, update the value of an existing key.
'''
update_val = {"name": "Harsh", "intrest": "Web dev"}
update_val["intrest"] = "AI/ML"
print(update_val)
'''
# Better example:
'''
student_marks = {
    "Mayank": 100,
    "Vedant": 80,
    "Tanish": 90,
    "Shanvi": 75
}
print(f"Original marksheet is: {student_marks}")

student_name = input("Enter the name of student: ")

if student_name in student_marks:
    new_marks = int(input(f"Enter the updated marks of {student_name}: "))
    student_marks[student_name] = new_marks
    print(f"Updated marks sheet is: {student_marks}")
else :
    print(f"Unable to find {student_name} in our records!")
'''


# Write a program to delete a key from a dictionary.
'''
new_dict = {}

for i in range(3):
    key = input('Enter key: ')
    val = input("Enter value: ")
    new_dict[key] = val

print(new_dict)

del new_dict["name"]
print(new_dict)
'''
# Better way:
'''
students_marks = {
    "Shiva": 95,
    "Ayush": 62,
    "Ansh": 80,
    "Rudra": 70
}

print(f"Original dictionary is: {students_marks}")

name = input("Enter the student's name you want to remove: ")

if (name in students_marks):
    del students_marks[name]
    print(f"New dictionary is: {students_marks}")
else :
    print("Invalid input!")
'''

# Create a dictionary and print all keys and all values separately.
'''
D = {"student1": {"name": "Sanskar", "age": 25, "city": "Hyd"}, "student2": {"name": "Rudra", "age": 23, "city": "Jbp"}}

keys = D.keys()
values = D.values()

print(f"Keys are: {keys}")
print(f"values are: {values}")
'''
# Enhanced way: 
'''
student_marks = {
    "Harsh": 99,
    "Raviraj": 68,
    "Sanskar": 57,
    "Ayush": 49
}

print("Keys are: ")
for k in student_marks.keys():
    print(k)

print("\nValues are: ")
for v in student_marks.values():
    print(v)
'''

# Write a program to check if a key exists in a dictionary.



# Count how many key-value pairs are there in a dictionary (without using len()).


# Ways to create dictionary:
# 1
'''
name = input("Enter your name: ")
age = int(input("Enter the age: "))
d = {"name": name, "age": age}
print(d)
'''

# 2
'''
x = input()
y = input()
print({x:y})
'''

# 3
'''
D = {input(): input(), input(): input()}
print(D)
'''

# 4
'''
D = {}
n = int(input('Enter the number of pairs: '))

for i in range(1, n+1):
    x = input("Enter the key: ")
    val = input("Enter the value: ")
    D[x] = val

print(D)
'''

# 5 Using an itreable object
'''
T = ("key1", 1, 4.5)
D = dict.fromkeys(T, 0)
print(D)
# all values initialized to 0. default val is none.
'''

# Other ways to create dictionary
# Using dict function with list
'''
L = [["name", "harsh"], ["age", 22], ["add", "mdp"]]
d = dict(L)
print(d)
'''

# Using dict function with tuple
'''
T = (("name", "tanish"), ("age", "14"), ("add", "bpl"))
d = dict(T)
print(d)
'''

# Using zip() function (with tuple)
'''
T1 = ("name", "age", "address") # keys  only
T2 = ("Vedant", 12, "bpl") # vals only
D = dict(zip(T1, T2))
print(D)
'''

# with list
'''
L1 = ["name", "age", "address"] # keys  only
L2 = ["Vedant", 12, "bpl"] # vals only
D = dict(zip(L1, L2))
print(D)
'''

# Nested Dictionary
'''
D = {"s1": {"name": "adarsh", "age": 23}, "s2": {"name": "Kartik", "age": 24}}
print(len(D))
print(D["s1"])
print(len(D["s2"]))
print(D["s2"])


print(D["s1"]["name"])

# how to access the age of 2nd person
print(D["s2"]["age"])
'''

# Trying to use some built in mehtods
# len()
'''
D = {"s1": {"name": "Harsh", "age": 22, "add": "mdp", "lang": ["JavaScript", "Nodejs", "Python", "Java"]}, "s2": {"name": "Adarsh", "age": 23, "add": "indore"}}

print(len(D)) # 2
print(len(D["s1"])) # 4
print(D["s1"]) 
print(len(D["s2"])) # 3
'''

# pop()
'''
D = {"s1": {"name": "Harsh", "age": 22, "add": "mdp", "lang": ["JavaScript", "Nodejs", "Python", "Java"]}, "s2": {"name": "Adarsh", "age": 23, "add": "indore"}}

# print(D.pop('s1'))
print(D["s1"].pop("add"))
print(D)
'''

# del
'''
D = {"s1": {"name": "Harsh", "age": 22, "add": "mdp", "lang": ["JavaScript", "Nodejs", "Python", "Java"]}, "s2": {"name": "Adarsh", "age": 23, "add": "indore"}}
# del D["s2"]
# print(D)

# del D
# print(D) # D is not defined
'''

# popitem()
'''
D = {"s1": {"name": "Harsh", "age": 22, "add": "mdp", "lang": ["JavaScript", "Nodejs", "Python", "Java"]}, "s2": {"name": "Adarsh", "age": 23, "add": "indore"}}

print(D.popitem())
print(D)
'''

# clear()
'''
D = {"s1": {"name": "Harsh", "age": 22, "add": "mdp", "lang": ["JavaScript", "Nodejs", "Python", "Java"]}, "s2": {"name": "Adarsh", "age": 23, "add": "indore"}}

D.clear()
print(D)
'''

# keys()
'''
D = {"s1": {"name": "Harsh", "age": 22, "add": "mdp", "lang": ["JavaScript", "Nodejs", "Python", "Java"]}, "s2": {"name": "Adarsh", "age": 23, "add": "indore"}}
print(D.keys())
print(D["s1"].keys())
'''

# values()
'''
D = {"s1": {"name": "Harsh", "age": 22, "add": "mdp", "lang": ["JavaScript", "Nodejs", "Python", "Java"]}, "s2": {"name": "Adarsh", "age": 23, "add": "indore"}}
print(D.values())
print(D["s1"].values())
'''

# items() ----- Returns a list of key value pairs
'''
D = {"s1": {"name": "Harsh", "age": 22, "add": "mdp", "lang": ["JavaScript", "Nodejs", "Python", "Java"]}, "s2": {"name": "Adarsh", "age": 23, "add": "indore"}}
print(D.items())
'''

# update()
'''
D = {"s1": {"name": "Harsh", "age": 22, "add": "mdp", "lang": ["JavaScript", "Nodejs", "Python", "Java"]}, "s2": {"name": "Adarsh", "age": 23, "add": "indore"}}

D["s1"].update({"is_graduated": True, "add": "Bangalore"})
print(D)
'''


# D = {"name": "harsh", "age": 22}
# D.clear()
# print(D)

# # D.pop('key')
# D.popitem()


