'''
**Assignment 2: If-Elif-Else Statement**
**Topic**: If-Else
**Objective**: Implement multiple conditions using if-elif-else statements.
'''

# 1. Define an integer variable named `score` and assign it a value between 0 and 100.
score = int(-99)

# 2. Use an if-elif-else statement to print the grade based on the following criteria:
#     - 90-100: "A"
#     - 80-89: "B"
#     - 70-79: "C"
#     - 60-69: "D"
#     - Below 60: "F"
def compro_grader(score):
	if score >= 90 and score <= 100:
		print("A")
	elif score >= 80 and score <= 89:
		print("B")
	elif score >= 70 and score <= 79:
		print("C")
	elif score >= 60 and score <= 69:
		print("D")
	elif score < 60:
		print("F")
	else:
		print("Invalid score")

# 3. Test the function with different scores to show the result from A to F.
compro_grader(score)
