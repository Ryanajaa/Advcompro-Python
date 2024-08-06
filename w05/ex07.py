'''
#### Assignment 7: Private Attributes and Methods
Required Knowledge: Encapsulation, Private Attributes
1. Add a private attribute `__salary` to the `Person` class and a method to set its value.
2. Add a method to retrieve the value of the `__salary` attribute.
3. Instantiate an object, set the salary, and print it using the retrieval method.
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

person = Person("Ryanaja", 19)
person.set_salary("20")
print(f"{person.name} salary: {person.get_salary()} Baht TwT")