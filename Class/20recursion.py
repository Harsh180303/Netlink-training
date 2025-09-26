# Recursion

def Factorial(n):
    if n ==1 or n == 0:
        return 1
    else :
        f = n* Factorial(n-1)
        return f
    
num = int(input("Enter a number to check factorial: "))
print(f"factorial {Factorial(num)}")

# Tower of hanoi
