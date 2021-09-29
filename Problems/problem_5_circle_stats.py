"""
Fill out the functions to calculate the area and circumference of a circle.
Print the result to the user.
"""

import math


def area(r):
    result_area = math.pi * r**2
    return result_area


def circumference(r):
    return math.pi * 2 * r


radius_input = float(input("Circle radius: "))
circle_area = area(radius_input)
circle_circumference = circumference(radius_input)
# print('circle area: ' + str(circle_area))

print('Area: ' + str(circle_area))
print('Circumference: ' + str(circle_circumference))