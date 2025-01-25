from math import sqrt
from unittest import TestCase
from classify_triangle import classify_triangle


class Test(TestCase):
    def test_classify_triangle(self):
        assert classify_triangle(5, 5, 5) == "Equilateral Triangle"
        assert classify_triangle(5*10**9, 5*10**9, 5*10**9) == "Equilateral Triangle"

        assert classify_triangle(5, 5, 8) == "Isosceles Triangle"
        assert classify_triangle(sqrt(2), sqrt(2), 2) == "Isosceles Right Triangle"
        assert classify_triangle(1*10**15, 1*10**15, sqrt(2)) == "Isosceles Right Triangle"

        assert classify_triangle(4, 5, 8) == "Scalene Triangle"
        assert classify_triangle(1, 2, 2.9999999) == "Scalene Triangle"
        assert classify_triangle(4.000001, 5.000001, 8.000001) == "Scalene Triangle"
        assert classify_triangle(3, 4, 5) == "Scalene Right Triangle"
        assert classify_triangle(5, 4, 3) == "Scalene Right Triangle"
        assert classify_triangle(4, 3, 5) == "Scalene Right Triangle"

        assert classify_triangle(0, 10, 10) == "All sides must be greater than zero"
        assert classify_triangle(10, 0, 10) == "All sides must be greater than zero"
        assert classify_triangle(10, 10, 0) == "All sides must be greater than zero"
        assert classify_triangle(10, 7, -5) == "All sides must be greater than zero"
        assert classify_triangle(0, 0, 0) == "All sides must be greater than zero"

        assert classify_triangle(1, 1, 8) == "Sum of any two sides must be greater than the third side"
        assert classify_triangle(1, 8, 1) == "Sum of any two sides must be greater than the third side"
        assert classify_triangle(8, 1, 1) == "Sum of any two sides must be greater than the third side"
        assert classify_triangle(8, 4, 4) == "Sum of any two sides must be greater than the third side"
