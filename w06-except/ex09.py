'''
### Assignment 9: Adding a Diagnosticss Method
**Required Knowledge**: Class Methods
**Instructions**:
1. Extend the `Car` class by adding a method named `diagnosticss` that prints various status information such as `fuel_level` and `speed`.
2. Test this method by creating an instance of the `Car` class and calling `diagnosticss` to print the car's status.
3. Call `diagnosticss` in a while loop in the main program to print every second. (Hint: use `time.sleep(1)` to delay).
'''
import time

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

	def accelerate(self, increase_speed):
		self.speed += increase_speed
		try:
			if self.speed > 120:
				raise OverSpeedError(f"OverSpeedError: Current speed {self.speed} exceeds the limit of 120.")
			print(f"Accelerated to {self.speed} km/h.")
		except OverSpeedError as e:
			print(f"Error: {e}")
	
	def diagnostics(self):
		print("-------------------------------")
		print(f"fuel_level: {self.fuel_level} unit\nspeed     : {self.speed} km/h")

# Test the method
car1 = Car("Toyota", "Camry", fuel_level=10, speed=100)
car1.print_car_info()
car1.start_engine()
car1.diagnostics()

while True:
    car1.diagnostics()
    time.sleep(1)