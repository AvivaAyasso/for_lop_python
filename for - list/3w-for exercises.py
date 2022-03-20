#1
for i in range(1500,2701):
     if i%7==0 and i%5==0:
        print(i)



4
for i in range(1,6):
    print("* "*i)
for j in range(4,0,-1):
    print("* "*j)

5
word=input("enter a word")
print(word[::-1])

word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")

#6
count1=0
count2=0
for i in range(1,6):
    if i%2==0:
        count1=count1+1
    elif i%2!=0:
        count2=count2+1
print("odd numbers=", count2, "\neven numbers=",count1)

7
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for i in datalist:
    print(i ,type(i))
#8
for i in range(0,7):
    if i==3:
        continue
    elif i==6:
        continue
    print(i ,end=' ')



10
for i in range(0,51):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
