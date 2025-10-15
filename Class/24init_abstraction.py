# Abstraction
'''
It is used to provide or show information to the current problem domain.
Eg: Buying a car/ ATM/  vending machine, fan etc

How to achieve abstraction in programming:
with the help of Access specifiers:
To restrict the access of data members of the class.
3 types of access specifier : PUBLIC / PRIVATE / PROTECTED

Public: Are accessible from anywhere in an application.
    Eg: roll_no = 111
Protected: P.M are accessible by its derived classes only. [using single underscore]
    Eg: _name = "Harsh"
Private: Are accessible within it's class only.
    Eg: __Mark = 100  [using double underscore]
'''

# Demo
'''
class Employee:
    age = 12
    _E_Name = 'abc'  # Protected Member.
    __E_Id = 1  # Private Member.

    def __init__(sf, nm, id):
        sf._E_Name = nm
        sf.__E_Id = id

    def getE(sf):
        print(f"Name: {sf._E_Name}")
        print(f"ID: {sf.__E_Id}")

name = input("Enter your name: ")
id = int(input("Enter ID: "))
emp1 = Employee(name, id)
emp1.getE()

print("Id (outside): ", emp1.age)
print("Name (outside): ", emp1._E_Name)   
# print("age: ", emp1.__E_Id)   # NOT ACCESSABLE
'''


# default init and perameterized init
'''
class employee:
    eid = 18
    ename = "harsh"

    def __init__(self):
        print("default init called")

    def __init__(self, id, nm):
        print("Parameterized Constructor")
        self.eid = id
        self.enm = nm

    def gete (self):
        print(self.eid)
        print(self.enm)

e1 = employee("Mayank", 180)
# e1 = employee()
e1.gete()
'''

# TASK: WAP to get addition of 2 numbers using Parameterized init
'''
class Addition:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def getSum(sf):
        s = sf.sm()
        print(f"Sum = {s}")
    
    def sm(sf):
        return sf.num1 + sf.num2
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
add_two_nums = Addition(num1, num2)
add_two_nums.getSum()
'''