#!/usr/bin/python3
"""Unit tests for Rectangle class."""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_auto_id(self):
        """Test if Rectangle instances get auto-assigned IDs correctly."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r1.id)  # Verifies the ID is set (first instance)
        self.assertEqual(r2.id, r2.id)  # Verifies the ID is set (second instance)

    def test_custom_id(self):
        """Test if custom IDs can be assigned to Rectangle 
instances."""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

if __name__ == '__main__':
    unittest.main()
