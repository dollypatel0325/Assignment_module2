#Write a Python function to check whether a number is in a given range

def is_in_range(n, start, end):
    if start <= n <= end:
        return True
    else:
        return False
    
print(is_in_range(5, 1, 10))  
print(is_in_range(15, 1, 10))
