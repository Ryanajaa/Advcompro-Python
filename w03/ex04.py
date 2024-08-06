'''
**Assignment 4: Short-Hand If-Else with List Elements**
**Topic**: Short-Hand If-Else
**Objective**: Use short-hand if-else statements to modify list elements.
'''

# 1. Create a list named `numbers` containing a integers from 1 to 5.
numbers = [1, 2, 3, 4, 5]

# 2. Use a list comprehension with a short-hand if-else statement to create a new list named `modified_numbers` where each element is increased by 10 if it is even, or decreased by 1 if it is odd.
modified_numbers = [(i + 10 if i % 2 == 0 else i - 1) for i in numbers]

# 3. Print the `modified_numbers` list.
print(modified_numbers)

# 4. The number line of code should limit to 3 lines only.
# ex. numbers = [1, 2, 3, 4, 5]
# modified_numbers will be [0, 12, 2, 14, 4]
