'''
Assignment 5: List insert() Method
Objective: Learn how to insert elements at specific positions in a list using insert().
'''

#1.	Create a list named numbers containing the integers 1, 2, 4, 5, 6.
numbers = [1, 2, 4, 5, 6]

#2.	Use the insert() method to add the number 3 between 2 and 4.
#	list.insert(position, element)
numbers.insert(2, 3)

#3.	Print the list.
print(numbers)

#4.	Insert the number 0 at the beginning of the list.
numbers.insert(0, 0)

#5.	Print the final list of numbers.
print(numbers)