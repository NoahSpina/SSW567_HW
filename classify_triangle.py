from math import isclose

def classify_triangle(a, b, c):
    # Invalid inputs check
    if a <= 0 or b <= 0 or c <= 0:
        return "All sides must be greater than zero"
    if a + b <= c or b + c <= a or a + c <= b:
        return "Sum of any two sides must be greater than the third side"

    if a == b == c:
        return "Equilateral Triangle"

    if a == b or b == c or a == c:
        # Check if it's also a right triangle
        if isRight(a, b, c):
            return "Isosceles Right Triangle"
        return "Isosceles Triangle"

    if isRight(a, b, c):
        return "Scalene Right Triangle"

    # If none of the above, it's scalene
    return "Scalene Triangle"


def isRight(a, b, c):
    # Sort the sides to ensure the largest is treated as the hypotenuse
    sides = sorted([a, b, c])

    # Useful for estimating if the value "is close" enough.
    # This is needed since python is bad at large floating point numbers
    return isclose(sides[0]**2 + sides[1]**2, sides[2]**2, rel_tol=1e-9)

