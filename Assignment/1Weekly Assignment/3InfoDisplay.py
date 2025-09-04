# Basic Information display

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print(f"Hello {user_name}! You are {user_age} years old.")

# without f string
print("Hello ", user_name + "! You are ", user_age + " years old.")