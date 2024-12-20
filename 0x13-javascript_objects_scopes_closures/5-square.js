#!/usr/bin/node

// Script that Imports the Rectangle class from 4-rectangle.js
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call Rectangle's constructor with equal width and height
  }
}

module.exports = Square;
