1) Take a screenshot of your sourcecode to Word and upload as one pdf file.
2) Raise your hand to ask the TA to check the result

**Assignment 1: Basic If-Else Statement** 
**Topic**: If-Else
**Objective**: Understand basic if-else statements in Python.
1. Define an integer variable named `number` and assign it a value.
2. Use an if-else statement to check if the number is even or odd.
3. Print "Even" if the number is even, otherwise print "Odd".

**Assignment 2: If-Elif-Else Statement**
**Topic**: If-Else
**Objective**: Implement multiple conditions using if-elif-else statements.
1. Define an integer variable named `score` and assign it a value between 0 and 100.
2. Use an if-elif-else statement to print the grade based on the following criteria:
    - 90-100: "A"
    - 80-89: "B"
    - 70-79: "C"
    - 60-69: "D"
    - Below 60: "F"
3. Test the function with different scores to show the result from A to F.

**Assignment 3: Short-Hand If-Else Statement**
**Topic**: Short-Hand If-Else
**Objective**: Use short-hand if-else statements for compact code.
1. Define a variable `age` and assign it the value 18.
2. Define a variable `status` and use a short-hand if-else statement to assign the value "Adult" if a person's age is 18 or above, and "Minor" if below 18 in one line.
3. Print the result.
4. The number line of code should limit to 3 lines only.


**Assignment 4: Short-Hand If-Else with List Elements**
**Topic**: Short-Hand If-Else
**Objective**: Use short-hand if-else statements to modify list elements.
1. Create a list named `numbers` containing a integers from 1 to 5.
2. Use a list comprehension with a short-hand if-else statement to create a new list named `modified_numbers` where each element is increased by 10 if it is even, or decreased by 1 if it is odd.
3. Print the `modified_numbers` list.
4. The number line of code should limit to 3 lines only.
ex. numbers = [1, 2, 3, 4, 5]
modified_numbers will be [0, 12, 2, 14, 4]

**Assignment 5: For Loop with a List**
**Topic**: For Loops
**Objective**: Iterate over elements in a list using a for loop.
1. Create a list named `fruits` containing "apple", "banana", "cherry".
2. Use a for loop to iterate over the list and print each fruit.

**Assignment 6: For Loop with a Range**
**Topic**: For Loops
**Objective**: Use a for loop with a range to iterate over a sequence of numbers.
1. Use a for loop to iterate over the numbers from 1 to 10.
2. Print the square of each number.

**Assignment 7: Basic While Loop**
**Topic**: While Loops
**Objective**: Understand basic while loops in Python.
1. Use a while loop to print the numbers from 1 to 5.

**Assignment 8: Using Break in a Loop**
**Topic**: Loops Flow Control
**Objective**: Understand how to use the break statement to exit a loop early.
1. Use a for loop to iterate over the numbers from 1 to 10 using range function.
2. Use a break statement to exit the loop when the number is 5.
3. Print the numbers iterated before the break.

**Assignment 9: Using Continue in a Loop**
**Topic**: Loops Flow Control
**Objective**: Understand how to use the continue statement to skip iterations in a loop.
1. Use a for loop to iterate over the numbers from 1 to 10 using range function.
2. Apply a continue statement to skip the number 5.
3. Print number of each loop

**Assignment 10: Looping Through a Dictionary**
**Topic**: Loops Dictionary
**Objective**: Iterate over keys and values in a dictionary using a for loop.
1. Create a dictionary named `inventory` with keys as item names and values as their quantities.
2. Use a for loop to iterate over the dictionary and print each key and value pair.

**Homework 1: For Loop with a Specified Range**
**Objective**: Use the range function in a for loop to iterate over a sequence of numbers.
1. Use a for loop with `range` to iterate over the numbers from 0 to 20, stepping by 2.
2. Print each number.

**Homework 2: Lists of Dictionaries in Python**
**Objective**: To practice creating, manipulating, and analyzing lists of dictionaries in Python. This assignment will help you understand how to work with complex data structures and apply various Python techniques.
1. Create a list named students that contains dictionaries. Each dictionary should represent a student with the following keys: name, age, grade, and major.
    Example:
    students = [
  	  {"name": "Alice", "age": 20, "grade": 85, "major": "Physics"},
  	  {"name": "Bob", "age": 22, "grade": 90, "major": "Chemistry"},
  	  {"name": "Charlie", "age": 19, "grade": 78, "major": "Mathematics"},
  	  {"name": "Diana", "age": 21, "grade": 92, "major": "Biology"}
    ]
2. Using a for loop to update Alice's grade to 87. Iterate over the list and update the grade for the student named Alice.
3. Using a for loop to update Diana's major to "Programming". Iterate over the list and update the major for the student named Diana.
4. Print the updated list of students. After making the updates, use a for loop to print each dictionary in the list to verify the changes.
    Expected output:
    students = [
  	  {"name": "Alice", "age": 20, "grade": 87, "major": "Physics"},
  	  {"name": "Bob", "age": 22, "grade": 90, "major": "Chemistry"},
  	  {"name": "Charlie", "age": 19, "grade": 78, "major": "Mathematics"},
  	  {"name": "Diana", "age": 21, "grade": 92, "major": "Programming"}
    ]

**Homework 3:  Adding Dictionary Items in a List of Dictionaries**
Objective: Practice adding items in dictionaries within a list.
1. Using data from the homework 2.
2. Add a new key "graduation_year" with a value to each student's dictionary. Assume all students are expected to graduate in 2024.
3. Remove the key "age" from each student's dictionary.
4. Print the updated list of students.
    Expected Output:
    {'name': 'Alice', 'grade': 85, 'major': 'Physics', 'graduation_year': 2024}
    {'name': 'Bob', 'grade': 90, 'major': 'Chemistry', 'graduation_year': 2024}
    {'name': 'Charlie', 'grade': 78, 'major': 'Mathematics', 'graduation_year': 2024}
    {'name': 'Diana', 'grade': 92, 'major': 'Biology', 'graduation_year': 2024}

