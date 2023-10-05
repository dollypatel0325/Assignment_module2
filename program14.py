#Write a Python program to split a list into different variables.

def split_list(lst):
    # Assigning each element to a separate variable
    var1, var2, var3 = lst

    return var1, var2, var3

# Example usage
my_list = [1, 2, 3]
var1, var2, var3 = split_list(my_list)

print("Variable 1:", var1)
print("Variable 2:", var2)
print("Variable 3:", var3)
