# Accessing & Slicing ----------->
# Indexing (positive & negative).
# String slicing (s[0:3], s[::-1] for reverse).

# String Functions/Methods ----------->
# .upper(), .lower(), .strip(), .replace(), .split(), .join() etc.
# Checking things: .isalpha(), .isdigit(), .startswith(), .endswith().
'''
str = input("Enter a string: ")
print(f"uppercase is", str.upper())
print(f"lowercase is", str.lower())
print(f"strip is just like trim", str.strip())
'''


i=3
while i:
    i -=1
    print(i)

print("---------------------------------")

i=3
while i>0:
    i -=1
    print(i)

print("----------------------------------")

i=3
while True and i:
    i -=1
    print(i)


print("Answer is All are same...")

str = input("Enter something")
str2 = input("Enter once again")

str = str+str2
print(str)