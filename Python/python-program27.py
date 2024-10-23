# Reverse of a number entered by a number

# try:
#     number = int(input("Enter number: "))
# except:
#     print("Enter a valid number")

# reverse = str(number)[::-1]
# print(int(reverse))

# To check the number entered by a user is prime or not
# try: 
#     number = int(input("Enter number: "))
# except:
#     print("Enter a valid number")

# i = 1

# try:
#     while i < number:
#         if number % i == 0:
#             i+=1
#             break
#         else:
#             print(f"{number} is prime.")
#     print(f"{number} is not prime")
# except:
#     print(" number is not positive duh'/")

# Input the value of x and n, and print the sum of the following series.

try:
    x = int(input("Enter the value of x: "))
    n = int(input("Enter the value of n: "))
except:
    print("Enter the values of x as integer and n as integer duh.")

S = (1-((-x)**n))/(1+x)
print(S)