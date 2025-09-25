
# TRANSLATE METHOND

'''
original_string = "Hello World Seah!"

treanslation_table = str.maketrans("aeiou", "12345")
translated_string = original_string.translate(treanslation_table)

print(translated_string)
'''
# Alphanum
'''
st = "Python13"
print(st)
print(st.isalnum())
'''


# isalnum
'''
st = "Pythonj#@"
print(st)
print(st.isalnum())
'''

# count
'''
st = "apple zoo apple"
print(st)
print(f"count of apple is: ", st.count('apple'))
'''

# center
'''
st = "Netlink"
print("Centered string: ", st.center(50))
'''

# replace
'''
str = "apple zoo apple"
print(str.replace('apple', 'mango'))
'''

# partition   --- always returns touple and divide string in 3 parts 
'''
text = "hello@world.com"

result = text.partition("@")
print(result)

# eg. 2
print("hello world".partition("@"))
'''


# split
'''
st = "harsh is a dev"
print(st.split(' '))
'''

# strip
'''
str = '     this   is new        word   '
print(str.strip())
'''

# isdigit
'''
dig = "123a"
num = "21345"
print(dig.isdigit())
print(num.isdigit())
'''

# format
'''
# eg. 1
quantity = 3
itemno = 567
price = 49.5
myorder = "I want to pay {2} dollars for {0} peices of item {1}"
print(myorder.format(quantity, itemno, price))

# eg. 2
name = "Harsh"
age = 22
sentence = "My name is {} and I'm {} years old.".format(name, age)
print(sentence)

# eg. 3
sentence = "I've been learning {x} for {y} months.".format(x="Python", y="1.5")
print(sentence)

# f string
name = "Krish"
age = 25
print(f"My name is {name} and I am {age} years old.")
'''