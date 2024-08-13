'''
### Assignment 5: Raising and Handling Custom Exceptions
**Required Knowledge**: Custom Exceptions, Raising Exceptions
**Instructions**:
1. Create a custom exception named `OverSpeedError`.
2. Add an attribute `speed` to the `Car` class.
3. Implement a method named `accelerate` that raises `OverSpeedError` if the car's speed exceeds 120.
4. Test this by calling `accelerate` and catching the `OverSpeedError` to print a warning message.
'''

# Custom exception
class OverSpeedError(Exception):
	def __init__(self, message="Speed limit exceeded!"):
		self.message = message
		super().__init__(self.message)

class Car:
	def __init__(self, make=None, model=None, fuel_level=0, speed=0):
		self.make = make
		self.model = model
		self.fuel_level = fuel_level
		self.speed = speed

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

	def accelerate(self, increase_speed):
		self.speed += increase_speed
		try:
			if self.speed > 120:
				raise OverSpeedError(f"OverSpeedError: Current speed {self.speed} exceeds the limit of 120.")
			print(f"Accelerated to {self.speed} km/h.")
		except OverSpeedError as e:
			print(f"Error: {e}")

# Test the method
car1 = Car("Toyota", "Camry", fuel_level=10, speed=100)
car1.print_car_info()
car1.start_engine()
car1.accelerate(15)
car1.accelerate(10)
car1.accelerate(10)