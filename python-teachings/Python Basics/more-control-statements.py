# Control Statements: If, Else, Elif
# Compare two numbers & input values from user

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")

# This program helps to input values from the user and compare them using control statements.