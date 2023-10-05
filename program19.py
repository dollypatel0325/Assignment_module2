#Write a Python program to check whether an element exists within a tuple.

def element_exists_in_tuple(element, tup):
    if element in tup:
        return True
    else:
        return False

# Example usage
my_tuple = (1, 2, 3, 4, 5)
element = 3
result = element_exists_in_tuple(element, my_tuple)

print("Does the element exist in the tuple?", result)

