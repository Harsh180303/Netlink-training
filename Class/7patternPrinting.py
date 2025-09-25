# start stop and step are the 3 attributes that we can use there
'''
for i in range(11):   # stop condition
    print(i, end=" ")

print("\nOnly stop condition\n")

for i in range(2, 11):     # start condition -> stop condition
    print(i, end=" ")

print("\nstart condition -> stop condition\n")

for i in range(0, 11, 2):   # start condition -> stop condition -> step condition
    print(i, end=' ')

print("\nstart condition -> stop condition -> step condition\n")
'''

# break, continue, pass

'''
n = int(input("Enter a number between 5 to 10 only: "))
for i in range(0, n + 1):
    if i == 3:
        break
    print(i, end=' ')
print("\nbreak at i == 3\n")


for i in range(0, n + 1):
    if i == 3:
        continue
    print(i, end=' ')
print("\ncontinue at i == 3\n")


for i in range(0, n + 1):
    if i == 3:
        pass
    print(i, end=' ')
print("\npass at i == 3\n")
'''


# Nested For loop
for i in range(5):
    for j in range(0, i+1):
        print("*", end=' ')
    print()