# Write a program to input a number and print the table of the number
n = int(input("Enter number: "))
for i in range(1, 100000000001):
    print("%d x %d = %d" % (n, i, n*i))
a = int(input("Hello"))