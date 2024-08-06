'''
Assignment 9: List Slicing
Objective: Learn how to slice lists to access sublists.
'''

#1.	Create a list named letters containing the first 10 letters of the alphabet. Ex. [A, B, C, D, ... ]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

#2.	Slice the list to get the first 5 letters and print the result.

#	first_five = letters[slice(5)] or
first_five = letters[0:5]
print(first_five)

#3.	Slice the list to get the last 5 letters and print the result.
last_five = letters[-5:]
print(last_five)

#4.	Reverse the list and print the result.
letters.sort(reverse=True)
print(letters)