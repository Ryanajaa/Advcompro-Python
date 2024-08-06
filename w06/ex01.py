'''
### Assignment 1: Creating a Class
**Required Knowledge**: Class Definition, Object Instantiation
**Instructions**:
1. Define a class named `Car`.
2. Add two attributes: `make` and `model`.
3. Instantiate an object of the `Car` class with a specific `make` and `model`. Example: `my_car = Car("Toyota", "Corolla")`.
4. Print the object's attributes.
Example of create an object in main program
```
my_car = Car("Toyota", "Corolla")
print(f"Make: {my_car.make}, Model: {my_car.model}")
```
'''

class Car:
	def __init__(self, make, model):
		self.make = make
		self.model = model

my_car = Car("Toyota", "Camry")
print(f"Make: {my_car.make}, Model: {my_car.model}")