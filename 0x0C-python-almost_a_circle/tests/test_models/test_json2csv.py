#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseCSV(unittest.TestCase):

    def test_save_load_from_file_csv_rectangle(self):
        """Test save_to_file_csv and load_from_file_csv methods for Rectangle."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()

        # Ensure that the number of loaded rectangles is correct
        self.assertEqual(len(list_rectangles_output), 2)

        # Ensure that loaded rectangles have the same attributes as the input
        for orig, loaded in zip(list_rectangles_input, list_rectangles_output):
            self.assertEqual(orig.width, loaded.width)
            self.assertEqual(orig.height, loaded.height)
            self.assertEqual(orig.x, loaded.x)
            self.assertEqual(orig.y, loaded.y)
            self.assertEqual(orig.id, loaded.id)

        # Clean up the CSV file created during the test
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")

    def test_save_load_from_file_csv_square(self):
        """Test save_to_file_csv and load_from_file_csv methods for Square."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()

        # Ensure that the number of loaded squares is correct
        self.assertEqual(len(list_squares_output), 2)

        # Ensure that loaded squares have the same attributes as the input
        for orig, loaded in zip(list_squares_input, list_squares_output):
            self.assertEqual(orig.size, loaded.size)
            self.assertEqual(orig.x, loaded.x)
            self.assertEqual(orig.y, loaded.y)
            self.assertEqual(orig.id, loaded.id)

        # Clean up the CSV file created during the test
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")

    def test_load_from_file_csv_no_file(self):
        """Test load_from_file_csv method when the file does not exist."""
        # Ensure that loading from a non-existent file returns an empty list
        self.assertEqual(Rectangle.load_from_file_csv(), [])
        self.assertEqual(Square.load_from_file_csv(), [])

if __name__ == "__main__":
    unittest.main()
