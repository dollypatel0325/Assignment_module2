#Write a Python program to unzip a list of tuples into individual lists.

# Given list of tuples
tuple_list = [('a', 1), ('b', 2), ('c', 3)]

# Unzip the list of tuples
unzipped_list = list(zip(*tuple_list))

print("List of tuples:", tuple_list)
print("Unzipped lists:", unzipped_list)
