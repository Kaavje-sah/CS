# Create the following list using a for loop:
# a) A lsit consisting of the integers 0 to 49.
# b) A list containing the squares of the integers 1 to 50.
# c) The list that ends with 26 copies of z.

A = []
B = []
C = []

for i in range(0,50):
    A.append(i)
print(A)
for i in range(0,51):
    B.append(i**2)
print(B)
for i in range(65,91 ):
    C.append(f"{chr(i)* (i-64)}")
print(C)