'''
### Assignment 3: Adding Methods and Exception Handling
**Required Knowledge**: Class Methods, Basic Exception Handling
**Instructions**:
1. Extend the `Car` class by adding a method named `start_engine`.
2. Inside `start_engine`, raise an exception if the car's `make` is `"Unknown"`. Use the built-in `ValueError`.
3. Catch the exception in a `try...except` block and print an appropriate message.
4. Test this by creating a car with `make="Unknown"` and calling `start_engine`.
'''

class Car:
	def __init__(self, make=None, model=None):
		self.make = make
		self.model = model

	def print_car_info(self):
		try:
			if self.make is None or self.model is None:
				raise AttributeError("Make or model attribute is not set.")
			print(f"Make: {self.make}, Model: {self.model}")
		except AttributeError as e:
			print(f"Error: {e}")

	def start_engine(self):
		try:
			if self.make == "Unknown":
				raise ValueError("Cannot start engine: Car make is 'Unknown'.")
			print(f"The engine of the {self.make} {self.model} is now running.")
		except ValueError as e:
			print(f"Error: {e}")

# Test the method
car1 = Car("Toyota", "Camry")
car1.print_car_info()
car1.start_engine()
print()
car2 = Car("Unknown", "Aristo")
car2.print_car_info()
car2.start_engine()
