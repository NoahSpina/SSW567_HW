"""Module for classifying triangles based on side lengths."""

from math import isclose

def classify_triangle(side_a, side_b, side_c):
    """
    Function that classifies a triangle based on side lengths.
    :param side_a: first side length
    :param side_b: second side length
    :param side_c: third side length
    :return: String of the triangle's classification
    """
    # Invalid inputs check
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return "All sides must be greater than zero"
    if side_a + side_b <= side_c or side_b + side_c <= side_a or side_a + side_c <= side_b:
        return "Sum of any two sides must be greater than the third side"

    if side_a == side_b == side_c:
        return "Equilateral Triangle"

    is_triangle_right = is_right(side_a, side_b, side_c)
    if side_a == side_b or side_b == side_c or side_a == side_c:
        # Check if it's also a right triangle, else return isosceles
        return "Isosceles Right Triangle" if is_triangle_right else "Isosceles Triangle"

    return "Scalene Right Triangle" if is_triangle_right else "Scalene Triangle"


def is_right(side_a, side_b, side_c):
    """
    Checks if a triangle is a right triangle or not.
    :param side_a: first side length
    :param side_b: second side length
    :param side_c: third side length
    :return: true if a triangle is a right triangle, false otherwise
    """
    # Sort the sides to ensure the largest is treated as the hypotenuse
    sides = sorted([side_a, side_b, side_c])

    # Useful for estimating if the value "is close" enough.
    # This is needed since python is bad at large floating point numbers
    return isclose(sides[0]**2 + sides[1]**2, sides[2]**2, rel_tol=1e-9)
