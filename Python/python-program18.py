n = 25

for i in range(1,n):
    for k in range(i,n):
        print(" ", end="")
    for j in range(1,i+1):
        print("*", end=" ")
    print()