#5row * 5column of "*"
n=5
for i in range(n): #O(n)
    for j in range(n): #O(n)
        print("*",end="")
    print(end="\n")
#O(n^2)

#5row * 5column * inc order
n=6
for i in range(n):
    for j in range(i):
        print("*",end="")
    print()

#5row * 5column 1-5  inc order
n=6
for i in range(n):
    for j in range(i):
        print(j+1,end="")
    print()

#5row * 5column 1-5 repeat order
n=5
for i in range(n):
    for j in range(i+1):
        print(i+1,end="")
    print()
print()

#5row * 5column * dec order
n=5
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()

#5row * 5column 5-1 dec order
n=5
for i in range(n):
    for j in range(n-i):
        print(j+1,end="")
    print()