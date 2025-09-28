# Functions- Allow you to encapsulate a code to reuse it later
# Define a function: def greet(name):
'''
# 1. Call a function: greet("Alice")
def greet(name): # Greet is the function name, name is the parameter
    print(f"Hello, {name}!") 
greet("Alice") # Calling the function with argument "Alice"

# 2. Function with return value
def add(a, b): # Function to add two numbers
    return a + b
result = add(5, 3) # Calling the function with arguments 5 and 3
print(result) # Output: 8
'''

# 3. Recursive function to calculate factorial-function that calls itself
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def greet(name, greeting="Hello"): # Default parameter greeting
    print(f"{greeting}, {name}!")

greet("Bob") # Uses default greeting
greet("Bob", "Good morning") # Overrides default greeting
