# FOR Loop Control Statements: Control the flow of execution within loops using 'break', 'continue', and 'pass' statements

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break  # Exits out of the loop if cherry fruit is found
    print(fruit)

print()

for fruit in fruits:
    if fruit == "cherry":
        continue  # Skips cherry and moves to the next iteration
    print(fruit)

print()

for fruit in fruits:
    if fruit == "cherry":
        pass  # A placeholder (for transformation of data), no action is needed for cherry- Tells python to do nothing when it encounters cherry
    print(fruit)

