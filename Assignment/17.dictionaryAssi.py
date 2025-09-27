
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
'''
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

while (True):
    print("\nMenu:")
    print("1. Learner with highest Marks in EXLAT")
    print("2. Check if a learner has passed/failed in EXLAT")
    print("3. Find learner details by enrollment number")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    # {'s1': {'name': 'Harsh', 'age': 22, 'roll_no': 18, 'ELAT_Marks': 100, 'MLAT_Marks': 99, 'EXLAT_Marks': 100}, 's2': {'name': 'Virat', 'age': 36, 'roll_no': 19, 'ELAT_Marks': 90, 'MLAT_Marks': 98, 'EXLAT_Marks': 97}}

    if choice == 1:
        highest_marks = -1
        topper = None
        for stud ,details in marks.items():
            if details["EXLAT_Marks"] > highest_marks:
                highest_marks = details["EXLAT_Marks"]
                topper = details["name"]
        print(f"{topper} got highest marks = {highest_marks}")
    elif choice == 2:
        learner_name = input("Enter learner's name: ") 
        for details in marks.values():
            if details["name"].lower() == learner_name.lower():
                if details["EXLAT_Marks"] > 40:
                    print(f"{learner_name} is passed and got {details["EXLAT_Marks"]} marks")
                else :
                    print(f"{learner_name} is failed and got {details["EXLAT_Marks"]} marks")
    elif choice == 3:
        # Finding learner's details by enrollment no.
        enroll = int(input("Enter enrollement number: "))
        for details in marks.values():
            if details["roll_no"] == enroll:
                print(f"Learner's details: {details}")
                break
        pass
    elif choice == 4:
        print("Greacefully exiting the program...")
        break
    else :
        print("Invalid input, please retry.")
'''

# Write a program to-
# Given a colour in Spanish find the German equivalent
# en_de={"red":"rot", "green":"grün", "blue":"blau", "yellow":"gelb"}
# en_es={"red":"rojo","green":"verde ","blue":"azul", "yellow":"amarillo"}
'''
en_german={"red":"rot", "green":"grün", "blue":"blau", "yellow":"gelb"}
en_spanish={"red":"rojo","green":"verde ","blue":"azul", "yellow":"amarillo"}

sp = input("Enter spanish color name: ").lower()
english_color = None

for eng,span in en_spanish.items():
    if span == sp:
        english_color = eng
        break

print(f"German equivalent of {sp} is: {en_german[english_color]}")
'''