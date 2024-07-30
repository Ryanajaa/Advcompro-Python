'''
#### Assignment 6: Overriding Methods
Required Knowledge: Method Overriding
1. Override the `greet` method in the `Student` class to include the student ID in the greeting.
2. Call the `greet` method from an instantiated `Student` object.
'''

class Person:
	def __init__(self, name, age, address=None, phone_number=None):
		self.name = name
		self.age = age
		self.address = address
		self.phone_number = phone_number

	def greet(self):
		print(f"Hello, my name is {self.name} and I am {self.age} years old.")
		
	def update_contact_info(self, address, phone_number):
		self.address = address
		self.phone_number = phone_number

	def have_birthday(self):
		self.age += 1
		print(f"HBD!!!!, {self.name}! You are now {self.age} years old.")

	def display_info(self):
		print(f"Name: {self.name}")
		print(f"Age: {self.age}")
		if self.age >= 18:
			print("You are an adult.")
		else:
			print("You are a minor.")
		print(f"Address: {self.address}")
		print(f"Phone Number: {self.phone_number}")
	
class Student(Person):
	def __init__(self, name, age, student_id, address=None, phone_number=None):
		super().__init__(name, age, address, phone_number)
		self.student_id = student_id

	def greet(self):
		print(f"Hello, my name is {self.name}, I am {self.age} years old, and my student ID is {self.student_id}.")

	def display_info(self):
		super().display_info()
		print(f"Student ID: {self.student_id}")

student = Student("Ryanaja", 19, "66011009", "BKK", "11-009")
student.greet()