#!/usr/bin/python3
"""Unit tests for the Square class - update method."""
import unittest
from models.square import Square

class TestSquareUpdate(unittest.TestCase):
    """Tests for the update method in the Square class."""

    def test_update_with_args(self):
        """Test updating attributes with *args."""
        s1 = Square(5)
        s1.update(1)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)  # Size should remain the same

        s1.update(1, 2)
        self.assertEqual(s1.size, 2)  # Size updated to 2

        s1.update(1, 2, 3)
        self.assertEqual(s1.x, 3)  # x should be updated to 3

        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.y, 4)  # y should be updated to 4

    def test_update_with_kwargs(self):
        """Test updating attributes with **kwargs."""
        s1 = Square(5)
        s1.update(x=12)
        self.assertEqual(s1.x, 12)  # x should be updated to 12
        self.assertEqual(s1.size, 5)  # Size should remain the same

        s1.update(size=7, y=1)
        self.assertEqual(s1.size, 7)  # Size should be updated to 7
        self.assertEqual(s1.y, 1)  # y should be updated to 1

        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.id, 89)  # id should be updated to 89
        self.assertEqual(s1.size, 7)  # Size should remain 7
        self.assertEqual(s1.y, 1)  # y should remain 1

    def test_update_with_mixed_args_and_kwargs(self):
        """Test update method with mixed *args and **kwargs."""
        s1 = Square(5)
        s1.update(10, 2, x=12, y=3)
        self.assertEqual(s1.id, 10)  # id updated to 10
        self.assertEqual(s1.size, 2)  # size updated to 2
        self.assertEqual(s1.x, 12)  # x updated to 12
        self.assertEqual(s1.y, 3)  # y updated to 3

if __name__ == '__main__':
    unittest.main()
