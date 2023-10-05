#Write a Python program to check multiple keys exists in a dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

keys_to_check = ['a', 'b', 'e']

for key in keys_to_check:
    if key in my_dict:
        print(f"Key '{key}' exists in the dictionary.")
    else:
        print(f"Key '{key}' does not exist in the dictionary.")
