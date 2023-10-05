#Write a Python program to convert degree to radian

import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

# Test the function
degree_value = float(input("Enter the angle in degrees: "))
radian_value = degree_to_radian(degree_value)
print(f"{degree_value} degrees is equal to {radian_value} radians.")
