student = {"name": "Harsh", "age": 23, 18: "Lucky Number", "age": 22 }
# so it will not give error whereas it will give the most recent value of that perticular  key
print(student)

# Accessing dict elements
# Method 1
student = {"name": "Harsh", "age": 22, 18: "Lucky Number", "grade": "A"}
print(student["name"])
print(student["grade"])
# print(student[18])

# Method 2
print(student.get(18, "Not Avail"))
print(student.get(189, "Not Avail"))
print(student.get("hello"))
print(student)

# Modifying dictionary ele
# Dictionary are mutable, so you can add, update or delete elements
student["age"] = 23
print(student)
student['isMillionare'] = True
print(student)
del student[18]
print(student)

# Dictionary Mthods
key = student.keys()
value = student.values()
item = student.items()

print(key)
print(value)
print(item)