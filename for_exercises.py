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

# max = 0
min = 10000
counteven = 0
countbig5 = 0
for i in range(6):
    num = int(input("enter a number"))
    if num > max:
        max = num
    if num < min:
        min = num
    if num > 5:
        countbig5+=1
    if num % 2 == 0:
        counteven+=1
print(max, min, counteven, countbig5)

count1 = 0
count2 = 0
for i in range(0, 52):
     if i % 2 == 0:
         count1 += 1
     if i % 4 == 0:
        count2 += 1
print("evenNumber:",count1)
print("unevenNumbers%4:",count2)

a = 1
b = 1
for i in range (1,40):
    c = a + b
    a = b
    b = c
print(c)


a = 1
b = 1
for i in range(5):
    c = a+b
    a = b
    b = c
print(c)






