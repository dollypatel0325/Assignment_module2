#Write a Python script to concatenate following dictionaries to create a new one.

# Given dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5}

# Concatenate dictionaries to create a new one
concatenated_dict = {}

concatenated_dict.update(dict1)
concatenated_dict.update(dict2)
concatenated_dict.update(dict3)

print("Concatenated dictionary:", concatenated_dict)


