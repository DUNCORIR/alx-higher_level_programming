#!/usr/bin/python3
import unittest
from models.base import Base
import json

class TestBase(unittest.TestCase):
    
    def test_from_json_string_valid(self):
        """Test from_json_string with a valid JSON string."""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4}, 
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)

        self.assertIsInstance(list_output, list)  # Check that output is a list
        self.assertEqual(list_output, list_input)  # Check that output matches input
    
    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string."""
        json_list_input = ""
        list_output = Base.from_json_string(json_list_input)

        self.assertIsInstance(list_output, list)  # Check that output is a list
        self.assertEqual(list_output, [])  # Check that output is an empty list
    
    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        json_list_input = None
        list_output = Base.from_json_string(json_list_input)

        self.assertIsInstance(list_output, list)  # Check that output is a list
        self.assertEqual(list_output, [])  # Check that output is an empty list

    def test_from_json_string_invalid(self):
        """Test from_json_string with an invalid JSON string."""
        json_list_input = "[{'id': 89, 'width': 10, 'height': 4}"  # Invalid JSON
        with self.assertRaises(json.JSONDecodeError):
            Base.from_json_string(json_list_input)  # Check for JSONDecodeError

if __name__ == "__main__":
    unittest.main()
