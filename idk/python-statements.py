# statement 1
print('Hello')

# statement 2
x = 20

# statement 3
print(x)

# two statements in one line
l = 10; b = 5
print('Area of Rectangle:', l*b)

#Multi-line statements
addition = 10 + 20 + \
           30 + 40 + \
           50 + 60 + 70
print(addition)
#or
addition = (
    10 + 20 + 30 +
    40 + 50 + 60 +
    70
)
print(addition)

# create a function
def fun1(arg):
    pass

# Define a function
# function acceptts two numbers and return their sum
def addition(num1, num2):
    return num1 + num2  # return the sum of two numbers

# result is the return value
result = addition(10, 20)
print(result)

import datetime

# get current datetime
now = datetime.datetime.now()
print(now)