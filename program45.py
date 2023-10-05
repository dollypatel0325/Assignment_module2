#Write a Python function to check whether a number is perfect or not.

def is_perfect(n):
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n

print(is_perfect(6))  
print(is_perfect(28))  
print(is_perfect(5))  
