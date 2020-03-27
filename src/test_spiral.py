import unittest
from spiral import spiral


class SpiralTestCase(unittest.TestCase):

    def test_spiral_odd(self):
        self.assertListEqual([
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ], spiral(3))

    def test_spiral_even(self):
        self.assertListEqual([
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7]
        ], spiral(4))

    def test_spiral_one(self):
        self.assertListEqual([[1]], spiral(1))


if __name__ == '__main__':
    unittest.main()
