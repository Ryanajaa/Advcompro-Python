'''
**Assignment 9: Filtering Eligible Children for a Fun Park**
Imagine you have a list of dictionaries where each dictionary contains a child's name, age, and height. You need to create a new list of children who are eligible to join a fun park. A child is eligible if their age is greater than 3 and their height is greater than 100 cm.
**Instructions:**
'''

# 1. Define a list of dictionaries named `children`, where each dictionary contains a `name`, `age`, and `height`.
children = [
	{"name": "Alice", "age": 2, "height": 95},
	{"name": "Bob", "age": 4, "height": 105},
	{"name": "Charlie", "age": 3, "height": 110},
	{"name": "David", "age": 5, "height": 102},
	{"name": "Eve", "age": 6, "height": 99}
]

# 2. Use a list comprehension to create a new list named `eligible_children` that:
#	- Filters the children to include only those with age greater than 3 and height greater than 100 cm.
eligible_children = [child for child in children if child['age'] > 3 and child['height'] > 100]

# 3. Print the `eligible_children` list to display the names, ages, and heights of the eligible children.
print("Eligible children for the fun park:", eligible_children)

# **Expected Output:**
# Eligible children for the fun park: [{'name': 'Bob', 'age': 4, 'height': 105}, {'name': 'David', 'age': 5, 'height': 102}]