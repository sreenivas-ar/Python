print("------------------Pattern 1------------------------")
print("*")

print("------------------Pattern 2------------------------")
for i in range(0,5):
    print("*", end= " ")
print()

print("------------------Pattern 3------------------------")
for i in range(0,5):
    print("*")

print("------------------Pattern 4------------------------")
for i in range(0,5):
    for j in range(0,5):
        print("*", end="")
    print()

print("------------------Pattern 5------------------------")
for i in range(1,6):
    for j in range(1,6):
        print(i, end="")
    print()

print("------------------Pattern 6------------------------")
for i in range(1,6):
    for j in range(1,6):
        print(j, end="")
    print()

print("------------------Pattern 7------------------------")
for i in range(1,6):
    for j in range(1,6):
        if i==2 or i==3 or i==4:
            if j==1 or j==5:
                print("*", end="")
            else:
                print(" ",end="")
        else:
            print("*", end="")
    print()
#OR
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print("------------------Pattern 8------------------------")
count=0
for i in range(5):
    for j in range(5):
        count+=1
        if count<10:
            print("0"+str(count),end=" ")
        else:
            print(count,end=" ")
    print()

print("------------------Pattern 9------------------------")
for i in range(1,6):
    count=i
    for j in range(5):
        if count<10:
            print("0"+str(count),end=" ")
        else:
            print(count, end=" ")
        count+=i
    print()

print("------------------Pattern 10------------------------")
for i in range(5):
    for j in range(5):
        print(i+j+1,end=" ")
    print()

print("------------------Pattern 11------------------------")
for i in range(5):
    for j in range(5):
        if j<=i:
            print("*", end=" ")
        print(end="")
    print()

print("------------------Pattern 12------------------------")
for i in range(5):
    for j in range(5):
        if j<=i:
            print(j+1, end=" ")
        print(end="")
    print()

print("------------------Pattern 13------------------------")
for i in range(5):
    for j in range(5):
        if j<=i:
            print(i+1, end=" ")
        print(end="")
    print()

print("------------------Pattern 14------------------------")
#print("Enter a Value: ")
#n=int(input())
n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for k in range(j,n):
        print("*",end="")
    print()

#print("Item 1", "Item 2", "Item 3", sep="-")
