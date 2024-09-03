numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
transformed_numbers = [(i * 2 if i % 3 == 0 else i - 2) for i in numbers]
print(transformed_numbers)