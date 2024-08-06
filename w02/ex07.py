'''
Assignment 7: List sort() Method
Objective: Learn how to sort elements in a list using sort().
'''

#1. Create a list named scores containing the following numbers: 88, 92, 75, 89, 78.
score = [88, 92, 75, 89, 78]

#2. Use the sort() method to sort the list in ascending order.
score.sort()

#3. Print the sorted list.
print(score)

#4. Sort the list in descending order and print it.
score.sort(reverse=True)
print(score)

#5. Create a list of strings named names containing “Alice”, “Bob”, “Charlie”, “David”, “Eve” and sort it in alphabetical order.
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names.sort()
print(names)