'''
### Assignment 10: Adding a Diagnostics Method
**Required Knowledge**: Basic Multi-threading
**Instructions**:
1. Extend the `Car` class by adding a method named `drive`. This method should contain a while loop that delays for 2 seconds per iteration, prints "Driving... Speed: {self.speed} km/h", and decreases the fuel level by 1 each time it loops.
2. Use threading to set the target of the thread as the `drive` method so that driving can occur in another thread.
3. Test to ensure that both the diagnostics and drive methods run simultaneously. The message from the diagnostics should be printed every second, while a new thread for driving should print the driving message every 2 seconds.
'''

import threading
import time

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
	
	def diagnostics(self):
		print("-------------------------------")
		print(f"fuel_level: {self.fuel_level} unit\nspeed     : {self.speed} km/h")
	
	def drive(self):
		while True:
			if self.fuel_level <= 0:
				break
			print(f"Driving... Speed: {self.speed} km/h")
			self.fuel_level -= 1
			time.sleep(2)  # Delay for 2 seconds

car1 = Car(make="Toyota", model="Camry", fuel_level=10, speed=60)

# Create a thread for driving
drive_thread = threading.Thread(target=car1.drive)
drive_thread.start()  # Start the thread

while True:
	car1.diagnostics()

	time.sleep(1)  # Delay for 1 second
