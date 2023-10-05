#Write a Python program to reverse a tuple

def reverse_tuple(tup):
    reversed_tup = tup[::-1]
    return reversed_tup

# Example usage
my_tuple = (1, 2, 3, 4, 5)
result = reverse_tuple(my_tuple)

print("Reversed tuple:", result)
