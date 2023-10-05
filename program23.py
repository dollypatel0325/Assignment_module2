#Write a Python program to replace last value of tuples in a list. 

def replace_last_value(tuples_list, new_value):
    modified_list = []
    for tup in tuples_list:
        modified_tuple = tup[:-1] + (new_value,)
        modified_list.append(modified_tuple)
    return modified_list

# Example usage
my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 10
result = replace_last_value(my_list, new_value)

print("Modified list:", result)
