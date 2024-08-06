'''
### Assignment 6: Creating and Writing to a Text File Using the `with` Statement
**Required Knowledge**: File Handling, `with` Statement
**Instructions**:
1. Create a Python script named `write_color_file.py`.
2. Write a Python script to create and write to a file named `color.txt`. Add the word "red" using the `with` statement to safely handle the file operations. Use `file.write("red")` to write content to the file.
'''

def write_color_file():
	with open('color.txt', 'w') as file:
		file.write("red")

write_color_file()