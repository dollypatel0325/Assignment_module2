#Write a Python program to check whether a list contains a sub list

def has_sublist(lst, sublist):
    if len(sublist) > len(lst):
        return False

    for i in range(len(lst) - len(sublist) + 1):
        if lst[i:i + len(sublist)] == sublist:
            return True

    return False

main_list = [1, 2, 3, 4, 5, 6, 7]
sub_list = [3, 4, 5]
result = has_sublist(main_list, sub_list)

print("Does the list contain the sublist?", result)
