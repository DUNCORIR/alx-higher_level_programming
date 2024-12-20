#!/usr/bin/node

// An instance method called print() that prints the rectangle using the character X.
class Rectangle {
  constructor (w, h) {
    // Check if w or h is 0 or not a positive integer
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      // if condition is met, create empty object by returning early
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width)); // Print a row of X.
      }
    }
  }
}

module.exports = Rectangle;
