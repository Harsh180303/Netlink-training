# Finding weather a triangle is isosceles equilateral or scalene

side1 = int(input("Enter the length of first side of a triangle(in cm): "))
side2 = int(input("Enter the length of second side of a triangle(in cm): "))
side3 = int(input("Enter the length of third side of a triangle(in cm): "))

if (side1 == side2 == side3):
    print("This is an equilateral triangle")
elif ((side1 != side2) and (side2 != side3) and (side1 != side3)) :
    print("This is scalene triangle")
else :
    print("This is an isosceles triangle")