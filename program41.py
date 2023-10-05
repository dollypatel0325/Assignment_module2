#Write a Python program to combine values in python list of dictionaries. Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, o {'item': 'item1', 'amount': 750}]
#Expected Output:
#Counter ({'item1': 1150, 'item2': 300})

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

# Initialize an empty dictionary to store the combined values
combined_values = {}

# Iterate over each dictionary in the list
for d in data:
    # If the item is already in the combined_values dictionary, add the amount to the existing amount
    # Otherwise, set the amount for the item in the combined_values dictionary
    if d['item'] in combined_values:
        combined_values[d['item']] += d['amount']
    else:
        combined_values[d['item']] = d['amount']

print(combined_values)  
