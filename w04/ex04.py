'''
### Assignment 4: Implementing Age Manipulation Methods
1. **Add Method**: Create a method `have_birthday` that increments the `age` attribute by 1 and prints a birthday message.
2. **Display Age**: Modify the `display_info` method to also include a message if the age is 18 or above.
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
	
test = Person("Ryanaja", 19)
test.greet()
test.update_contact_info("BKK", "11-009")
test.have_birthday()
test.display_info()