# Loops- Allow us to execute a block of code multiple times: For Loop & While Loop
# For Loop: Used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and perform an action for each item in that sequence.
# While Loop: Repeats a block of code as long as a specified condition is true.

# For Loop Example:

fruits = ["apple", "banana", "cherry"]

for fruit in fruits: # Iterates over each item in the list 'fruits'
    print(fruit)

numbers = [1, 2, 3, 4, 5]

for number in numbers: # Iterates over each item in the list 'numbers'
    print(numbers) # Prints the entire list 'numbers'
    print(number) # Prints each individual number in the list 'numbers'

# While Loop Example: Execute a block of code as long as a specified condition is true.
# Using a while loop to print numbers from 1 to 5
count = 1

while count <= 5: # Condition to check
    print(count) # Print the current value of count
    count += 1 # Increments count by 1 to avoid infinite loop


