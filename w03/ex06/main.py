# 3. Create another Python file named `main.py`.
# 4. Import the `string_operations` module in `main.py`.
import string_operations as so

# 5. Use the imported functions to perform operations on sample strings and print the results.
sample_string = "hello World"

print("Original:", sample_string)
print("Reversed:", so.reverse_string(sample_string))
print("Capitalized:", so.capitalize_string(sample_string))
print("Lowercase:", so.lowercase_string(sample_string))
print("Uppercase:", so.uppercase_string(sample_string))