def has_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

my_list1 = [1, 2, 3, 4, 5]
my_list2 = [6, 7, 8, 9, 10]
result = has_common_member(my_list1, my_list2)

print("Do the lists have at least one common member?", result)
