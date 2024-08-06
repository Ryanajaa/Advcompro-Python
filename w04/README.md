**Topic**:
1) Git repository
2) Module and Package
3) Real-world problem in dictionary and list comprehension


**Submission**:  
1) Take a screenshot of your sourcecode to Word and upload as one pdf file.
2) Raise your hand to ask the TA to check the result


**Assignment 1**
**Creating and Initializing a Git Repository on GitHub**
Create and initialize a Git repository on GitHub to track changes in your project.
**Instructions:**
1. Create a new repository on GitHub named `python_assignment_week04`.
2. Clone the repository to your local machine.
3. In the local repository, create a `README.md` file with a brief description of the project.
4. Commit the `README.md` file to the repository.
5. Push the commit to the remote repository on GitHub.
Submission:
- Put the URL of GitHub into the submission pdf file.


**Assignment 2**
Creating a New Branch and Committing Changes
Create a new branch in your Git repository and commit changes to that branch.
**Instructions:**
1. In your local repository, create a new branch named `feature`.
2. Switch to the `feature` branch.
3. Create a file named `main.py` and add some sample Python code such as print("hello world") to it.
4. Commit the `main.py` file to the `feature` branch.
5. Push the `feature` branch to the remote repository on GitHub.
Submission:
- Put the URL of GitHub into the submission pdf file.


**Assignment 3: Merging Branches in Git**
Merge changes from the `feature` branch into the `main` branch in your Git repository.
**Instructions:**
1. Switch to the `main` branch in your local repository.
2. Merge the `feature` branch into the `main` branch.
3. Push the merged changes to the remote repository on GitHub.
Submission:
- Put the URL of GitHub into the submission pdf file.


**Assignment 4: Defining Functions in Python**
Define and use functions in Python to perform specific tasks.
**Instructions:**
1. Create a new Python file named `calculator.py`.
2. Define a function named `add` that takes two arguments and returns their sum.
3. Define a function named `subtract` that takes two arguments and returns their difference.
4. Define a function named `multiply` that takes two arguments and returns their product.
5. Define a function named `divide` that takes two arguments and returns their quotient.
6. Write a main block that calls each function with sample inputs and prints the results.


**Assignment 5: Using Lambda Functions in Python**
Rewrite the functions from Assignment 4 using lambda functions.
**Instructions:**
1. Create a new Python file named `lambda_calculator.py`.
2. Define a lambda function for addition that takes two arguments and returns their sum.
3. Define a lambda function for subtraction that takes two arguments and returns their difference.
4. Define a lambda function for multiplication that takes two arguments and returns their product.
5. Define a lambda function for division that takes two arguments and returns their quotient.
6. Write a main block that calls each lambda function with sample inputs and prints the results.


**Assignment 6: Importing Modules in Python**
Import and use modules in Python to enhance functionality.
Instructions:
1. Create a new Python file named `string_operations.py`.
2. Define functions for common string operations:
    - `reverse_string`: Reverses a given string.
    - `capitalize_string`: Capitalizes the first letter of a given string.
    - `lowercase_string`: Converts all characters in a given string to lowercase.
    - `uppercase_string`: Converts all characters in a given string to uppercase.
3. Create another Python file named `main.py`.
4. Import the `string_operations` module in `main.py`.
5. Use the imported functions to perform operations on sample strings and print the results.
Example of main.py
```python
# Importing the string_operations module
import string_operations as so

# Sample strings and printing results
sample_string = "hello World"

print("Original:", sample_string)
print("Reversed:", so.reverse_string(sample_string))
print("Capitalized:", so.capitalize_string(sample_string))
print("Lowercase:", so.lowercase_string(sample_string))
print("Uppercase:", so.uppercase_string(sample_string))
```

