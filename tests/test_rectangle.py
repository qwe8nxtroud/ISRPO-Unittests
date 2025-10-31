import unittest
from src.rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    # --- area ---
    def test_area_zero(self):
        self.assertEqual(area(0, 10), 0)

    def test_area_square(self):
        self.assertEqual(area(5, 5), 25)

    def test_area_normal(self):
        self.assertEqual(area(3, 7), 21)

    # --- perimeter ---
    def test_perimeter_zero(self):
        # Perimeter with a zero side still uses the formula 2*(a+b)
        self.assertEqual(perimeter(0, 10), 20)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(5, 5), 20)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(3, 7), 20)

if __name__ == "__main__":
    unittest.main()
