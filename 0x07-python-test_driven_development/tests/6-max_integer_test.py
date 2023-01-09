#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_value(self):
        self.assertEqual(max_integer([5, 3, 2]), 5)
        self.assertEqual(max_integer([4, 6, 7]), 7)
        self.assertEqual(max_integer([4, 8, 5]), 8)
        self.assertEqual(max_integer([4, 6, -2]), 6)
        self.assertEqual(max_integer([-4, -5, -8]), -4)
        self.assertEqual(max_integer([-4]), -4)
        self.assertEqual(max_integer([5]), 5)

    def test_empty(self):
        self.assertIsNone(max_integer([]))


if __name__ == "__main__":
    unittest.main()
