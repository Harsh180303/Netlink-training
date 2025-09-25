# Fibonacci Series
# Reverse String
# Armstrong Numbers

# kite
# butterfly
# A BB CCC DDDD EEEEE

# Pyramid
 
#     *
#    ***
#   *****
#  *******
# *********
'''
for i in range(4):
    for j in range(4-i-1, 0, -1):
        print(" ", end=" ")
        
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()
'''

# *******
#  *****
#   ***
#    *
# inverted pyramid
'''
k = 3
for i in range(4):
    for j in range(i):
        print(' ', end=" ")
    for j in range(4-i+k):
        print("*", end=" ")
    print()
    k-=1
'''


# Fibonacci series:
# 0 1 1 2 3 5 8 13
'''
a = -1
b = 1

for i in range(8):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
'''


# Armstrong numbers
# 0, 1, 153, 370, 371, 407, 1634, 8208, 9474
# 1*1*1 + 5*5*5 + 3*3*3 = 152
'''
num = int(input("Enter a number: "))
original_num = num
no_of_digit = 0
for i in str(num):
    no_of_digit += 1

print(no_of_digit)

sum = 0
while num > 0:
    last_dig = num % 10
    sum += last_dig ** no_of_digit
    num = num // 10


if sum == original_num :
    print("This is an Armstrong number.")
else :
    print("This is not and Armstrong number.")
'''