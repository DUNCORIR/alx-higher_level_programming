#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test with a normal list of integers
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([0, 1, 2]), 2)
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_empty_list(self):
        # Test with an empty list
        self.assertIsNone(max_integer([]), None)

    def test_strings(self):
        """Test max_integer with a list of strings."""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_single_element(self):
        """Test list with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_floats(self):
        """Test max_integer with a list of floats."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)


if __name__ == '__main__':
    unittest.main()
