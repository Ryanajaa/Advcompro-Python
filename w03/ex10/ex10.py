'''
**Assignment 10: Filtering Eligible Children for a Fun Park (Using Lambda Function)**
Student can incorporate a lambda function into the list comprehension for filtering eligible children.
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

# 2. Use a l    ion named criteria to define the eligibility criteria. `criteria` is a lambda function that takes a dictionary `child` and returns `True` if the child's age is greater than 3 and height is greater than 100 cm.
criteria = lambda child: child['age'] > 3 and child['height'] > 100
eligible_children = list(filter(criteria, children))

# 3. Print the `eligible_children` list to display the names, ages, and heights of the eligible children.
print("Eligible children for the fun park:", eligible_children)

# **Expected Output:**
# Eligible children for the fun park: [{'name': 'Bob', 'age': 4, 'height': 105}, {'name': 'David', 'age': 5, 'height': 102}]