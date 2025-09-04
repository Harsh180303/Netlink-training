# WAP to find out the maximum of 3 number
'''
n1, n2, n3 = map(int, input("Enter 3 numbers: ").split())
if (n1 > n2) :
    if (n1 > n3) :
        print("n1 is greater")
    else :
        print('n3 is greater')
else:
    if (n2 > n3):
        print("n2 is greater")
    else: 
        print("n3 is greater")
'''


# TERNARY

age = int(input("Enter your age: "))

print("Issue license") if (age > 18) else print("License can't be issued")