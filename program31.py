#Write a Python script to check if a given key already exists in a dictionary.

# Given dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Key to check
key_to_check = 'b'

# Check if the key exists in the dictionary
if key_to_check in my_dict:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")
