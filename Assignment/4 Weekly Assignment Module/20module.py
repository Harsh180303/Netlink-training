# 1.Write a Python program to select a random element from a list, set, dictionary-value, and file from a directory.
'''
import random

lst = [1,2,3,4,5,6,7,8,9]
list_ele = random.choice(lst)
print('Random element from a list is:',list_ele)

set1 = {"this", "is", "set", 1}
set_ele = random.choice(list(set1))
print('Random element from a set is:', set_ele)

dictionary = {"name": "Harsh", "age": 22, "isMarried": False, "grade": "A"}
dict_val = dictionary.values()
random_val = random.choice(list(dict_val))
print('Random element from a dictionary is:',random_val)
'''


# 2. Write a Python program to generate a random integer between 0 and 6 - excluding 6, random integer between 5 and 10 - excluding 10, random integer between 0 and 10, with a step of 3 and random date between two dates.
'''
from datetime import datetime, timedelta
import random as r

random_int = r.randint(0,5)
print(random_int)
random_int1 = r.randint(5,9)
print(random_int1)
random_int2 = r.randrange(0,10,3)
print(random_int2)

# date1 = datetime(2025, 3, 18)
# date2 = datetime(2026, 10, 4)
'''

# 3. Write a Python program to shuffle the elements of a given list.
'''
import random as r
my_list = [1,2,3,4,5,6,7,8,9]
r.shuffle(my_list)
print(my_list)
'''

# 4. Write a Python program to create a list of random integers and randomly select multiple items from the said list.
'''
import random
lst = []

n = int(input("Enter a number: "))

for i in range(n):
    lst.append(random.randint(0,9))

print(lst)
randomly_selected_num = random.choice(lst)
print(f"Randomly selected item from list is: {randomly_selected_num}")

new_lst = []

for i in range(randomly_selected_num):
    new_lst.append(random.choice(lst))

print(new_lst)
'''

# 5. Write a Python program to construct a Decimal from a float and a Decimal from a string. Also represent the decimal value as a tuple. Use decimal.Decimal
'''
import decimal
print("Construct a Decimal from a float:")
pi_val = decimal.Decimal(3.14159)
print(pi_val)

print("\nConstruct a Decimal from a string:")
num_str = decimal.Decimal("123.2356")
print(num_str)
print(num_str.as_tuple())
'''