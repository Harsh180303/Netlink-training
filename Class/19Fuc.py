# Date function with default values 
''' Always assign from last '''
'''
def date(dd=1, mm=10, yy=2025):
    print(f"{dd} / {mm} / {yy}")

date()
date(24)
date(24, 9)
date(24, 9, 2026)
date(9, 10, )
date(None, None, None)
'''

# NOT ALLOWED
'''
def date(dd=1, mm=10, yy=2025):
    print(f"{dd} / {mm} / {yy}")

# date(25, ,)
# date(25, ,2026)
# date(, ,2026)
# date(, ,)
'''


'''
def calme(x,y,z=3,w=5):
    pass

# calme(1,2,w=13,z=1,2)
# calme(x=1,z=4,w=11)
# calme(11,12,13,z=4)
# calme(11,12,v=14)
'''


# LOCAL SCOPE OF VARIABLE
# GLOBAL SCOPE
# ===============================
'''
def fun():
    global x
    x = 12
    print(f"x = {x}")

x = 17
print(f"x = {x}")
fun()
print(f"x = {x}")
'''

# WAP to define a function named Profile(d_name, d_stream, d_skill) Accept input from the user to pass it to the function and do return all the values and print
'''
def Profile(d_name, d_stream, d_skill):
    return d_name, d_stream, d_skill

name = input("Enter name: ")
stream = input("Enter stream: ")
skill = input("Enter skill: ")

t = Profile(name, stream, skill)
print(t)
for item in t:
    print(item)
'''


# WAP to create a tuple named marks pass this tuple to a function named score inside function.
# i) You have to display all the marks individually
# ii) Add 5 to each mark
'''
def score(marks):
    for val in marks:
        print(val)

    for val in marks:
        print(f"Incremented value = {val + 5}")

marks = tuple(map(int, input("Enter elements saperated by comma: ").split(',')))

score(marks)
'''