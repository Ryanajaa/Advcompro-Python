**Topic**:
1) OOP

**Submission**:  
1) Take a screenshot of your sourcecode to Word and upload as one pdf file.
2) Raise your hand to ask the TA to check the result


#### Assignment 1: Creating a Class
Required Knowledge: Class Definition, Object Instantiation
1. Define a class named `Person`.
2. Add two attributes: `name` and `age`.
3. Instantiate an object of the `Person` class with your name and age.
4. Print the object's attributes.

#### Assignment 2: Instance Methods
Required Knowledge: Instance Methods
1. Add a method `greet` to the `Person` class that prints "Hello, my name is [name] and I am [age] years old."
2. Call the `greet` method from an instantiated object.

### Assignment 3: Adding More Attributes and Methods
1. **Add Attributes**: Extend the `Person` class to include `address` and `phone_number` attributes.
2. **Add Method**: Create a method `update_contact_info` that updates the `address` and `phone_number` attributes.
3. **Display Information**: Add a method `display_info` that prints all the attributes of the `Person` object.

### Assignment 4: Implementing Age Manipulation Methods
1. **Add Method**: Create a method `have_birthday` that increments the `age` attribute by 1 and prints a birthday message.
2. **Display Age**: Modify the `display_info` method to also include a message if the age is 18 or above.

#### Assignment 5: Inheritance
Required Knowledge: Inheritance
1. Define a subclass `Student` that inherits from the `Person` class.
2. Add an attribute `student_id` to the `Student` class.
3. Instantiate an object of the `Student` class and print all its attributes.

#### Assignment 6: Overriding Methods
Required Knowledge: Method Overriding
1. Override the `greet` method in the `Student` class to include the student ID in the greeting.
2. Call the `greet` method from an instantiated `Student` object.


#### Assignment 7: Private Attributes and Methods
Required Knowledge: Encapsulation, Private Attributes
1. Add a private attribute `__salary` to the `Person` class and a method to set its value.
2. Add a method to retrieve the value of the `__salary` attribute.
3. Instantiate an object, set the salary, and print it using the retrieval method.

#### Assignment 8: Static Methods
Required Knowledge: Static Methods
1. Add a static method `is_adult` to the `Person` class that takes an age as an argument and returns `True` if the age is 18 or above, otherwise `False`.
2. Call the `is_adult` method from the class without creating an object.

#### Assignment 9: Polymorphism
Required Knowledge: Polymorphism
1. Define a function `introduce` that takes a `Person` object and calls its `greet` method.
2. Instantiate both `Person` and `Student` objects and pass them to the `introduce` function.

#### Assignment 10: Creating and Using a Package
Required Knowledge: Package Creation, Module Import, Class Design
1. Create a package named `shapes`.
2. Inside the `shapes` package, create a module `geometry.py` and define the following classes:
    - `Shape` (abstract class with an abstract method `area`).
    - `Circle` (inherits from `Shape` and implements the `area` method).
    - `Rectangle` (inherits from `Shape` and implements the `area` method).
3. Create a script outside the `shapes` package named `main.py` to:
    - Import the `Circle` and `Rectangle` classes from the `shapes.geometry` module.
    - Instantiate `Circle` and `Rectangle` objects with sample dimensions.
    - Print the area of the instantiated shapes.