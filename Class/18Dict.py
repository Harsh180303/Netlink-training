'''
marks = {"python": 41, "java": 56, "javascript": 89}

for k in marks.keys():
    print(f"{k} : {marks[k]}")

for sub,score in marks.items():
    print(f"{sub} : {score}")
'''

'''
mydict = {'a': 1, "b": [1,2,3,4], "c": 3, }
result = mydict.pop("b", 0)
print(result)
'''

                                        # FUNCTIONS

# benefits
# 1. Reusability
# 2. Maintainability
# 3. Readability
# 4. Modularity
# 5. To avoid repetetion

def Person(name, age, city):
    print(f"Hello, My name is {name} and I am {age} years old. live in {city}")

Person("Harsh", 22, "Bhopal")