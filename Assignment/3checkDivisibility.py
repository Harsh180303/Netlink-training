# Checking if a given number is divisible by another given number

num = int(input("Enter a number: "))
new_no = int(input("Enter a new number to check divisibility: "))

if (num % new_no == 0) :
    print(f"{num} is completely divisible by {new_no}.")
else :
    print(f"{num} is not divisible by {new_no}.")