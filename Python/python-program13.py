# Write a program to input the value of n and run the loop from 1 to n, and find the numbers which are prime.
n = int(input("Enter the value of n:"))
for i in range (1, n+1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(f"{i} is a prime number.")