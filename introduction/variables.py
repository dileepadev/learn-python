# Basic Data Types


# String
message = "Hello, World!"
print(message)

first_name = "Dileepa" # Double quotes
last_name = 'Bandara' # Single quotes
job_title = "Dileepa's Job is Developer" # Using single quotes inside double quotes
address = 'Dileepa\'s Address is "123 Main St"' # Using escape character for single quote and double quotes inside single quotes
description = '''Dileepa is a software developer.
He loves coding and learning new technologies.''' # Triple quotes for multi-line string
another_description = """Dileepa is a software developer.
He loves coding and learning new technologies.""" # Triple double quotes for multi-line string

print(first_name)
print(last_name)
print(job_title)
print(description)
print(another_description)

print("My name is " + first_name + " " + last_name) # Concatenation
print("My name is",first_name, last_name) # Comma separated
print(f"My name is {first_name} {last_name}") # f-string
print("My name is {} {}".format(first_name, last_name)) # format method


# Decimal Numbers
# Integer
age = 28
# Float
average_commits_per_day = 5.5
print(age)
print(average_commits_per_day)

# Boolean
is_developer = True
experienced = False
print(is_developer)
print(experienced)


# None
middle_name = None
print(middle_name)


# Type Checking
print(type(message)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(average_commits_per_day)) # <class 'float'>
print(type(is_developer)) # <class 'bool'>
print(type(middle_name)) # <class 'NoneType'>