# Encapsulation
'''
Encapsulation: It is wrapping up of data and functions together in a single unit is called as encapsulation
                                    OR
Wrapping up of data members and member functions is known as encapsulation

To secure it's data and manage it's accessability encapsulation is used
'''

# Inharitance
'''
Inharitance: In which  one class aquires the property and behaviour from another class
Eg: Parent child relationship where child aquire properties from it's parent by birth

It follows is-a relationship

Base Class: A class which gets inherited by another class is called as base class / parent class / super class

Derived Class: A class which inherits the properties of another class is called derived class / child class / sub class

Why inheritance:
    Re-usibility
    Extansibility
    To avoid repetition of code
'''

# How to achieve inheritance in programming
'''
class Employee:
    def __init__(self, id, dept):
        self.E_id = id
        self.E_dept = dept        

    def getE(self):
        print(f"Id: {self.E_id}")
        print(f"Department: {self.E_dept}")

# Creating derived class

class Developer(Employee):
    def __init__(self, id, dept, name, role):
        Employee.__init__(self, id, dept)
        self.name = name
        self.role = role
    #     super().__init__(id, dept)

    def getDev(sf,):
        sf.getE()
        print(f"Name: {sf.name}")
        print(f"Role: {sf.role}")

# create object of Developer (derived class)
id = int(input("Enter your id: "))
dept = input("Enter your department name: ")
name = input("Enter your name: ")
role = input("Enter your role: ")

dev1 = Developer(id, dept, name, role)
dev1.getDev()
'''