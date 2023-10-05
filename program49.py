#Write a Python program to calculate the area of a trapezoid
def trapezoid_area(a, b, h):
    return (a + b) / 2 * h

# Get the dimensions of the trapezoid from the user
a = float(input("Enter the length of the first parallel side (a): "))
b = float(input("Enter the length of the second parallel side (b): "))
h = float(input("Enter the height (h): "))

# Calculate the area
area = trapezoid_area(a, b, h)

print(f"The area of the trapezoid with sides {a} and {b}, and height {h}, is: {area}")
