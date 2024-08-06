'''
### Assignment 4: Fuel Check and Basic Exception Handling
**Required Knowledge**: Class Methods, Basic Exception Handling
**Instructions**:
1. Extend the `Car` class by adding an attribute `fuel_level` that represents the car's current fuel level.
2. Add a method named `check_fuel` that raises a `ValueError` if `fuel_level` is less than 5.
3. Implement a method named `drive` that reduces the `fuel_level` by a certain amount and calls `check_fuel`.
4. Test this by driving the car and catching the `ValueError` if the fuel level gets too low.
'''

class Car:
	def __init__(self, make=None, model=None, fuel_level=0):
		self.make = make
		self.model = model
		self.fuel_level = fuel_level

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

	def check_fuel(self):
		if self.fuel_level < 5:
			raise ValueError(f"Fuel level is too low ({self.fuel_level}). Please refuel.")

	def drive(self, distance):
		fuel_consumption = distance * 0.2
		self.fuel_level -= fuel_consumption
		try:
			self.check_fuel()
			print(f"Drove {distance} km. Fuel level: {self.fuel_level} units.")
		except ValueError as e:
			print(f"Error: {e}")

# Test the method
car1 = Car("Toyota", "Camry", fuel_level=10)
car1.print_car_info()
car1.start_engine()
car1.drive(10)
car1.drive(10)
car1.drive(10)
car1.drive(10)
car1.drive(10)
car1.drive(10)

print()

car2 = Car("Unknown", "Aristo", fuel_level=4)
car2.print_car_info()
car2.start_engine()
car2.drive(5)
