#Write a Python program to convert a list to a tuple.

def convert_list_to_tuple(lst):
    tup = tuple(lst)
    return tup

# Example usage
my_list = [1, 2, 3, 4, 5]
result = convert_list_to_tuple(my_list)

print("List converted to tuple:", result)
