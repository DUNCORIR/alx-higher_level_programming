#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def test_load_from_file_rectangle(self):
        """Test load_from_file method for Rectangle."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

        # Ensure that the number of loaded rectangles is correct
        self.assertEqual(len(list_rectangles_output), 2)

        # Ensure that loaded rectangles have the same attributes as the input
        for orig, loaded in zip(list_rectangles_input, list_rectangles_output):
            self.assertEqual(orig.width, loaded.width)
            self.assertEqual(orig.height, loaded.height)
            self.assertEqual(orig.x, loaded.x)
            self.assertEqual(orig.y, loaded.y)
            self.assertEqual(orig.id, loaded.id)

        # Clean up the JSON file created during the test
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_load_from_file_square(self):
        """Test load_from_file method for Square."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()

        # Ensure that the number of loaded squares is correct
        self.assertEqual(len(list_squares_output), 2)

        # Ensure that loaded squares have the same attributes as the input
        for orig, loaded in zip(list_squares_input, list_squares_output):
            self.assertEqual(orig.size, loaded.size)
            self.assertEqual(orig.x, loaded.x)
            self.assertEqual(orig.y, loaded.y)
            self.assertEqual(orig.id, loaded.id)

        # Clean up the JSON file created during the test
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_load_from_file_no_file(self):
        """Test load_from_file method when the file does not exist."""
        # Ensure that loading from a non-existent file returns an empty list
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

if __name__ == "__main__":
    unittest.main()
