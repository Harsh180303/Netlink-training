class Dog:
    def __init__(self, name="a", age=0):
        self.name = name
        self.age = age

dog1 = Dog()
dog1.name = "boxy"
dog1.age = 2
# print(dog1)
# print(dog1.name)
# print(dog1.age)

class Ai:
    def __init__(self, company, model):
        self.company = company
        self.model = model

comp = input("Enter name of Provider / Company model you prefer: ")
model = input("Enter model name: ")

my_ai_tool = Ai(comp, model)
print(my_ai_tool)
print(my_ai_tool.company)
print(my_ai_tool.model)

