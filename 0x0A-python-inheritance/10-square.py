#!/usr/bin/python3
"""Main program to test the Square class."""

# Import the Square class from 9-rectangle module
Square = __import__('9-rectangle').Square

# Create an instance of Square
square = Square(5)

# Print the area of the square
print(f"The area of the square is: {square.area()}")

# Print the string representation of the square
print(square)
