#2
for i in range(1, 20):
    if i % 2 != 0:
        print(i)
        mum = i + 1

#13
for i in range(100,5000,4):
    print(i)

#14
for i in range(5, 2500):
    if i % 6 == 0:
        print(i)

#15
name = input("enter a name")
n = len(name)
for i in range(n):
    print(name[i], end=" ")
