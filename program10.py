# Write a Python program to find the second smallest number in a list.

def find_second_smallest(lst):
    smallest = float('inf')  # Initialize smallest to infinity
    second_smallest = float('inf')  # Initialize second smallest to infinity

    for num in lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return second_smallest

# Example usage
my_list = [5, 2, 8, 1, 9, 3]
result = find_second_smallest(my_list)

print("Second smallest number:", result)
