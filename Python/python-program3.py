# Write a program to input length ad bradth. Calculate area and perimeter of rectangle.

length = int(input("Enter the length of Rectangle: "))
breadth = int(input("Enter the breadth of the Rectangle: "))

def area(length, breadth):
    area = length * breadth
    print("Area of the rectangle will be equal to: ", area)

area(length, breadth)

def perimeter(length, breadth):
    perimeter = 2 * length + 2* breadth
    print("The perimeter of the rectangle will be equal to: ", perimeter)

perimeter(length, breadth)