# Accept a list from user using list comprehension.
'''
row = int(input("Enter number of rows: "))
col = int(input("Enter number of cols: "))

matrix = [int(input(f"Enter ele {y+1} in row {x+1}: ")) for x in range(row) for y in range(col)]
print(matrix)
'''

# Ek string list me se wo saare words nikaalo jinki length 5 se zyada hai.
'''
my_string = ["this", "string", "Harsh", "seven", "characters" '12345']
new_list = [st for st in my_string if len(st) == 5]
print(my_string)
print(f"List have string with 5 characters: {new_list}")
'''

# accept numbers and print a matrix
'''
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of cols: "))

matrix = [[int(input(f"Enter element {j+1} of row {i+1}: ")) for j in range(col)]
            for i in range(row)
          ]

print(matrix)
'''

# 1 se 20 tak ke numbers me se sirf divisible by 3 wale numbers ek list me store karo.
str = "Harsh"
help(str)