#!/usr/bin/python3
"""Unit tests for the Rectangle class - to_dictionary method."""
import unittest
from models.rectangle import Rectangle

class TestRectangleToDictionary(unittest.TestCase):
    """Tests for the to_dictionary method in the Rectangle class."""

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        r1 = Rectangle(10, 2, 1, 9)
        expected_dict = {
            'id': r1.id,
            'width': 10,
            'height': 2,
            'x': 1,
            'y': 9
        }
        self.assertEqual(r1.to_dictionary(), expected_dict)  # Check if the dictionary matches

    def test_to_dictionary_with_updated_rectangle(self):
        """Test to_dictionary after updating the Rectangle."""
        r1 = Rectangle(10, 2, 1, 9)
        r1.update(89, 4, 5, 6, 7)  # Update the attributes
        expected_dict = {
            'id': 89,
            'width': 4,
            'height': 5,
            'x': 6,
            'y': 7
        }
        self.assertEqual(r1.to_dictionary(), expected_dict)  # Check if the updated dictionary matches

    def test_to_dictionary_type(self):
        """Test the type of the dictionary returned by to_dictionary."""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertIsInstance(r1_dictionary, dict)  # Check if the returned type is a dictionary

if __name__ == '__main__':
    unittest.main()
