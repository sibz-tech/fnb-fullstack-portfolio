# Sets: A set is a collection which is unordered, unindexed, and does not allow duplicate values.
# Sets are Immutable, meaning that you can add or remove items after its creation.

'''
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set.add(6)  # Adding an element to the set
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

my_set.remove(3)  # Removing an element from the set
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Sets allow several operations like Union, Intersection, Difference, and Symmetric Difference.

''' #USE THREE SINGLE QUOTES TO COMMENT MULTIPLE LINES OUT TO NOT SHOW ON TERMINAL RUN

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union- Combines both sets, removing duplicates
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection- Elements common to both sets
inter_set = set1.intersection(set2)
print(inter_set)  # Output: {3}

# Difference- Elements present in set1 but not in set2
diff_set = set1.difference(set2)
print(diff_set)  # Output: {1, 2}

# Sets are useful when you need to work with a collection of unique items and perform mathematical set operations.
# Can check for membership using 'in' keyword