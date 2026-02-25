# Lists

# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Accessing elements
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[-1]) # Output: cherry

# Modifying elements
fruits[0] = "orange"
print(fruits)

# Adding elements
fruits.append("grape")
print(fruits)

# Removing elements
fruits.remove("banana")
print(fruits)

# List length
print(len(fruits))

# Iterating through a list
for fruit in fruits:
    print(fruit)

# Checking the type of a list
print(type(fruits)) # Output: <class 'list'>

# List methods
numbers = [1, 3, 2, 5, 4]
print(numbers) # Output: [1, 3, 2, 5, 4]
numbers.append(6) # Adds 6 to the end of the list
print(numbers) # Output: [1, 3, 2, 5, 4, 6]
numbers.insert(2, 10) # Inserts 10 at index 2
print(numbers) # Output: [1, 3, 10, 2, 5, 4, 6]
print(numbers.count(3)) # Output: 1 (counts the occurrences of 3)
print(numbers.index(4)) # Output: 5 (returns the index of the first occurrence of 4)
numbers.sort() # Sorts the list in ascending order
print(numbers)
numbers.reverse() # Reverses the order of the list
print(numbers)
numbers.remove(3) # Removes the first occurrence of 3
print(numbers)

# Accessing a sublist (slicing)
devices = ["laptop", "smartphone", "tablet", "smartwatch", "desktop", "printer", "router", "monitor", "keyboard", "mouse"]
print(devices) # Output: ['laptop', 'smartphone', 'tablet', 'smartwatch', 'desktop', 'printer', 'router', 'monitor', 'keyboard', 'mouse']
print(devices[1:3]) # Output: ['smartphone', 'tablet'] (slices from index 1 to 2)
print(devices[:2])  # Output: ['laptop', 'smartphone'] (slices from the beginning to index 1)
print(devices[2:])  # Output: ['tablet', 'smartwatch', 'desktop', 'printer', 'router', 'monitor', 'keyboard', 'mouse'] (slices from index 2 to the end)
print(devices[-2:]) # Output: ['keyboard', 'mouse'] (slices the last two elements)
print(devices[::2]) # Output: ['laptop', 'tablet', 'desktop', 'router', 'keyboard'] (slices every second element)
print(devices[1::3]) # Output: ['smartphone', 'smartwatch', 'monitor'] (slices every third element starting from index 1)