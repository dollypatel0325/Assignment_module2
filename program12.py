#Write a Python program to get unique values from a list

def get_unique_values(lst):
    unique_values = []
    for item in lst:
        if item not in unique_values:
            unique_values.append(item)
    return unique_values

my_list = [1, 2, 2, 3, 3, 4, 5, 5]
result = get_unique_values(my_list)

print("Unique values in the list:", result)
