# 1.Write a program to convert duplicate number if it is exist in continuous manner to single one in a list for example: If the list is: [2,3,4,4,3,5,5,7,7,4,2,1,1,8] So the output is : [2,3,4,3,5,7,4,2,1,8]
'''
list1 = list(map(int, input("Enter the ele. of list: ").split()))
print(f"given list is: {list1}")

val = -1
non_cont_dup = []

for i in list1:
    if (i != val):
        non_cont_dup.append(i)
    val = i

print(f"non continious duplicate ele list is: {non_cont_dup}")
'''

# 2. Write a program to convert duplicate numbers to single one in a list for example: If the list is : [2,3,4,4,3,5,5,7,7,4,2,1,1,8] So the output is : [2,3,4,5,7,1,8]
'''
lst1 = list(map(int, input("Enter the elements of list: ").split()))
print(f"given list is: {lst1}")

lst1.sort()
print(f"sorted : {lst1}")
non_dup_list = []

val = -1
for i in lst1:
    if (i != val):
        non_dup_list.append(i)
    val = i

print(f"List having non duplicate elements: {non_dup_list}")
'''


# 3. Write a program using function which accepts tuple as a arguments and return all even values as a tuple.
'''
def evenVal(tup):
    my_tuple = ()
    for val in tup:
        if (val % 2 == 0):
            my_tuple = my_tuple + (val,)
    return my_tuple

tup1 = tuple(map(int, input("Enter numbers saperated by comma: ").split(",")))

print(evenVal(tup1))
'''

# 4.Input a string and check if it is palindrome or not?
'''
str1 = input("Enter a string: ")
rev_str = ""

for letter in str1:
    rev_str = letter + rev_str

if (rev_str == str1):
    print(f"{str1} is palindrome.")
else :
    print(f"{str1} is not palindrome.")
'''


# 5. Write a program to make a list of 10 string given by user and sort all  list alphabetically.
'''
str_list = input("Enter strings saperated by sapce: ").split()
sorted_list = list(sorted(str_list))
print(sorted_list)
'''

# 2. Write a program to convert duplicate numbers to single one in a list for example: If the list is : [2,3,4,4,3,5,5,7,7,4,2,1,1,8] So the output is : [2,3,4,5,7,1,8]
# Now without using another list:
'''
lst1 = list(map(int, input("Enter the elements of list: ").split()))
print(f"given list is: {lst1}")

for i in lst1:
    for j in range(1, len(lst1)+1):
        if (i == lst1[j]):
            lst1.remove(lst1[j])

print(f"List having non duplicate elements: {lst1}")
'''