12
number = []
for i in range(100):
    number.append(i)
print(number)

name = []
for i in range(10):
    j =input ("enter a name")
    name.append(j)
    print(name)

name = []
name2 = []
for i in range(10):
    j = input("enter a name")
    name.append(j)
    if "a" in j:
        name2.append(j)
print(name)
print(name2)