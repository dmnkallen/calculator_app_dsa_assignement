import unittest
from circle import Circle
import math

class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.area(), math.pi * 3 ** 2, places=5)

    def test_perimeter(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.perimeter(), 2 * math.pi * 3, places=5)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-5)

if __name__ == '__main__':
    unittest.main()
