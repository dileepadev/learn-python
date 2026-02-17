# Strings

# Types of Strings
single_quote_string = 'This is a string with single quotes.'
double_quote_string = "This is a string with double quotes."
triple_single_quote_string = '''This is a string with triple single quotes. 
It can span multiple lines.''' # Also known as a docstring or multi-line string
triple_double_quote_string = """This is a string with triple double quotes. 
It can also span multiple lines.""" # Also known as a docstring or multi-line string

print(single_quote_string)
print(double_quote_string)
print(triple_single_quote_string)
print(triple_double_quote_string)

# Skipping Escape Characters
escaped_string = 'This is a string with an escaped single quote: It\'s a nice day.'
escaped_string_double = "This is a string with an escaped double quote: He said, \"Hello!\""
print(escaped_string)
print(escaped_string_double)


# Methods for Strings
my_string = "Hello, World!"
print(my_string.upper()) # Output: "HELLO, WORLD!"
print(my_string.lower()) # Output: "hello, world!"
print(my_string.capitalize()) # Output: "Hello, world!"
print(my_string.title()) # Output: "Hello, World!"
print(my_string.strip()) # Output: "Hello, World!" (removes leading and trailing whitespace)
print(my_string.replace("World", "Python")) # Output: "Hello, Python!"
print(my_string.split(", ")) # Output: ["Hello", "World!"]
print(my_string.find("World")) # Output: 7 (index of the first occurrence of "World")
print(my_string.startswith("Hello")) # Output: True
print(my_string.endswith("!")) # Output: True
