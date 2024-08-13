'''
### Assignment 7: Reading from a Text File and Handling Exceptions
**Required Knowledge**: File Handling, with Statement, Exception Handling in Python
**Instructions**:
1. Continue from Assignment 5. Ensure you have the Car class ready with its current functionalities intact.
2. Create a Method: Add a method named read_color_from_file to your Car class. This method will be responsible for reading the car's color from an external file.
3. File Reading: Use a with statement to safely open and read the contents of the color.txt file created in Assignment 6. The file should contain a single word representing the car’s color. To retrieve the content, you can use file.read().strip().
4. Testing: Create a Car object and test the read_color_from_file method by providing the correct path to the color.txt file and ensuring it works as expected.
'''

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
		self.color = None

	def print_car_info(self):
		try:
			if self.make is None or self.model is None:
				raise AttributeError("Make or model attribute is not set.")
			print(f"Make: {self.make}, Model: {self.model}, Color: {self.color}")
		except AttributeError as e:
			print(f"Error: {e}")

	def main_read(self, file_path):
		with open(file_path, 'r') as file:
			self.color = file.read().strip()
			if self.color == "" or self.color == None:
				raise ValueError("No color")
			else:
				print(f"Car color read from file: {self.color}")
		return(f"the color is {self.color}")

	def read_color_from_file(self, file_path):
		try:
			self.main_read(file_path)
		except FileNotFoundError:
			print(f"Error: The file {file_path} was not found.")
		except ValueError as ve:
			print(ve)
		except Exception as e:
			print(f"Error: {e}")

# Test the method
car1 = Car("Toyota", "Camry")
# Reading color from file
car1.read_color_from_file('color.txt')
car1.print_car_info()