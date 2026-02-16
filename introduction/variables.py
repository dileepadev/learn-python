# Basic Data Types


# String
message = "Hello, World!"
print(message)

first_name = "Dileepa" # Double quotes
last_name = 'Bandara' # Single quotes
job_title = "Dileepa's Job is Developer" # Using single quotes inside double quotes

print(first_name)
print(last_name)
print(job_title)

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