#!/usr/bin/python3
"""Unit tests for the display method of the Rectangle class."""
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys

class TestRectangleDisplay(unittest.TestCase):
    """Tests for the display method in the Rectangle class, with x and y offsets."""

    def setUp(self):
        """Redirect stdout to capture print output."""
        self.held_stdout = StringIO()
        sys.stdout = self.held_stdout

    def tearDown(self):
        """Reset stdout to its original state."""
        sys.stdout = sys.__stdout__

    def test_display_with_x_and_y(self):
        """Test the display method considering x and y."""
        # Create a Rectangle with x=2 and y=2
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        output = self.held_stdout.getvalue()
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(output, expected_output)

        # Reset stdout capture
        self.held_stdout.truncate(0)
        self.held_stdout.seek(0)

        # Create another Rectangle with x=1 and y=0
        r2 = Rectangle(3, 2, 1, 0)
        r2.display()
        output = self.held_stdout.getvalue()
        expected_output = " ###\n ###\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
