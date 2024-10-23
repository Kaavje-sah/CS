# Write a program to input an email id and check the email ids entered in the correct form. For examle, should contain @ and a domain after the @ symbol.
# The program should also check if the email id is in the correct format.

# email = input("Enter the e-mail")
# list = email.partition("@")
# domain = list[2]
# if "@" in email and '.' in domain :
#     print("Email is in correct format")
# else:
#     print("Email is not in correct format")

# WAP to input  a string and find the digits in the string. If the digit is found, then add the elements,  otherwise print the string is not in correct format.

# str = input("Enter a string: ")
# if any(char.isdigit() for char in str):
#     print("The sum of digits in the string is: ", sum(int(digit) for digit  in str if digit.isdigit()))
# else:
#     print("The string is not in correct format")  # Output: The string is not in  correct format

# WAP to create a file named as file.txt to store the name of the students entered by the user

f = open("E:\\file.txt", "+wt")
for i in range(0,5):
    name = input("Enter the name of the student: ")
    f.write(name + "\n")
f.close()
