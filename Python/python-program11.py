# Write a program to print the Fibonacci series.

n = int(input("Enter the value of n"))

first = 0
second = 1

for i in range(0,n):
    third = first + second
    print(third)
    first, second = second, third