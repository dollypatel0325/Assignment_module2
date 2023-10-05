#Write a Python program to read a random line from a file.

import random

def read_random_line(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return random.choice(lines)

# Use the function
print(read_random_line('my_file.txt')) 
