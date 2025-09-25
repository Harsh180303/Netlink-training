# stuendt grade
# weekdays
# sum and avg of marks
# pattern

# leap year
'''
year = int(input("Enter a year: "))

if ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
    print("leap year") 
else :
    print("not leap year")
'''

# Armstrong no
# fibonacci
# perfect number
# leap year
# pyramid pattern
# right angled triangle

num = int(input("Enter a number: "))
og_num = num

# power = len(str(num))
power = 0
for i in str(num):
    power += 1

s = 0
while(num > 0):
    last_digit = num % 10
    s += last_digit** power
    num //= 10

if(s == og_num):
    print("Armstrong.")
else :
    print("Not armstrong")




    


start = int(input("Enter start num: "))
stop = int(input("Enter stop num: "))

for num in range(start, stop + 1):
    divisor_sum = 0
    for i in range(1, num // 2 + 1):
        if (num % i == 0):
            divisor_sum += i
    if divisor_sum == num and divisor_sum != 0:
            print(num, "is a perfect no. ")