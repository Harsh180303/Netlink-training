# WAP to consider two different list one of Batsman and another of Bowlers and find the all rounders among them.
'''
batsman = input("Enter the name of batsman: ").split()
bowlers = input("Enter the name of bowlers: ").split()

all_rounders = set(batsman).intersection(set(bowlers))
print(f"All rounders in the team are: {all_rounders}")
'''

# WAP to consider three different list of placed students in TCS, Infosys, Wipro and find the total no. of placed students.
'''
tcs = input("Name of placed students in TCS: ").split()
infosys = input("Name of placed students in infosys: ").split()
wipro = input("Name of placed students in wipro: ").split()

total_placed_studs = set(tcs).union(set(infosys).union(set(wipro)))
print(total_placed_studs)
'''

# WAP to remove duplicates from a list using a set.
'''
list_of_nums = list(map(int, input("Enter numbers saperated by space: ").split()))
print(list_of_nums)

unique_num_set = set(list_of_nums)
unique_num_list = list(unique_num_set)
print(f"Unique numbers list is {unique_num_list}")
'''

# Find all pairs of elements in a list whose sum is equal to a given value.
'''
value = int(input("Enter a number: "))

lst1 = list(map(int, (input("Enter numbers saperated by sapce: ").split())))
print(lst1)

for i in lst1:
    for j in lst1:
        if (i+j == value):
            print(f"{i} + {j} = {value}")
            
'''