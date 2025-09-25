'''
String : I is a series of character.
it is indexed
it is immutable means not changable
it is ordered colletion
methematical operation cannot be performed on string
operations like : concatination (merging) and traversing and replication
sicing can alse be done

'''

# N | E | T | S | E | E | D
# 0   1   2   3   4   5   6


st = "Netlink"
print("\n String: ",st)
st = "Netseed"

print("\n string: ", st[0])
print("\n string: ", st[6]) 
print("\n string: ", st[-1]) 


print("=============== Slicing ==============")
print("\nString Slicing:", st[ : ])
print("\nString Slicing:", st[0 : ])
print("\nString Slicing:", st[ : 6])
print("\nString Slicing:", st[2 : 4])
print("\nString Slicing:", st[-3 : -1])
print("\nString Slicing:", st[-1 : -3])


# String Operations:

str1 = "Netlink"
str2 = " Netseed"
print("\nConcatination ", str1+str2)
print("\Replication ", str2*3)

# String is immutable
# str1[4] = "Z"
# print("\nString Updation: ", str1)

del str2
# print(str2)  # Error: Since we deleted this so we can't access it.
print("We can remove prefix using this ", str1.removeprefix("N"))

print("We can remove suffix using this ",str1.removesuffix("nk"))


print("\n String in upppercase", str1.upper())
print("\n String in lowercase", str1.lower())
print("\n swap the case of the string", str1.swapcase())

newString = 'fls#$2ldslf fjLHJLL'
print("\n Capitalize", newString.capitalize())
print("\n title", newString.title())

print('\n Length of string including space ', len(str1))

# isupper, islower, split, strip, format, isalpha, is........... all