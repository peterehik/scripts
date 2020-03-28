import unittest
from spiral import spiral
from one_edit_apart import one_edit_apart
from look_and_say import next_look_and_say_sequence


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


class ScriptsTestCase(unittest.TestCase):

    def test_next_look_and_say_sequence(self):
        self.assertEqual(next_look_and_say_sequence('1'), '11')
        self.assertEqual(next_look_and_say_sequence('11'), '21')
        self.assertEqual(next_look_and_say_sequence('21'), '1211')
        self.assertEqual(next_look_and_say_sequence('1211'), '111221')

    def test_one_edit_apart(self):
        self.assertTrue(one_edit_apart('cat', 'cut'))
        self.assertTrue(one_edit_apart('cats', 'cat'))
        self.assertTrue(one_edit_apart('bth', 'bath'))
        self.assertFalse(one_edit_apart('act', 'cat'))
        self.assertFalse(one_edit_apart('bather', 'bath'))

