#Write a Python program to calculate the area of a parallelogram

def parallelogram_area(b, h):
    return b * h

# Get the dimensions of the parallelogram from the user
b = float(input("Enter the length of the base (b): "))
h = float(input("Enter the perpendicular height (h): "))

# Calculate the area
area = parallelogram_area(b, h)

print(f"The area of the parallelogram with base {b} and height {h} is: {area}")
