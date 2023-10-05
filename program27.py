#Write a Python program to convert a list of tuples into a dictionary.

def convert_to_dict(tuples_list):
    return dict(tuples_list)

# Example usage
tuples_list = [('a', 1), ('b', 2), ('c', 3)]

result_dict = convert_to_dict(tuples_list)
print("Converted dictionary:", result_dict)
