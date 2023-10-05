def get_list_stats(numbers):
    if not numbers:
        return None, None, 0

    largest = numbers[0]
    smallest = numbers[0]
    total = 0

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
        total += num

    return largest, smallest, total

my_list = [52,22,10,89,28,5]
largest_num, smallest_num, total_sum = get_list_stats(my_list)

print("Largest number:", largest_num)
print("Smallest number:", smallest_num)
print("Sum of all numbers:", total_sum)
