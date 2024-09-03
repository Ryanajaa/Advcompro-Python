'''
Assignment 10: Dictionary Basics
Objective: Learn how to create and use dictionaries in Python.
'''

#1.	Create a dictionary named student with keys: “name”, “age”, “grade”.
student = {
	"name": str(), 
	"age": int(),
	"grade": int()
}

#2.	Set the values of the dictionary to your name, age, and a grade of your choice.
student["name"] = "Jitpanu"
student["age"] = 20
student["grade"] = 99

#3.	Print the dictionary.
print(student)

#4.	Add a new key-value pair: “school” with the value of your school name.
student.update({"school": "KMITL"})

#5.	Remove the key “grade” from the dictionary and print the updated dictionary.
del student["grade"]
print(student)
