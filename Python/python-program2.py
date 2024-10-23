# Write a program to input radius of a circle and print its area and perimeter

import math

radius = int(input("Enter the Radius of the cirlce: "))

def area(radius):
    area = math.pi * radius**2
    print(area)

area(radius)

def perimeter(radius):
    perimeter = math.pi * 2 * radius
    print(perimeter)

perimeter(radius)