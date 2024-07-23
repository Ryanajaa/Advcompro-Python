'''**Assignment 6: Importing Modules in Python**
Import and use modules in Python to enhance functionality.
Instructions:
'''
# 1. Create a new Python file named `string_operations.py`.
# 2. Define functions for common string operations:
#	- `reverse_string`: Reverses a given string.
def reverse_string(str):
	return str[::-1]

#	- `capitalize_string`: Capitalizes the first letter of a given string.
def capitalize_string(str):
	return str.capitalize()

#	- `lowercase_string`: Converts all characters in a given string to lowercase.
def lowercase_string(str):
	return str.lower()

#	- `uppercase_string`: Converts all characters in a given string to uppercase.
def uppercase_string(str):
	return str.upper()