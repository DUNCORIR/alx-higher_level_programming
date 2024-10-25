#!/usr/bin/python3
"""Unit tests for the update method of the Rectangle class."""
import unittest
from models.rectangle import Rectangle

class TestRectangleUpdate(unittest.TestCase):
    """Tests for the update method in the Rectangle class."""

    def test_update_id(self):
        """Test updating only the id attribute."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
    
    def test_update_id_width(self):
        """Test updating id and width attributes."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)

    def test_update_id_width_height(self):
        """Test updating id, width, and height attributes."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)

    def test_update_id_width_height_x(self):
        """Test updating id, width, height, and x attributes."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)

    def test_update_id_width_height_x_y(self):
        """Test updating all attributes: id, width, height, x, and y."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

if __name__ == '__main__':
    unittest.main()
