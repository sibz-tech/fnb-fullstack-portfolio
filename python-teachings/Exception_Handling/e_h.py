# Exception Handling in Python
# Exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.

try:
    print(x)
# except NameError:
#     print("Variable x is not defined")
# except: 
#     print("An exception occurred")
#except:
#    print("Something went wrong")
#finally: # Finally block will always be executed regardless if exception occurs or not
#    print("The 'try except' is finished")

# Else block gets exceuted if no exception occurs in try block
except NameError:
    print("Variable x is not defined")
else:
    print("Everything went wrong")

# Python supports raising exceptions manually using the raise keyword.
# This throws an exception if particular condition is met.

x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero") # Raise an exception if condition is met- Won't print anything but instead raise an error message

# Try, Except, Finally, Else, Raise are keywords used for exception handling in Python.
# These help to create a robust program and resilient code that can handle errors gracefully without crashing.

