#Write a Python program to find the repeated items of a tuple.
my_tuple = (1, 2, 3, 2, 4, 1, 3, 5, 1)

# Initialize a dictionary to count occurrences of each item
counts = {}

# Iterate over each item in the tuple
for item in my_tuple:
    # If the item is not yet in the dictionary, add it with a count of 1
    if item not in counts:
        counts[item] = 1
    # If the item is already in the dictionary, increment the count
    else:
        counts[item] += 1

# Identify and print the repeated items
repeated_items = [item for item, count in counts.items() if count > 1]

print("Repeated items in the tuple:", repeated_items)
