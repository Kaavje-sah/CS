# Write a program to input 2 list such that their sizes are the and make a new list that has the elements of the corresponding elemnts of the lists.
L = eval(input("Enter list L: "))
M = eval(input("Enter list M: "))
try: 
    P = []
    if len(L) == len(M):
        for i in range(len(L)):
            P.append(L[i])
            j = M[i]
            while j not in P:
                P. append(j)
    print(P)
except:
    print("Both the strings have to be of equivalent length")