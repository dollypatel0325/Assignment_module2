#Write a Python program to calculate surface volume and area of a cylinder

import math

def cylinder_volume(r, h):
    return math.pi * r**2 * h

def cylinder_surface_area(r, h):
    base_area = math.pi * r**2
    lateral_area = 2 * math.pi * r * h
    return 2 * base_area + lateral_area

# Get the dimensions of the cylinder from the user
r = float(input("Enter the radius of the cylinder (r): "))
h = float(input("Enter the height of the cylinder (h): "))

# Calculate volume and surface area
volume = cylinder_volume(r, h)
surface_area = cylinder_surface_area(r, h)

print(f"The volume of the cylinder is: {volume:.2f}")
print(f"The surface area of the cylinder is: {surface_area:.2f}")
