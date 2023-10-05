#Write a Python function that checks whether a passed string is palindrome or not

def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphabetic characters
    s = ''.join(c for c in s.lower() if c.isalpha())
    
    # Check if the string is a palindrome
    return s == s[::-1]

print(is_palindrome('A man a plan a canal Panama')) 
print(is_palindrome('Hello'))  
