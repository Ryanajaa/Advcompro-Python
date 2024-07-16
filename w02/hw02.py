'''
**Homework 2: Lists of Dictionaries in Python**
**Objective**: To practice creating, manipulating, and analyzing lists of dictionaries in Python. This assignment will help you understand how to work with complex data structures and apply various Python techniques.
'''

'''
1. Create a list named students that contains dictionaries. Each dictionary should represent a student with the following keys: name, age, grade, and major.
	Example:
	students = [
  	  {"name": "Alice", "age": 20, "grade": 85, "major": "Physics"},
  	  {"name": "Bob", "age": 22, "grade": 90, "major": "Chemistry"},
  	  {"name": "Charlie", "age": 19, "grade": 78, "major": "Mathematics"},
  	  {"name": "Diana", "age": 21, "grade": 92, "major": "Biology"}
	]
'''
students = [
	{"name": "Alice", "age": 20, "grade": 85, "major": "Physics"},
	{"name": "Bob", "age": 22, "grade": 90, "major": "Chemistry"},
	{"name": "Charlie", "age": 19, "grade": 78, "major": "Mathematics"},
	{"name": "Diana", "age": 21, "grade": 92, "major": "Biology"}
]

# 2. Using a for loop to update Alice's grade to 87. Iterate over the list and update the grade for the student named Alice.
for student in students:
	if student["name"] == "Alice":
		student["grade"] = 87

# 3. Using a for loop to update Diana's major to "Programming". Iterate over the list and update the major for the student named Diana.
for student in students:
	if student["name"] == "Diana":
		student["major"] = "Programming"
	
# 4. Print the updated list of students. After making the updates, use a for loop to print each dictionary in the list to verify the changes.
# 	Expected output:
# 	students = [
#   	  {"name": "Alice", "age": 20, "grade": 87, "major": "Physics"},
#   	  {"name": "Bob", "age": 22, "grade": 90, "major": "Chemistry"},
#   	  {"name": "Charlie", "age": 19, "grade": 78, "major": "Mathematics"},
#   	  {"name": "Diana", "age": 21, "grade": 92, "major": "Programming"}
# 	  '''
for student in students:
	print(student)