# Write a program to-
# Given a colour in Spanish find the German equivalent
# en_de={"red":"rot", "green":"grün", "blue":"blau", "yellow":"gelb"}
# en_es={"red":"rojo","green":"verde ","blue":"azul", "yellow":"amarillo"}

en_de={"red":"rot", "green":"grün", "blue":"blau", "yellow":"gelb"}
en_es={"red":"rojo","green":"verde ","blue":"azul", "yellow":"amarillo"}

for eng,spanish in en_de.items():
    pass


# Create a dictionary of countries and their capitals. Given a capital display the country and vice versa
'''
D = {"India": "Delhi", "UK": "London", "Japan": "Tokyo", "America": "Washinton DC"}

country_or_capital = input("Give the country or capital name: ")

if country_or_capital in D:
    capital = D[country_or_capital]
    print(f"{capital} is the capital of {country_or_capital}")

elif country_or_capital in D.values():
    for ctry, cap in D.items():
        if cap == country_or_capital:
            print(f"{country_or_capital} is the capital of {ctry}")

else :
    print("Invalid Input")
'''

# Create a dictionary of n number of learners. Each learner should have a name, age, enrollment number, ELAT_Marks, MLAT_Marks and EXLAT_Marks. Create a menu which will print:

# - Learner with highest Marks in EXLAT

# - Given a learner name, determine if he/she has failed or passed in EXLAT.

# - Given an enrollment number find the corresponding learner details.

n = int(input("Enter the number of learners: "))

marks = {}

for i in range(n):
    name = input(f"Enter the name of learner {i+1}: ")
    age = int(input(f"Enter the age of {name}: "))
    roll_no = int(input(f"Enter the enrollment number of {name}: "))
    ELAT_Marks = int(input(f"Enter {name}'s ELAT marks? "))
    MLAT_Marks = int(input(f"Enter {name}'s MLAT marks? "))
    EXLAT_Marks = int(input(f"Enter {name}'s EXLAT marks? "))

    stud = 's' + str(i+1)
    marks[stud] = {"name": name, "age": age, "roll_no": roll_no, "ELAT_Marks": ELAT_Marks, "MLAT_Marks": MLAT_Marks, "EXLAT_Marks": EXLAT_Marks}

print(marks)

EXLAT_max = max(marks["s1"][EXLAT_Marks])
print(f"Learner with highest Marks in EXLAT is {EXLAT_max}")