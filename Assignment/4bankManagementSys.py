# TODO: Bank management system

'''
Male
Age < 60 → Interest = 6%
Age ≥ 60 → Interest = 7%

Female
Age < 58 → Interest = 6.5%
Age ≥ 58 → Interest = 7.5%
'''

gender = input("Enter your gender, (Type M/F): ").upper()
age = int(input("Enter your age: "))

if (gender == "M"):
    if (age >= 60 ):
        print("Your intrest rate will be 7%")
    else :
        print("Your intrest rate will be 6%")
else :
    if (age >= 58 ):
        print("Your intrest rate will be 7.5%")
    else :
        print("Your intrest rate will be 6.5%")