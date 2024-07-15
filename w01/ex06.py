'''
Assignment 6: List pop() Method
Objective: Understand how to remove elements from a list using pop() and how to use the removed elements.
'''

#1.	Create a list named cities containing “New York”, “Los Angeles”, “Chicago”, “Houston”, “Phoenix”.
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

#2.	Use the pop() method to remove the last element from the list and store it in a variable.
#	pop() removes the element at the specified position. default is last position(-1)
last = cities.pop()

#3.	Print the variable holding the removed element.
print(last)

#4.	Use pop() to remove the first element from the list.
cities.pop(0)

#5.	Print the final list of cities.
print(cities)