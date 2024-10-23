for i in range(1,5):
    for k in range(i,5):
        print(" ", end="")
    for j in range(1,i+1):
        if i==1 or i==4:
            print("*", end=" ")
        elif j==1 or j==i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
