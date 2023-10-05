def generate_square_list():
    square_list = [num ** 2 for num in range(1, 31)]
    first_five = square_list[:5]
    last_five = square_list[-5:]
    return first_five, last_five

# Example usage
first_five, last_five = generate_square_list()

print("First 5 elements:", first_five)
print("Last 5 elements:", last_five)
