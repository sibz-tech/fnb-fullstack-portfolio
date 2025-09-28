# A dictionary is a collection of key-value pairs.
# They are indexed by keys, which can be of any immutable type (like strings, numbers, or tuples).

my_dict = {'apple' : 3, 'banana' : 5, 'orange' : 2} # Colon separates key and value, comma separates pairs

print(my_dict['apple'])  # Output: 3 - Trying to find the value attached to the key

my_dict['grapes'] = 4  # Updating the value for key 'grapes'
print(my_dict)  # Output: {'apple': 3, 'banana': 5, 'orange': 2, 'grapes': 4}

# Modify existing key-value pair
my_dict['banana'] = 7
print(my_dict)  # Output: {'apple': 3, 'banana': 7, 'orange': 2, 'grapes': 4}