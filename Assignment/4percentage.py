# TODO: ask user to enter percentage and check it's grade

per = int(input("Enter your percentage: "))

if (per >= 80 and per < 100) :
    print("A Grade.")
elif (per >= 70 and per < 80 ) :
    print("B Grade.")
elif (per >= 60 and per < 70) :
    print("C Grade.")
elif (per >= 50 and per < 60) :
    print("D Grade.")
else :
    print("Failed.")