# Dictionaries

# Creating a dictionary
person = {"name": "Dileepa", "age": 28, "city": "Kurunegala"}

# Printing the dictionary
print(person) # Output: {'name': 'Dileepa', 'age': 28, 'city': 'Kurunegala'}

# Print the dictionary with key-value pairs
print(person.items()) # Output: dict_items([('name', 'Dileepa'), ('age', 28), ('city', 'Kurunegala')])

# Print the dictionary with formatted string
print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}") # Output: Name: Dileepa, Age: 28, City: Kurunegala

# Printing the type of the dictionary
print(type(person)) # Output: <class 'dict'>

# Accessing values
print(person["name"])  # Output: Dileepa
print(person["age"])   # Output: 28
print(person["city"])  # Output: Kurunegala

# Accessing all keys
print(person.keys())   # Output: dict_keys(['name', 'age', 'city'])

# Accessing all key as a list
print(list(person.keys())) # Output: ['name', 'age', 'city']

# Accessing all values
print(person.values()) # Output: dict_values(['Dileepa', 28, 'Kurunegala'])

# Accessing all values as a list
print(list(person.values())) # Output: ['Dileepa', 28, 'Kurunegala']

# Modifying values
person["age"] = 29
print(person) # Output: {'name': 'Dileepa', 'age': 29, 'city': 'Kurunegala'}

# Adding a new key-value pair
person["country"] = "Sri Lanka"
print(person) # Output: {'name': 'Dileepa', 'age': 29, 'city': 'Kurunegala', 'country': 'Sri Lanka'}

# Deleting a key-value pair
del person["city"]
print(person) # Output: {'name': 'Dileepa', 'age': 29, 'country': 'Sri Lanka'}

# Checking if a key exists
print("name" in person)  # Output: True
print("city" in person)  # Output: False

# Duplicate keys in a dictionary
# If you create a dictionary with duplicate keys, the last value will overwrite the previous ones.
duplicate_dict = {"key": "value1", "key": "value2"}
print(duplicate_dict) # Output: {'key': 'value2'} (the value 'value1' is overwritten by 'value2')