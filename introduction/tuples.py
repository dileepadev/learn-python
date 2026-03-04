# Tuples

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple) # Output: (1, 2, 3, 4, 5)

# Printing the type of the tuple
print(type(my_tuple)) # Output: <class 'tuple'> 

# Accessing values in a tuple
print(my_tuple[0]) # Output: 1
print(my_tuple[1]) # Output: 2
print(my_tuple[2]) # Output: 3
print(my_tuple[3]) # Output: 4
print(my_tuple[4]) # Output: 5

# Modifying values in a tuple
# Tuples are immutable, which means you cannot modify their values after they are created.
# The following code will raise a TypeError:
# my_tuple[0] = 10 # Uncommenting this line will raise a TypeError

# Creating a tuple with duplicate values
my_tuple_with_duplicates = (1, 2, 2, 3, 4, 4, 5)
print(my_tuple_with_duplicates) # Output: (1, 2, 2, 3, 4, 4, 5) (duplicates are allowed in tuples)

# Add values to a tuple
# Since tuples are immutable, you cannot add values to a tuple. However, you can create a new tuple that combines the existing tuple with the new values.
my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4, 5)
print(new_tuple) # Output: (1, 2, 3, 4, 5)

# Removing specific values from a tuple
# Since tuples are immutable, you cannot remove specific values from a tuple. However, you can create a new tuple that excludes the values you want to remove.
my_tuple = (1, 2, 3, 4, 5)
# Create a new tuple that excludes the value 3
new_tuple = tuple(x for x in my_tuple if x != 3)
print(new_tuple) # Output: (1, 2, 4, 5)

# Sorting a tuple
# Tuples do not have a built-in method for sorting, but you can convert it to a list, sort it, and convert it back to a tuple.
my_tuple = (5, 3, 1, 4, 2)
sorted_tuple = tuple(sorted(my_tuple))
print(sorted_tuple) # Output: (1, 2, 3, 4, 5)