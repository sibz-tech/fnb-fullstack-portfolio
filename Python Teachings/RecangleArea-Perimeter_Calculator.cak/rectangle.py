# RECTANGLE AREA AND PERIMETER CALCULATOR- using functions and modules
# The task is to ask user to input the length and width of a rectangle
# and then calculate the area and perimeter of the rectangle.

import calculate

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculate.area(length, width)
perimeter = calculate.perimeter(length, width)
# Importing calls the functions from calculate.py

print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")

