# fob = open("file.txt",'r+')
# print(fob.read())
# fob.write("Harsh")
# print(fob.read())


# Q1. WAP to accept 5 students record and write into the file.
fob = open('records.txt', "w+")
fob.write('S.No.\tS.Name\t\tS.Age\tS.Stream\n')
for idx, stud in enumerate(range(5)):
    name = input(f"Enter name of student {idx+1}: ")
    age = int(input(f"Enter age of {name}: "))
    stream = input(f"Enter stream of {name}: ")
    fob.write(f"{idx+1}\t\t{name}\t\t{age}\t{stream}\n")
