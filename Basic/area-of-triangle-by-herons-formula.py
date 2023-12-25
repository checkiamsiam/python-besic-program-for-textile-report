import math
# area of triangle using Heron's formula

a = float(input("Enter first side of triangle: "))
b = float(input("Enter second side of triangle: "))
c = float(input("Enter third side of triangle: "))
# calculate the semi-perimeter
s = (a + b + c) / 2
# calculate the area
area = math.sqrt( (s * (s - a) * (s - b) * (s - c)))

print("Area of triangle is:", area)