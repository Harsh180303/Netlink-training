my_set = {1,2,3,4,5,6,7,8}
print(my_set.pop())
print(my_set)

# Set Membership test
print(3 in my_set)
print(31 in my_set)

# Mathematical Opearations  (union (|), intersection (&), difference (-), symmetric difference (^))
set1 = {2,4,6,8,10}
set2 = {10,12,14,16,18}

# union
union_set = set1.union(set2)
print(union_set)

# Intersection 
intersection_set = set1 & set2
print(intersection_set)

# intersection_update
'''
set1.intersection_update(set2)
print(set1)
'''

# Difference
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
print(set1.difference(set2))

# symetric difference
print(set1.symmetric_difference(set2))

# Stes methods
set1 = {1,2,3}
set2 = {3,4,5,1,2}

# is subse
print(set1.issubset(set2))

# is superset
set1 = {1,2,3,4,5}
set2 = {3,4,5}
print(set1.issuperset(set2))

# it will get the uniques elements from the list
lst = [1,2,2,3,4,4,5]
lst = set(lst)
print(lst)

# counting unique words in text
text = "In this tutorial we are dicussing about sets"
words = text.split()
print(words)

# convert list of words to set to get unique words
unique_words = set(words)
print(unique_words)
print(len(unique_words))