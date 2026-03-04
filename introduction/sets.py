# Sets

# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set) # Output: {1, 2, 3, 4, 5}

# Creating a set with duplicate values
my_set_with_duplicates = {1, 2, 2, 3, 4, 4, 5}
print(my_set_with_duplicates) # Output: {1, 2, 3, 4, 5} (duplicates are removed)

# Printing the type of the set
print(type(my_set)) # Output: <class 'set'>

# Accessing values in a set
# Sets do not support indexing, so you cannot access elements by their position.
# However, you can check if an element exists in the set.
print(3 in my_set) # Output: True
print(6 in my_set) # Output: False

# Adding an element to a set
my_set.add(6)
print(my_set) # Output: {1, 2, 3, 4, 5, 6}

# Removing an element from a set
my_set.remove(2)
print(my_set) # Output: {1, 3, 4, 5, 6}

# Sorting a set
# Sets do not maintain any order, so you cannot sort a set directly. However, you can convert it to a list and sort it.
my_set = {5, 3, 1, 4, 6}
sorted_set = sorted(my_set)
print(sorted_set) # Output: [1, 3, 4, 5, 6]

# Converting a list to a set
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set_from_list = set(my_list)
print(my_set_from_list) # Output: {1, 2, 3, 4, 5} (duplicates are removed)