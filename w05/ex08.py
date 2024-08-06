'''
#### Assignment 8: Static Methods
Required Knowledge: Static Methods
1. Add a static method `is_adult` to the `Person` class that takes an age as an argument and returns `True` if the age is 18 or above, otherwise `False`.
2. Call the `is_adult` method from the class without creating an object.
'''

class Person:
	def __init__(self, name, age, address=None, phone_number=None):
		self.name = name
		self.age = age
		self.address = address
		self.phone_number = phone_number
		self.__salary = None

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
	
	def set_salary(self, salary):
		self.__salary = salary
	
	def get_salary(self):
		return self.__salary

	@staticmethod
	def is_adult(age):
		return age >= 18

print(Person.is_adult(20))
print(Person.is_adult(17))