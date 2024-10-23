# Write a program to input the value of A and B and print sum, mulitply, divide, and subtraction.

a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))

def question_1(a, b):
    print("The addition of A and B gives: ", a + b);
    print("The multiplication of A and B gives:", a * b)
    print("The Division of A and B gives: ", a / b);
    print("The Subtraction of A and B gives: ", a - b)

question_1(a, b)