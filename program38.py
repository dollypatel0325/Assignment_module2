#Write a Python program to print all unique values in a dictionary

my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 3}

# Create a set of values
unique_values = set(my_dict.values())

print(unique_values)  
