# Lesson 1: Hello World and Variables

# 1. Printing to the console
# The print() function is used to output text to the console.
print("Hello, World!")

# 2. Variables
# Variables are containers for storing data values.
# In Python, you don't need to declare the type of a variable.

# String variable
message = "Welcome to Python learning!"
print(message)

# Integer variable
age = 25
print("Age:", age)

# Float variable (decimal numbers)
price = 19.99
print("Price:", price)

# Boolean variable
is_learning = True
print("Is learning Python?", is_learning)

# 3. Dynamic Typing
# You can change the type of data a variable holds.
variable = 100
print("Variable is now a number:", variable)

variable = "Now I'm a string"
print("Variable is now a string:", variable)

# 4. String Formatting (f-strings)
# A convenient way to embed variables inside strings.
name = "Alice"
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)
