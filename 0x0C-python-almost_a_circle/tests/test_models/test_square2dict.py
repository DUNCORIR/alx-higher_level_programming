#!/usr/bin/python3
"""Unit tests for the Square class - to_dictionary method."""
import unittest
from models.square import Square

class TestSquareToDictionary(unittest.TestCase):
    """Tests for the to_dictionary method in the Square class."""

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        s1 = Square(10, 2, 1)
        expected_dict = {
            'id': s1.id,
            'size': 10,
            'x': 2,
            'y': 1
        }
        self.assertEqual(s1.to_dictionary(), expected_dict)  # Check if the dictionary matches

    def test_to_dictionary_with_updated_square(self):
        """Test to_dictionary after updating the Square."""
        s1 = Square(10, 2, 1)
        s1.update(89, 4, 5, 6)  # Update the attributes
        expected_dict = {
            'id': 89,
            'size': 4,
            'x': 5,
            'y': 6
        }
        self.assertEqual(s1.to_dictionary(), expected_dict)  # Check if the updated dictionary matches

    def test_to_dictionary_type(self):
        """Test the type of the dictionary returned by to_dictionary."""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertIsInstance(s1_dictionary, dict)  # Check if the returned type is a dictionary

if __name__ == '__main__':
    unittest.main()
