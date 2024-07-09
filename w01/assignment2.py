'''
Assignment 2: String Manipulation
Objective: Learn various string operations and methods.
'''

#1.	Create a string variable named sentence with the value “Python programming is fun”.
sentence = str("Python programming is fun")

#2.	Convert the string to uppercase and print it.
#	use upper() to returns a string where all characters are in upper case.
cap = sentence.upper()
print(cap)

#3.	Replace the word “fun” with “awesome” and print the new sentence.
#	use replace() to replace a substring with another string.
replace = sentence.replace("fun", "awesome")
print(replace)

#4.	Split the sentence into a list of words and print it.
#	use split() to splits a string into a list.
split = sentence.split()
print(split)