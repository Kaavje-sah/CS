# WAP to print every integer between 1 and n, that are divisble by m. also, report whether the number is even or odd.

n = int(input("Enter the maximum no: "))
m = int(input("Enter the divisor: "))
for i in range(2, n, 1):
    if (i % m == 0) and (i != m):
        print(f"{i} is a divisor of {m}")
        if i%2 ==0:
            print(f"{i} is an even no.")
        else:
            print(f"{i} is a odd no")