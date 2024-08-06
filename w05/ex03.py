'''
### Assignment 3: Adding More Attributes and Methods
1. **Add Attributes**: Extend the `Person` class to include `address` and `phone_number` attributes.
2. **Add Method**: Create a method `update_contact_info` that updates the `address` and `phone_number` attributes.
3. **Display Information**: Add a method `display_info` that prints all the attributes of the `Person` object.
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

	def display_info(self):
		print(f"Name: {self.name}")
		print(f"Age: {self.age}")
		print(f"Address: {self.address}")
		print(f"Phone Number: {self.phone_number}")
	
test = Person("Ryanaja", 19)
test.greet()
test.update_contact_info("BKK", "11009")
test.display_info()