# A list is a built-in data structure in Python that can hold an ordered collection of items.
# Lists are ordered, changeable, and allow duplicate values.
# They are defined by enclosing elements in square brackets [].

# Example of Python list- A list containing strings: They are zero-indexed.
fruits = ["apple", "banana", "cherry"]

# Accessing elements/index in a list
print(fruits[0])  # Output: apple

# Mutable/Changeable: You can change, add, and remove items in a list after it has been created.
fruits[1] = "blueberry"  # Changing the second item
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Python allows a range of functions to operate on lists, including:Removing and adding items, sorting, reversing, and more.

# Adding items to a list use append  method
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# Adding items at a specific index/position of list use insert method
fruits.insert(1, "kiwi")  # Inserting 'kiwi' at index 1/position 2 of list
print(fruits)  # Output: ['apple', 'kiwi', 'blueberry', 'cherry', 'orange']

# Removing items from a list use remove method- removes the first occurrence of a value.
fruits.remove("blueberry")
print(fruits)  # Output: ['apple', 'kiwi', 'cherry', 'orange']

# Sorting a list use sort method - Alphabetically for strings and numerically for numbers.
fruits.sort()
print(fruits)  # Output: ['apple', 'cherry', 'kiwi', 'orange']

# Sorting in descending order- Pass a reverse=True argument to the sort() method.
fruits.sort(reverse=True)
print(fruits)  # Output: ['orange', 'kiwi', 'cherry', 'apple']