# Assign on classes and Objects:
# Task: WAP to create a class named Student and display the student information (rollno  ,name, five subject marks in a Tuple).
'''
class Student:
    roll = 1
    name = "Your Name"
    marks = (0,0,0,0,0)

    def set_stud(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def get_stud(self):
        print(f"{self.name}'s roll number is {self.roll} and marks are {self.marks}")

s1 = Student()

name = input("Enter your name: ")
roll = int(input("Enter your roll number: "))
marks_list = list(map(int, (input("Enter your marks saperated by comma: ").split(','))))
marks_tuple = tuple(marks_list)

s1.set_stud(roll=roll, name=name, marks=marks_tuple)
s1.get_stud()
'''


# Task-2: WAP to create a class named Swap to do swapping of 2 numbers.
'''
class Swap:
    num1 = 0
    num2 = 0
    
    def swap_nums(self):
        temp = self.num1
        self.num1 = self.num2
        self.num2 = temp

    def set_swap(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def get_swap(self):
        self.swap_nums()
        print(f"a = {self.num1}")
        print(f"b = {self.num2}")

s = Swap()
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
s.set_swap(num1=a, num2=b)
s.get_swap()
'''

# Task-3: WAP to create a class named Addition to do addition of 2 numbers.
'''
class Addition:
    num1 = 10
    num2 = 12

    def set_addtion(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def get_addition(self):
        total = self.add()
        print(f"Addition of {self.num1} and {self.num2} = {total}")

    def add(self):
        return self.num1 + self.num2
    
s = Addition()
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
s.set_addtion(a, b)
s.get_addition()
'''

# Task-4:A start up employes Intern.The following details of Intern stores:
# 1.First_Name
# 2. LAst_Name
# 3. Mobile_No
# 4. Email
# WAP to create Intern class,which stores above details.Create init() which takes only one parameter(self,) and ask user to enter values for above data.Craft a function putdata() to display above data.
'''
class Intern:
    def __init__(self, ):
        self.f_name = input("Enter First name: ")
        self.l_name = input("Enter Last name: ")
        self.mob = int(input("Enter Mobile number: "))
        self.email = input("Enter Email address: ")

    def putdata(self,):
        print('\n')
        print(f"Intern name - {self.f_name} {self.l_name}\nIntern mobile number - {self.mob}\nIntern email - {self.email}")
        
new_intern = Intern()

new_intern.putdata()
'''

# 5. Create a class named Book. And, implement as above problem.
'''
class Book:
    def __init__ (self,):
        self.book_name = input("Enter book name: ")
        self.no_of_pages = int(input("Enter number of pages : "))
        self.ISBN = input("Enter ISBN number: ")
        self.Author = input("Enter Author name: ")

    def get_details(self, ):
        print()
        print(f"Book name - {self.book_name}")
        print(f"Number of pages - {self.no_of_pages}")
        print(f"ISBN number - {self.ISBN}")
        print(f"Author name - {self.Author}")

b = Book()
b.get_details()
'''