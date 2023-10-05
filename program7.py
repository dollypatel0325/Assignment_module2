def get_unique_elements(lst):
    unique_list = list(set(lst))
    return unique_list

my_list = [1, 2, 2, 3, 3, 4, 5, 5]
result = get_unique_elements(my_list)

print("Unique elements in the list:", result)
