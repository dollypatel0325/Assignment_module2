import random

def select_random_item(lst):
    random_item = random.choice(lst)
    return random_item
my_list = [1, 2, 3, 4, 5]
random_item = select_random_item(my_list)

print("Randomly selected item:", random_item)
