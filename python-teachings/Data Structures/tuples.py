# A tuple in python is a collection of audit elements which is ordered, immutable (unchangeable) and allows duplicate values.
# They are immutable, meaning that once a tuple is created, its elements cannot be changed, added, or removed.

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# Accessing elements in a tuple- use indexing to print (starting from 0)
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3

#Use negative indexing to print to start from the end of list & tuples (starting from -1)
print(my_tuple[-1])  # Output: 5

# Operations on tuples: Concatenation, Repetition (Multiplication), Membership Testing, Slicing

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
conc_tuple = tuple1 + tuple2
print(conc_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition (Multiplication)
rep_tuple = tuple1 * 3
print(rep_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# With tuples you can't add or remove elements, it's unchangeable.
# Use it to strore data that shouldn't be changed.





