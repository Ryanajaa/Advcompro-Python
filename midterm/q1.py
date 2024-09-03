def calculate_grade(score):
    if score >= 95 and score <= 100:
        return "A+"
    elif score >= 90 and score <= 94:
        return "A"
    elif score >= 80 and score <= 89:
        return "B"
    elif score >= 70 and score <= 79:
        return "C"
    elif score >= 60 and score <= 69:
        return "D"
    elif score <= 60:
        return"F"
    else:
        return "Error, Score is not in criteria"

print(calculate_grade(100))
print(calculate_grade(91))
print(calculate_grade(85))
print(calculate_grade(70))
print(calculate_grade(69))
print(calculate_grade(50))
print(calculate_grade(-20))
print(calculate_grade(2000))