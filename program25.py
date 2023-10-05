#Write a Python program to remove an empty tuple(s) from a list of tuples.

tuple_list = [('a', 1), (), ('b', 2), ('c', 3), ()]

# Remove empty tuples using list comprehension
non_empty_tuple_list = [tup for tup in tuple_list if tup]

print("List with empty tuples:", tuple_list)
print("List without empty tuples:", non_empty_tuple_list)

