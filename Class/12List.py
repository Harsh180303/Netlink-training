'''
print("List with built in method")
L = [123, 456, 789, 123, 908, 786]
print("List is : ", L)

# len() used to return length of the list.
print("List length : ", len(L))

# max() used to return maximum val of the list.  (we can not use any val other than a number otherwise it will throw err)
print("List max element : ", max(L))

# min() used to return minimum val of the list.  (we can not use any val other than a number otherwise it will throw err) [we can also check with True and False it will work]
print("List max element : ", min(L))

# sorted(): used to arrange the list item in ascending order
print("sorted list in ascending: ", sorted(L))

# count() is used to get the occurance of the given element
print("List: Occurence of 123 ", L.count(123))

# index(): it returns the position of given element 
print("Index: ",L.index(123))

'''

# QUESTION

'''
fruitList = ["apple", "mango", "grapes", "apple"]
ele = input("Enter a fruit name: ")

c = 0
for fruit in fruitList :
    if (ele == fruit):
        print(f"{fruit} found! at {fruitList.index(fruit)}")
        print(f"{fruit} found! at {c}")
        break
    else :
        print("element not found")
    c+=1
'''

'''
# reverse(): it return the reversed list 
Lst = [1,2 ,3, 4,5,6,8, 3,6,2,6,2]
sortedLst = sorted(Lst)
print("Sorted list ", sortedLst)
sortedLst.reverse()
print("Reversed sorted list ", sortedLst)
'''


# deletion methods --- pop() remove(), del(), clear()

'''
# pop()

L = [11, 22, 33, 44, 55]
print("List: ", L)

print("An element popped out: ", L.pop())  # remove last element
print("new List: ", L)  # remove last element

print("An element popped out: ", L.pop())  # remove last element
print("new List: ", L)  # remove last element

print("An element popped out: ", L.pop())  # remove last element
print("new List: ", L)  # remove last element

print("An element popped out: ", L.pop())  # remove last element
print("new List: ", L)  # remove last element

print("An element popped out: ", L.pop())  # remove last element
print("new List: ", L)  # List is empty now

print("An element popped out: ", L.pop())  # error cause empty list
print("new List: ", L)
'''

L = [11, 22, 33, 44, 55]
print("popped ele at index 3 ",L.pop(3))

# when we use pop() by default last element popped out and if you want to remove a specific value then you have to provide index value inside the parenthesis of pop()
# it also support negative indexing inside parenthesis()

# any/ all   