#!/usr/bin/python3
"""Unit tests for the display method of the Rectangle class."""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle

class TestRectangleDisplay(unittest.TestCase):
    """Tests for the display method in the Rectangle class."""

    def test_display_rectangle(self):
        """Test if display prints a rectangle of the correct size."""
        # Capture output for a 4x6 rectangle
        r1 = Rectangle(4, 6)
        expected_output1 = "####\n####\n####\n####\n####\n####\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            r1.display()
            output = buffer.getvalue()
        self.assertEqual(output, expected_output1)

        # Capture output for a 2x2 rectangle
        r2 = Rectangle(2, 2)
        expected_output2 = "##\n##\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            r2.display()
            output = buffer.getvalue()
        self.assertEqual(output, expected_output2)

if __name__ == '__main__':
    unittest.main()
