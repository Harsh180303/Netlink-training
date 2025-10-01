# OOPs in Python
# Object oriented programming system

# Benifits:
# 1. To develop an application to map with real world
# 2. To reduce user-client communication gap.
# 3. To fulfil the dynamic requiremnt of client
# 4. Re-usability
# 5. Easy mantainance
# 6. Security

# Major OOP Features
# 1. CLASS AND OBJECTS
# 2. INHARITANCE
# 3. POLYMORPHISM
# 4. ENCAPSULATION
# 5. ABSTRACTION

class Player:
    p_name = "Virat"
    p_city = 'Delhi'

p1 = Player()
p1.p_name = "Harsh"
p1.p_city = "Bhopal"

print(f"{p1.p_name} lives in {p1.p_city}")