#!/usr/bin/python3
"""Unit tests for the Base class - to_json_string method."""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBaseToJsonString(unittest.TestCase):
    """Tests for the to_json_string method in the Base class."""

    def test_to_json_string_empty_list(self):
        """Test to_json_string with an empty list."""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")  # Expect "[]"

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")  # Expect "[]"

    def test_to_json_string_with_dictionaries(self):
        """Test to_json_string with a list of dictionaries."""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()  # Get the dictionary representation of the rectangle
        json_string = Base.to_json_string([dictionary])
        
        expected_json = '[{"id": ' + str(dictionary['id']) + 
                         ', "width": ' + str(dictionary['width']) + 
                         ', "height": ' + str(dictionary['height']) + 
                         ', "x": ' + str(dictionary['x']) + 
                         ', "y": ' + str(dictionary['y']) + '}]'
        self.assertEqual(json_string, expected_json)  # Check if the JSON string matches the expected output

    def test_to_json_string_type(self):
        """Test the type of the JSON string returned by to_json_string."""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertIsInstance(json_string, str)  # Check if the returned type is a string

if __name__ == '__main__':
    unittest.main()
