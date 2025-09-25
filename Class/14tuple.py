# Touple
# It is similar to List.
# It is ordered collection of similar or dis-similar elements.
# It is indexed where each element stored at specific index started from 0
# It is immutable
# Whenever you have write protected data prefer tuple to store
# It supports slicing
# Mesting of tuple is also supported.
# Built-in methods support only for non-changeable task like max() min() len() count() sort() reverse().
# del to delete entire tuple is allowed.

# Represented by parenthesis

# List_is = [11, 22, 33, 44, 55]
# List_is.
'''
t = (11, 22, 33, 44, 55)
print("tuple elements: ", t)

t2 = (11, 22, 33, 44, 44, "abc", True, 55, 34.2)
print("tuple with dis-similar elements: ", t2)
'''

# Empty tuple
'''
emp_tuple = ()
print(type(emp_tuple))
'''

# Creating tuple with single ele 
'''
tup = (1)
print(tup)
print(type(tup))  # int class
'''

'''
tup2 = (1,)
print(tup2)
print(type(tup2))  # tuple class 
'''

# Tuple paking is creating tuple without parenthesis is tuple packing.
'''
T = 123,234,345,456

print(T)
print("Type of T is : ", type(T))
'''

# Tuple packing
'''
numbers = 123, 234, 345, 456
print("\n Tuple Packing: ", numbers)
print("\n Type of tuple: ", type(numbers))
'''

# Tuple Un-packing
'''
numbers = (123, 234, 345, 456)
x, *y = numbers
print("\nTuple up-packing: ", numbers, "\nX= ", x, "\nY=", y)
'''

'''
Lang = ("C", "CPP", "Python", "Java", "Ruby")
print("\nP.Languages", Lang)

P2, P3, P4, *P5 = Lang
print("\n Tuple Un-Packing: \n", Lang,"\n P2= ", P2, "\nP3= ", P3, "\nP4= ", P4, "\nP5= ", P5)
'''

# Converting list into tuple
'''
test_list = [1, 2, 3]
new_tup = tuple(test_list)
print(new_tup)
print(type(new_tup))
'''

# Immutability check:
'''
tup3 = (1,2,3,4,5)
print("Tuple: ",t, "first ele: ", tup3[0])

# tup3[3] = 222 # now allowed
print("Item asssignment ", tup3)

# tup3.append(6)  #not allowed 
# tup3.insert(2, 34) #not allowed
'''

# accepting testing the class int or tuple
'''
L = [1]
check = tuple(L)
print(check)
print(type(check))
'''

# Method supported by tuple
# len()
tuplenew = (1,2,34,5,6,7,8)
'''
print("\n length of tuple ", tuplenew)
'''

# max()
'''
print("Max of tuple is : ", max(tuplenew))
'''

# min()
'''
print("Min of tuple is : ", min(tuplenew))
'''

# sort()
'''
print("Sorting of tuple: ", sorted(tuplenew, reverse=True))
'''

# Tuple with list
'''
tList = (1,2,3,[11,22,33])
print("\nTuple with List: ", tList)
'''

# Nested Tuple:
'''
t = (1,2,3,(111,222,333))

print(t, "\n", t[0], "\n", t[1], t[2], "\n", t[3])
print("\n========== Now printing only 3rd row ===========")
print(t[3][0])
print(t[3][1])
print(t[3][2])
'''

