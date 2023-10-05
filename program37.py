#Write a Python program to combine two dictionary adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
#Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Create Counters from the dictionaries
counter1 = Counter(d1)
counter2 = Counter(d2)

# Combine Counters
combined_counter = counter1 + counter2

print(combined_counter)

