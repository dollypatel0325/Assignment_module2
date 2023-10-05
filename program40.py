#Write a Python program to find the highest 3 values in a dictionary

my_dict = {'a': 5, 'b': 14, 'c': 32, 'd': 7, 'e': 23, 'f': 56, 'g': 1}

# Find the highest 3 values
highest_3_values = sorted(my_dict.values(), reverse=True)[:3]

print(highest_3_values)  
