# write a program to print reverse of a number entered by the user
n = int(input("Enter the number:"))
reverse = 0
while(n > 0):
    reverse = (reverse * 10) + (n % 10)
    n = n // 10
print(f"The reverse of {n} is {reverse}")