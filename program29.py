#Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'a': 2, 'b': 1, 'c': 3, 'd': 4, 'e': 0}

# Sort the dictionary by value in ascending order
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Dictionary sorted by value (ascending):", sorted_dict_asc)

# Sort the dictionary by value in descending order
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Dictionary sorted by value (descending):", sorted_dict_desc)