Assignment 7: Creating Packages in Python
Organize your code into packages to improve modularity and reusability. Use the knowledge from Assignments 4 and 6.
**Instructions:**
1. Create a directory named `utilities`.
2. Inside `utilities`, create an `__init__.py` file.
3. Create a module named `calculator.py` inside `utilities` and include the functions defined in Assignment 4.
5. Create a module named `string_operations.py` inside `utilities` and include the functions defined in Assignment 6.
6. Create another Python file named `main.py` outside the `utilities` directory.
7. Import functions from all three modules (`calculator` and `string_operations`) in `main.py`.
8. Use the imported functions to perform operations and print the results.
Example of main.py
```python
# Importing modules from the utilities package
from utilities.calculator import add as add_def, subtract as subtract_def, multiply as multiply_def, divide as divide_def
from utilities.string_operations import reverse_string, capitalize_string, lowercase_string, uppercase_string

# Sample inputs and printing results using calculator.py
print("Using calculator.py:")
print("Addition:", add_def(10, 5))
print("Subtraction:", subtract_def(10, 5))
print("Multiplication:", multiply_def(10, 5))
print("Division:", divide_def(10, 5))

# Sample strings and printing results using string_operations.py
sample_string = "hello World"
print("\nUsing string_operations.py:")
print("Original:", sample_string)
print("Reversed:", reverse_string(sample_string))
print("Capitalized:", capitalize_string(sample_string))
print("Lowercase:", lowercase_string(sample_string))
print("Uppercase:", uppercase_string(sample_string))

```

Expected output:
Using calculator.py:
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0

Using string_operations.py:
Original: hello World
Reversed: dlroW olleh
Capitalized: Hello world
Lowercase: hello world
Uppercase: HELLO WORLD


**Assignment 8: Filtering and Modifying a List of Student Grades**
Imagine you have a list of student grades and you need to create a list of students who have passed (with grades 60 and above) and give a 5% bonus to those grades.
**Instruction**:
1. Define a list of integers named `grades` containing student grades.
   grades = [55, 70, 65, 40, 90, 85, 50, 77]
2. Use a list comprehension to create a new list named `passed_with_bonus` that:
    - Filters the grades to include only those that are 60 and above.
    - Applies a 5% bonus to each of the filtered grades.
3. Print the `passed_with_bonus` list to display the modified grades.
Expected Output:
Grades after filtering and applying bonus: [73.5, 68.25, 94.5, 89.25, 80.85]


**Assignment 9: Filtering Eligible Children for a Fun Park**
Imagine you have a list of dictionaries where each dictionary contains a child's name, age, and height. You need to create a new list of children who are eligible to join a fun park. A child is eligible if their age is greater than 3 and their height is greater than 100 cm.
**Instructions:**
1. Define a list of dictionaries named `children`, where each dictionary contains a `name`, `age`, and `height`.
   children = [ {"name": "Alice", "age": 2, "height": 95}, {"name": "Bob", "age": 4, "height": 105}, {"name": "Charlie", "age": 3, "height": 110}, {"name": "David", "age": 5, "height": 102}, {"name": "Eve", "age": 6, "height": 99} ]
2. Use a list comprehension to create a new list named `eligible_children` that:
    - Filters the children to include only those with age greater than 3 and height greater than 100 cm.
3. Print the `eligible_children` list to display the names, ages, and heights of the eligible children.
**Expected Output:**
Eligible children for the fun park: [{'name': 'Bob', 'age': 4, 'height': 105}, {'name': 'David', 'age': 5, 'height': 102}]


**Assignment 10: Filtering Eligible Children for a Fun Park (Using Lambda Function)**
Student can incorporate a lambda function into the list comprehension for filtering eligible children.
**Instructions:**
1. Define a list of dictionaries named `children`, where each dictionary contains a `name`, `age`, and `height`.
   children = [ {"name": "Alice", "age": 2, "height": 95}, {"name": "Bob", "age": 4, "height": 105}, {"name": "Charlie", "age": 3, "height": 110}, {"name": "David", "age": 5, "height": 102}, {"name": "Eve", "age": 6, "height": 99} ]
2. Use a lambda function named criteria to define the eligibility criteria. `criteria` is a lambda function that takes a dictionary `child` and returns `True` if the child's age is greater than 3 and height is greater than 100 cm.
3. Print the `eligible_children` list to display the names, ages, and heights of the eligible children.
**Expected Output:**
Eligible children for the fun park: [{'name': 'Bob', 'age': 4, 'height': 105}, {'name': 'David', 'age': 5, 'height': 102}]