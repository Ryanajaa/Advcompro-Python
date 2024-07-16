'''
**Homework 3:  Adding Dictionary Items in a List of Dictionaries**
Objective: Practice adding items in dictionaries within a list.
'''

# 1. Using data from the homework 2.
students = [
	{"name": "Alice", "age": 20, "grade": 85, "major": "Physics"},
	{"name": "Bob", "age": 22, "grade": 90, "major": "Chemistry"},
	{"name": "Charlie", "age": 19, "grade": 78, "major": "Mathematics"},
	{"name": "Diana", "age": 21, "grade": 92, "major": "Biology"}
]

# 2. Add a new key "graduation_year" with a value to each student's dictionary. Assume all students are expected to graduate in 2024.
for student in students:
	student["graduation_year"] = 2024
	
# 3. Remove the key "age" from each student's dictionary.
for student in students:
	del student["age"]

'''
4. Print the updated list of students.
	Expected Output:
	{'name': 'Alice', 'grade': 85, 'major': 'Physics', 'graduation_year': 2024}
	{'name': 'Bob', 'grade': 90, 'major': 'Chemistry', 'graduation_year': 2024}
	{'name': 'Charlie', 'grade': 78, 'major': 'Mathematics', 'graduation_year': 2024}
	{'name': 'Diana', 'grade': 92, 'major': 'Biology', 'graduation_year': 2024}
'''
for student in students:
	print(student)