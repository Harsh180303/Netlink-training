'''
L = ["C", "CPP", "Python"]
L1 = []
L3 = [[]]
print("list", L)
print(any(L))
print(all(L))


print(any(L1))
print(all(L1))

print(any(L3))
print(all(L3))
'''


# it's sharing same memory location.
'''
a = [ [] ] * 3
a.append(5)

print(a)

a[0].extend([5])
print(a)

print(id(a[0]))
print(id(a[1]))
print(id(a[2]))


list1 = [1, 1]
print(id(list1[0]))
print(id(list1[1]))
'''

l = []
l.remove()