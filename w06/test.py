'''
class NegativeValueError(Exception):
    pass

def calculate_square_root(value):
    if value < 0:
        raise NegativeValueError("Cannot calculate square root of a negative number.")
    return value ** 0.5

try:
    calculate_square_root(-10)
except NegativeValueError as e:
    print(e)
'''
try:
    number = "9"
except ValueError:
    print("no no no number")
else:
    print("izza number")