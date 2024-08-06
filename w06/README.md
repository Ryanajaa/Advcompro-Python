### Topic:
1. Basic Exception Handling
2. Raising Exceptions
3. Custom Exceptions
4. Context Managers using `with`
5. Multi-threading

### Submission:
1. Take a screenshot of your source code and paste it into a Word document. Upload this document as a single PDF file.
2. Raise your hand to ask the TA to check your results.

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

### Assignment 2: Basic Exception Handling
**Required Knowledge**: Basic Exception Handling, Try-Except Block
**Instructions**:
1. Modify the `Car` class to include a method named `print_car_info()` that prints the car's make and model.
2. Add exception handling in the `print_car_info()` method using a try-except block to handle potential errors (e.g., if the attributes are not set using AttributeError to handle exception).
3. Test the method by:
   
Creating a `car1` object with valid `make` and `model` attributes and calling `print_car_info()`.
   
Creating a `car2` object without setting the attributes (or by setting them to `None`) and calling `print_car_info()` to see how the exception is handled.
### Assignment 3: Adding Methods and Exception Handling
**Required Knowledge**: Class Methods, Basic Exception Handling
**Instructions**:
1. Extend the `Car` class by adding a method named `start_engine`.
2. Inside `start_engine`, raise an exception if the car's `make` is `"Unknown"`. Use the built-in `ValueError`.
3. Catch the exception in a `try...except` block and print an appropriate message.
4. Test this by creating a car with `make="Unknown"` and calling `start_engine`.

### Assignment 4: Fuel Check and Basic Exception Handling
**Required Knowledge**: Class Methods, Basic Exception Handling
**Instructions**:
1. Extend the `Car` class by adding an attribute `fuel_level` that represents the car’s current fuel level.
2. Add a method named `check_fuel` that raises a `ValueError` if `fuel_level` is less than 5.
3. Implement a method named `drive` that reduces the `fuel_level` by a certain amount and calls `check_fuel`.
4. Test this by driving the car and catching the `ValueError` if the fuel level gets too low.

```python
my_car = Car("Toyota", "Corolla", 2022, 10)

try:
    my_car.drive(3)  # Should be fine
    my_car.drive(4)  # Should be fine
    my_car.drive(3)  # Should raise ValueError
except ValueError as e:
    print(e)
```

### Assignment 5: Raising and Handling Custom Exceptions
**Required Knowledge**: Custom Exceptions, Raising Exceptions
**Instructions**:
1. Create a custom exception named `OverSpeedError`.
2. Add an attribute `speed` to the `Car` class.
3. Implement a method named `accelerate` that raises `OverSpeedError` if the car's speed exceeds 120.
4. Test this by calling `accelerate` and catching the `OverSpeedError` to print a warning message.

### Assignment 6: Creating and Writing to a Text File Using the `with` Statement
**Required Knowledge**: File Handling, `with` Statement
**Instructions**:
1. Create a Python script named `write_color_file.py`.
2. Write a Python script to create and write to a file named `color.txt`. Add the word "red" using the `with` statement to safely handle the file operations. Use `file.write("red")` to write content to the file.

### Assignment 7: Reading from a Text File and Handling Exceptions
**Required Knowledge**: File Handling, with Statement, Exception Handling in Python
**Instructions**:
1. Continue from Assignment 5. Ensure you have the Car class ready with its current functionalities intact.
2. Create a Method: Add a method named read_color_from_file to your Car class. This method will be responsible for reading the car's color from an external file.
3. File Reading: Use a with statement to safely open and read the contents of the color.txt file created in Assignment 6. The file should contain a single word representing the car’s color. To retrieve the content, you can use file.read().strip().
4. Testing: Create a Car object and test the read_color_from_file method by providing the correct path to the color.txt file and ensuring it works as expected.

### Assignment 8: Implementing Exception Handling
**Required Knowledge**: Exception Handling in Python
**Instructions**:
1. Continue from Assignment 7. Ensure you have the Car class with the read_color_from_file method implemented.
2. Exception Handling: Implement proper exception handling within the read_color_from_file method to manage potential errors such as ValueError, FileNotFoundError, ValueError and other exception.
```
# Initial source code for exception handling.
try:
    # something here
except FileNotFoundError:
    print(f"Error: The file at {filepath} was not found.")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
3. Testing: Create a Car object and test the read_color_from_file method by:
    3.1 Providing the correct path to the color.txt file and ensuring it works as expected.
    3.2 Providing an incorrect or non-existent path to observe how the method handles errors gracefully.

### Assignment 9: Adding a Diagnostics Method
**Required Knowledge**: Class Methods
**Instructions**:
1. Extend the `Car` class by adding a method named `diagnostics` that prints various status information such as `fuel_level` and `speed`.
2. Test this method by creating an instance of the `Car` class and calling `diagnostics` to print the car's status.
3. Call `diagnostics` in a while loop in the main program to print every second. (Hint: use `time.sleep(1)` to delay).

### Assignment 10: Adding a Diagnostics Method
**Required Knowledge**: Basic Multi-threading
**Instructions**:
1. Extend the `Car` class by adding a method named `drive`. This method should contain a while loop that delays for 2 seconds per iteration, prints "Driving... Speed: {self.speed} km/h", and decreases the fuel level by 1 each time it loops.
2. Use threading to set the target of the thread as the `drive` method so that driving can occur in another thread.
3. Test to ensure that both the diagnostics and drive methods run simultaneously. The message from the diagnostics should be printed every second, while a new thread for driving should print the driving message every 2 seconds.