import unittest
from math import sqrt
from classify_triangle import classify_triangle, is_right

class TestTriangleClassification(unittest.TestCase):
    def test_equilateral_triangle(self):
        # Tests for equilateral triangles
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral Triangle")
        self.assertEqual(classify_triangle(5*10**9, 5*10**9, 5*10**9), "Equilateral Triangle")

    def test_isosceles_triangle(self):
        # Non-right triangle tests
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles Triangle")

        # Right triangle tests
        self.assertEqual(classify_triangle(sqrt(2), sqrt(2), 2), "Isosceles Right Triangle")
        self.assertEqual(classify_triangle(1*10**15, 1*10**15, sqrt(2)), "Isosceles Right Triangle")

    def test_scalene_triangle(self):
        # Non-right scalene triangle
        self.assertEqual(classify_triangle(4, 5, 8), "Scalene Triangle")
        self.assertEqual(classify_triangle(1, 2, 2.9999999), "Scalene Triangle")
        self.assertEqual(classify_triangle(4.000001, 5.000001, 8.000001), "Scalene Triangle")

        # Right scalene triangle cases
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Right Triangle")
        self.assertEqual(classify_triangle(5, 4, 3), "Scalene Right Triangle")
        self.assertEqual(classify_triangle(4, 3, 5), "Scalene Right Triangle")

    def test_invalid_sides(self):
        self.assertEqual(classify_triangle(0, 10, 10), "All sides must be greater than zero")
        self.assertEqual(classify_triangle(10, 0, 10), "All sides must be greater than zero")
        self.assertEqual(classify_triangle(10, 10, 0), "All sides must be greater than zero")
        self.assertEqual(classify_triangle(10, 7, -5), "All sides must be greater than zero")
        self.assertEqual(classify_triangle(0, 0, 0), "All sides must be greater than zero")

    def test_triangle_inequality(self):
        self.assertEqual(classify_triangle(1, 1, 8), "Sum of any two sides must be greater than the third side")
        self.assertEqual(classify_triangle(1, 8, 1), "Sum of any two sides must be greater than the third side")
        self.assertEqual(classify_triangle(8, 1, 1), "Sum of any two sides must be greater than the third side")
        self.assertEqual(classify_triangle(8, 4, 4), "Sum of any two sides must be greater than the third side")

    def test_is_right_function(self):
        # Directly testing the is_right function (helps with coverage)
        self.assertTrue(is_right(3, 4, 5))
        self.assertFalse(is_right(4, 5, 8))
        self.assertTrue(is_right(sqrt(2), sqrt(2), 2))
        self.assertFalse(is_right(5, 5, 8))

if __name__ == '__main__':
    unittest.main()