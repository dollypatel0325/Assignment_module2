#Write a Python script to merge two Python dictionaries

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = dict1.copy()  # Start with a copy of dict1
merged_dict.update(dict2)  # Add items from dict2

print("Merged dictionary:", merged_dict)
