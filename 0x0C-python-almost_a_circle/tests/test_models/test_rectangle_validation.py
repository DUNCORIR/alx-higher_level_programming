#!/usr/bin/python3
"""Unit tests for validating Rectangle attributes."""
import unittest
from models.rectangle import Rectangle

class TestRectangleValidation(unittest.TestCase):
    """Tests for validating Rectangle attribute values."""

    def test_invalid_width_type(self):
        """Test for invalid width type."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_invalid_height_type(self):
        """Test for invalid height type."""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_invalid_x_type(self):
        """Test for invalid x type."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "3", 0)

    def test_invalid_y_type(self):
        """Test for invalid y type."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "4")

    def test_negative_width(self):
        """Test for negative width."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_zero_height(self):
        """Test for zero height."""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_negative_x(self):
        """Test for negative x value."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 0)

    def test_negative_y(self):
        """Test for negative y value."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)

if __name__ == '__main__':
    unittest.main()

