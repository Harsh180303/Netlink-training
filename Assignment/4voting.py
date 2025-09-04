# TODO: Voting Management system

nationality = input("Are you an Indian citizen. Type (Yes/NO): ").lower()

if (nationality == "yes") :
    age = int(input("Enter your age: "))
    if (age >= 18 and age <= 110) :
        print("You are eligible to vote.")
    elif (age >= 0 and age < 18): 
        print("Sorry, You are not eligble to vote.")
    else :
        print("Please enter a valid input.")
else :
    print("You are not eligible for vote. because you are not an indian citizen")