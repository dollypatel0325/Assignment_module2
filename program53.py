#Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

def find_max_min(numbers):
    return max(numbers), min(numbers)

# Get decimal numbers from the user
numbers_input = input("Enter decimal numbers separated by commas (e.g. 1.2, 3.4, 5.6): ")
numbers_list = [float(num.strip()) for num in numbers_input.split(",")]

# Calculate maximum and minimum
maximum, minimum = find_max_min(numbers_list)

print(f"The maximum number is: {maximum}")
print(f"The minimum number is: {minimum}")
