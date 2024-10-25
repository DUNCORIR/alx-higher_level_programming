#!/usr/bin/python3
import unittest
import os
import json
from models.rectangle import Rectangle
from models.base import Base

class TestBaseSaveToFile(unittest.TestCase):
    """Unit tests for the Base class - save_to_file method."""

    def setUp(self):
        """Set up the test environment."""
        # Remove the file if it exists before each test
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Clean up after each test."""
        # Remove the file after each test
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_save_to_file_with_objects(self):
        """Test saving to file with a list of Rectangle objects."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
            self.assertEqual(content, expected)  # Check if the content matches the expected JSON string

    def test_save_to_file_with_none(self):
        """Test saving to file with None."""
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")  # Expect an empty JSON array

    def test_save_to_file_empty_list(self):
        """Test saving to file with an empty list."""
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")  # Expect an empty JSON array

    def test_save_to_file_overwrite(self):
        """Test saving to file to ensure it overwrites."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])

        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r2])  # This should overwrite the previous file

        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected = '[{"id": 1, "width": 2, "height": 4, "x": 0, "y": 0}]'
            self.assertEqual(content, expected)  # Check that the content matches the latest save

if __name__ == '__main__':
    unittest.main()
