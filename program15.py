#What is tuple? Difference between list and tuple.

my_list = [1, 2, 3, 4, 5]  # List
my_tuple = (1, 2, 3, 4, 5)  # Tuple

my_list[0] = 10  # Modifying list element
print(my_list)  # Output: [10, 2, 3, 4, 5]

my_tuple[0] = 10  # Error: Tuples are immutable
