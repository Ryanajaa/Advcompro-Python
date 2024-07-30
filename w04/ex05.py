'''
#### Assignment 5: Inheritance
Required Knowledge: Inheritance
1. Define a subclass `Student` that inherits from the `Person` class.
2. Add an attribute `student_id` to the `Student` class.
3. Instantiate an object of the `Student` class and print all its attributes.
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
    
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

student = Student("Ryanaja", "19", "66011009", "BKK", "11-009")
student.display_info()