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