# Write a program to display factorial of the number entered by the user

n = int(input("Enter the number to get factorial:"))
fact = 1
if n ==0:
    print(f"Factorial of {n} is {fact}")
else:
    i=1
    while i <= n :
        fact = fact * i
        i += 1
    print(f"Factorial of {n} is {fact}")