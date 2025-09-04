# program to clac. total marks and precentage of a student

maths = int(input("Enter your marks in mathematics: "))
physics = int(input("Enter your marks in physics: "))
chem = int(input("Enter your marks in chemistry: "))
hindi = int(input("Enter your marks in hindi: "))
english = int(input("Enter your marks in english: "))

total_marks = 500
obtained = maths + physics + chem + hindi + english
per = (obtained/total_marks) * 100

print(f"Your total obtained marks is {obtained}")
print(f"Your percentage is {per}")