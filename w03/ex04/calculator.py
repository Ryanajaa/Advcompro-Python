'''
**Assignment 4: Defining Functions in Python**
Define and use functions in Python to perform specific tasks.
**Instructions:**
'''

# 1. Create a new Python file named `calculator.py`.
# 2. Define a function named `add` that takes two arguments and returns their sum.
def add(x, y):
	return x + y

# 3. Define a function named `subtract` that takes two arguments and returns their difference.
def subtract(x, y):
	return x - y

# 4. Define a function named `multiply` that takes two arguments and returns their product.
def multiply(x, y):
	return x * y

# 5. Define a function named `divide` that takes two arguments and returns their quotient.
def divide(x, y):
	return x / y

# 6. Write a main block that calls each function with sample inputs and prints the results.
x = int(10)
y = int(3)
print("Calculator")
print(add(x, y))
print(subtract(x, y))
print(multiply(x, y))
print(divide(x, y))