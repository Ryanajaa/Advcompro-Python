'''
**Assignment 10: Looping Through a Dictionary**
**Topic**: Loops Dictionary
**Objective**: Iterate over keys and values in a dictionary using a for loop.
'''

# 1. Create a dictionary named `inventory` with keys as item names and values as their quantities.
inventory = {
	"laptop": int(70000),
	"watch": int(1000),
	"ipad": int(20000),
	"money": int(0)
}

# 2. Use a for loop to iterate over the dictionary and print each key and value pair.
for key, value in inventory.items():
	print(f"{key}: {value}")
