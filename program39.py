#Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
#Sample data: {'1': ['a','b'], '2': ['c','d']}
#Expected Output:
#ac ad bc bd

from itertools import product

dict1 = {'1': ['a','b'], '2': ['c','d']}

# Extract values from dictionary and generate all combinations
combinations = product(*dict1.values())

# Print all combinations
for combination in combinations:
    print(''.join(combination))
